import pandas as pd

df = pd.read_csv('tweets.csv')
df = df[~df['full_text'].str.contains('RT|\@|»')]
df.to_csv('tweets_processed.csv', encoding='utf_8_sig')
