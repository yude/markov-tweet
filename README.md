# markov-text-generator
Generate tweets like yours by using Markov-chains.

## Dependencies
- Python 3.x
- pandas
- Mecab
- mecab-python3

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
### Running this bot regularly
Use [crontab](https://linuxjm.osdn.jp/html/cron/man5/crontab.5.html) to run this bot regularly.  
#### Example
`*/20 * * * * /usr/bin/python3 /path/to/your/run.py`  
This definition make this bot run every 20 minutes. (`*:00`, `*:20`, `*:40`)

## References
- https://github.com/o-tomox/TextGenerator

## Example
- [@yuderobot](https://twitter.com/yuderobot)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).