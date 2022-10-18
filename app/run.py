#-*- coding: utf-8 -*-

import tweepy
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv
from text_generator import create_sentence

# Import keys from .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
CK = os.environ.get("CK")
CS = os.environ.get("CS")
AT = os.environ.get("AT")
AS = os.environ.get("AS")

# Generate tweepy objects
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

# Remove risky words from result
def remover(result):
  # Load banned.json
  json_open = open('data/banned.json', 'r')
  json_load = json.load(json_open)
  # Delete detected words from original sentences
  for w in json_load['words']:
    result = result.replace(w, '')
  return result

def main():
  # Get original sentences generated from markov-chains
  ## Run text_generator.py to get sentence.
  ## Put the generated sentence into 'result' variable
  result = create_sentence()

  # Remove risky words from result
  result = remover(result)

  # Call Twitter API to tweet
  # api.update_status(result)
  print("✅ Tweeted: ", result)

if __name__ == '__main__':
  main()
