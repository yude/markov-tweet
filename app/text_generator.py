import os
import re
import pandas as pd
import pickle
import tweepy
import MeCab

from os.path import join, dirname
from dotenv import load_dotenv

# Import keys from .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
CK = os.environ.get("CK")
CS = os.environ.get("CS")
AT = os.environ.get("AT")
AS = os.environ.get("AS")
N = os.environ.get("N")

# Generate tweepy objects
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

# MeCab thing
tagger = MeCab.Tagger('-d /usr/lib64/mecab/dic/mecab-ipadic-neologd -Ochasen')

def read_tweets():
    unwanted_chars = ['\n', '\r', '\u3000', '-', '｜']
    unwanted_patterns = [re.compile(r'《.*》'), re.compile(r'［＃.*］')]

    # Retrieve tweets from user
    tweets = api.user_timeline(
            screen_name=os.environ.get("SOURCE"),
            count=200
            )

    full_text = []

    # Deep copy source array
    for tweet in tweets:
        text = tweet.text

        match = re.search(r'RT|\@|»|https', text)
        if match is None:
            for char in unwanted_chars:
                text = text.replace(char, '')
            for pattern in unwanted_patterns:
                text = re.sub(pattern, '', text)

            full_text.append(text)

    return "。".join(full_text)

def normalize_text(text):
    #blacklist = '[ @0-9a-zA-Z\|/:%\$&?\(\)~\.=\+\-_「」（）／　：・”“]+'
    blacklist = '[ @\|/:%\$&?\(\)~\.=\+\-_「」（）／　：・”“]+'
    return re.sub(blacklist, '', text)

def to_sentences(text):
    delimiter = "。|．|\."
    return re.split(delimiter, text)

def to_morphemes(sentence):
    assert isinstance(sentence, str)
    ms = ['__B__']
    node = tagger.parseToNode(sentence)
    while node:
        m = node.surface
        if len(m) > 0:
            ms.append(m)
        node = node.next
    ms.append('__E__')
    return ms

def to_triplets(morphemes):
    triplets = []
    if len(morphemes) >= 3:
        for i in range(len(morphemes)-2):
            triplet = tuple(morphemes[i:i+3])
            triplets.append(triplet)
    return triplets

def flatten_list(ls):
    res = []
    for item in ls:
        res.extend(item)
    return res

def create_triplets(text):
    text = normalize_text(text)
    sentences = to_sentences(text)
    triplets = [to_triplets(to_morphemes(sentence))
                for sentence in sentences]
    return flatten_list(triplets)


def save_to_pickle(path, obj):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)


def load_from_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def call_triplets():
    text = read_tweets()
    triplets = create_triplets(text)
    return triplets

def matched_triplets(triplets, cond):
    l = len(cond)
    return [triplet for triplet in triplets if triplet[:l] == cond[:l]]

def random_triplet(triplets, cond):
    matched = matched_triplets(triplets, cond)
    return random.choice(matched)

def create_sentence(triplets):
    ms = []
    triplet = random_triplet(triplets, ('__B__',))
    ms.append(triplet[1])
    while triplet[2] != '__E__':
        triplet = random_triplet(triplets, triplet[1:3])
        ms.append(triplet[1])
    return ''.join(ms) + ' '

def generate_sentence():
    triplets = call_triplets()
    n = int(N)

    result = ""
    for i in range(n):
        try:
            result += create_sentence(triplets)
        except:
            pass
    
    return result
    

if __name__ == '__main__':
    print(generate_sentence())
