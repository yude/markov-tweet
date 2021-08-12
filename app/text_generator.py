import os
import pandas as pd
import re
import pickle
import random
import MeCab
from os.path import join, dirname
from dotenv import load_dotenv

tagger = MeCab.Tagger('-Ochasen')
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
N = os.environ.get("N")

def read_tweets():
    df = pd.read_csv('data/tweets.csv')
    tweets = df['full_text']
    return "。".join(tweets)

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

def load_or_create_triplets():
    path = 'data/triplets.pkl'
    if os.path.isfile(path):
        return load_from_pickle(path)
    else:
        text = read_tweets()
        triplets = create_triplets(text)
        save_to_pickle(path, triplets)
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

def main():
    triplets = load_or_create_triplets()
    n = int(N)
    for i in range(n):
        try:
            print(create_sentence(triplets), end='')
        except:
            pass

if __name__ == '__main__':
    main()
