import yfinance as yf
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Define the ticker symbol
ticker = input('Enter Ticker: ')
# ticker = 'TSLA'
# Get data on this ticker
tickerData = yf.Ticker(ticker)

# Get the historical prices for this ticker
df = tickerData.history(period='1d', start='2013-1-1', end='2023-7-1')
df.reset_index(inplace=True)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# See your data
print(f'You are viewing {ticker}')
# print(df.columns)
# variables
high_price = df['High']
low_price = df['Low']
closing_price = df['Close']
open_price = df['Open']
date = df['Date']
df['date_unix'] = df['Date'].apply(lambda x: x.timestamp())
date2 = df['date_unix']
# adj_close = df['Adj Close']
volume = df['Volume']
dividends = df['Dividends']
splits = df['Stock Splits']

sns.set_theme(style="darkgrid")
sns.set_context(font_scale=1.4)


sns.jointplot(x=date2, y=closing_price, kind='reg', color='#FF7F70')
plt.title(f'Closing Price of {ticker} Stock Over Time')
plt.ylabel('Closing Price (USD)')
plt.xlabel('')
ax = plt.gca()
x_ticks = ax.get_xticks()
ax.set_xticks(x_ticks)
ax.set_xticklabels(pd.to_datetime(x_ticks, unit='s').strftime('%Y-%m-%d'))
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
