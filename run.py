#-*- coding: utf-8 -*-

import tweepy
import subprocess

# Put your keys into this area
CK=""
CS=""
AT=""
AS=""

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
 result = result.replace('[tweet] ', '')
 result = result.replace('殺', '')
 result = result.replace('爆破', '')
 result = result.replace('爆発', '')
 result = result.replace('死', '')
 result = result.replace('@', '')
 result = result.replace('#', '')

 api.update_status(result)

if __name__ == '__main__':
  main()
