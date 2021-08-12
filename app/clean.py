import pandas as pd

df = pd.read_csv('data/tweets.csv')
df = df[~df['full_text'].str.contains('RT|\@|»|https')]
df.to_csv('data/tweets_processed.csv', encoding='utf_8_sig')
