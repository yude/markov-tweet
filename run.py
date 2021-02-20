#-*- coding: utf-8 -*-

import tweepy
import subprocess
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv


# Import keys from .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
CK = os.environ.get("CK")
CS = os.environ.get("CS")
AT = os.environ.get("AT")
AS = os.environ.get("AS")

# Generate Twitter objects
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

# Tweet
def res_cmd(cmd):
  return subprocess.Popen(
      cmd, stdout=subprocess.PIPE,
      shell=True).communicate()[0]

def main():
 cmd = ("python3 text_generator.py")
 # Remove risky words from result
 result = res_cmd(cmd)
 result = result.decode()
 result = result.replace('殺', '')
 result = result.replace('爆破', '')
 result = result.replace('爆発', '')
 result = result.replace('死', '')
 result = result.replace('@', '')
 result = result.replace('#', '')

 api.update_status(result)

if __name__ == '__main__':
  main()
