#-*- coding: utf-8 -*-

import tweepy
import subprocess

# 各種キーを代入する
CK=""
CS=""
AT=""
AS=""

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

# ツイート
def res_cmd(cmd):
  return subprocess.Popen(
      cmd, stdout=subprocess.PIPE,
      shell=True).communicate()[0]

def main():
 cmd = ("python3 text_generator.py")
 result = res_cmd(cmd)
 result = result.decode()
 result = result.replace('[tweet] ', '')
 result = result.replace('殺', '')
 result = result.replace('爆破', '')
 result = result.replace('爆発', '')
 result = result.replace('死', '')
 result = result.replace('@', '')
 api.update_status(result)

if __name__ == '__main__':
  main()
