# markov-text-generator
マルコフ連鎖を使って自分のツイートっぽい文章を生成する

## 前提

以下のソフトウェアがインストール済であること。

- Python 3
- pandas
- Mecab
- mecab-python3

## 準備

Twitterの公式サイトから、自分のツイートをダウンロードしておく。
その zip ファイルを解凍すると、tweets.csv というファイルが現れるので、
それをこのプロジェクトのあるディレクトリに置いておく。

## 実行

```
$ python text_generator.py
```

## 参考

- https://github.com/o-tomox/TextGenerator

アルゴリズムについてはこのコードに基づいている。
コードの一部については、そのまま利用している部分がある。
ただし、全体の構成は私が大幅に変更した。
