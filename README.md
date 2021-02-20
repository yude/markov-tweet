# markov-text-generator
Generate tweets like yours by using Markov-chains.

## Requirements
- Python 3
- pandas
- Mecab
- mecab-python3

## Setup
1. Download your tweets from Twitter (Download an archive of your data).
1. Convert `tweets.js` into `tweets.csv` by using [Twitter archive JS to CSV converter](http://tweetjstocsv.glitch.me/)
1. Put `tweets.csv` into this repository.

## Run
```
$ python3 run.py
```
Use crontab in order to run this bot regularly.
Example: `*/20 * * * * /usr/bin/python3 /path/to/your/run.py`

## References
- https://github.com/o-tomox/TextGenerator

## Example
- [@yuderobot](https://twitter.com/yuderobot)
