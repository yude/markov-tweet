# markov-tweet
Automatically generate and tweet sentences like your daily tweets by using markov-chain.

## Dependencies
- Python 3.x
- pandas
- MeCab
- mecab-python3
- tweepy

## Setup
1. Install Python 3.x, MeCab in the way of your environment.
1. Run `pip install -r requirements.txt` to install depending Python packages.
1. Download your tweets from Twitter (Download an archive of your data).
1. Convert `tweets.js` into `tweets.csv` by using [Twitter archive JS to CSV converter](http://tweetjstocsv.glitch.me/).  
Warning: Don't forget to rename `.csv` file!
1. Put `tweets.csv` into this repository.
1. Copy `.env.sample` as `.env`.
1. Put your tokens related to Twitter into `.env`. (You can get one from [Developer Portal](https://developer.twitter.com/en/portal/dashboard).)
1. (Optional: Edit `banned.json` to add / remove banned words.)

## Run
```
$ python3 run.py
```

### Change settings
#### Remove RT and replies from source
1. If you already run this bot, please delete `triplets.pkl`.
1. Run `python3 remove_rt_and_reply.py` on this repository.  
   Warning: Make sure you have `tweets.csv` inside the bot directory!
1. Rename `tweets.csv` as `tweets.csv.bak`.
1. Rename `tweets_processed.csv` as `tweets.csv`.
1. Run `python3 run.py`.

#### Change the number of sentences
1. Open `.env` and change the value of `N`.
1. Run `python3 run.py`.


### Running this bot regularly
Use [crontab](https://linuxjm.osdn.jp/html/cron/man5/crontab.5.html) to run this bot regularly.  
#### Example
`*/20 * * * * cd /path/to/your/markov-tweet; /usr/bin/python3 /path/to/your/run.py`  
This definition make this bot run every 20 minutes. (`*:00`, `*:20`, `*:40`)

## References
- https://github.com/o-tomox/TextGenerator

## Example
- [@yuderobot](https://twitter.com/yuderobot)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
