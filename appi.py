# -*- coding: utf-8 -*-
import requests
import pandas as pd
import time
import os
import matplotlib.pyplot as plt
from datetime import datetime
from pandas.plotting import register_matplotlib_converters

# Register matplotlib converters
register_matplotlib_converters()

# Get the current date
current_date = datetime.now()

# Function to get historical klines from Binance
def get_historical_klines(symbol, interval, start_time, end_time=None):
    url = 'https://api.binance.com/api/v3/klines'
    params = {
        'symbol': symbol,
        'interval': interval,
        'startTime': start_time,
        'endTime': end_time,
        'limit': 1000  # Max limit per request
    }
    response = requests.get(url, params=params)
    print("Request URL: {}".format(response.url))
    print("Response Status Code: {}".format(response.status_code))
    data = response.json()
    print("API Response: {}".format(data))
    return data

# Function to get USD to INR conversion rate
def get_usd_to_inr_rate():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()
    return data['rates']['INR']

# Function to get the market cap of a specific coin
def get_coin_market_cap(symbol):
    url = 'https://api.coingecko.com/api/v3/coins/' + symbol
    response = requests.get(url)
    data = response.json()
    return data['market_data']['market_cap']['usd']

# Function to get total market cap of all cryptocurrencies
def get_total_market_cap():
    url = 'https://api.coingecko.com/api/v3/global'
    response = requests.get(url)
    data = response.json()
    return data['data']['total_market_cap']['usd']

# Convert a date string to milliseconds
def date_to_milliseconds(date_str):
    return int(pd.Timestamp(date_str).timestamp() * 1000)

# Fetch 5 years of data
symbol = 'BTCUSDT'  # Corrected symbol for Binance
interval = '1d'
start_date = '2019-07-23'  # Adjust this to 5 years back from today
end_date = current_date.strftime('%Y-%m-%d')   # Adjust this to today's date
start_time = date_to_milliseconds(start_date)
end_time = date_to_milliseconds(end_date)

# Get USD to INR conversion rate
usd_to_inr_rate = get_usd_to_inr_rate()
print("USD to INR Conversion Rate: {}".format(usd_to_inr_rate))

# Get market cap of Bitcoin
bitcoin_market_cap = get_coin_market_cap('bitcoin')
print("Bitcoin Market Cap (USD): {}".format(bitcoin_market_cap))

# Fetch total market cap
total_market_cap = get_total_market_cap()
print("Total Cryptocurrency Market Cap (USD): {}".format(total_market_cap))

# Fetch data in chunks
data = []
while start_time < end_time:
    new_data = get_historical_klines(symbol, interval, start_time, end_time)
    
    # Check if new_data is empty or not a list
    if not isinstance(new_data, list) or len(new_data) == 0:
        print("No more data or invalid response.")
        break
    
    data.extend(new_data)
    
    # Update start_time to the timestamp of the last fetched data plus one millisecond
    start_time = new_data[-1][0] + 1
    # Avoid hitting rate limits
    time.sleep(0.5)

# Convert data to DataFrame
columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time',
           'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume',
           'taker_buy_quote_asset_volume', 'ignore']
df = pd.DataFrame(data, columns=columns)
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df.set_index('timestamp', inplace=True)

# Convert columns to numeric
df[['open', 'high', 'low', 'close']] = df[['open', 'high', 'low', 'close']].apply(pd.to_numeric, errors='coerce')

# Check if conversion was successful
print(df[['open', 'high', 'low', 'close']].head())

# Convert USDT prices to INR
df['close'] = df['close'] * usd_to_inr_rate
df['open'] = df['open'] * usd_to_inr_rate
df['high'] = df['high'] * usd_to_inr_rate
df['low'] = df['low'] * usd_to_inr_rate

# Add Bitcoin market cap to DataFrame
df['market_cap'] = bitcoin_market_cap

# Calculate Bitcoin dominance
if total_market_cap:
    df['dominance'] = (bitcoin_market_cap / total_market_cap) * 100

# Select relevant columns
df = df[['open', 'high', 'low', 'close', 'market_cap', 'dominance', 'volume']]
df = df.astype(float)

# Path to your CSV file
file_path = 'binance_btcinr_5years.csv'  # Changed file name to reflect BTCINR

# Check if the file exists
if os.path.exists(file_path):
    # If it exists, delete it
    os.remove(file_path)

# Now save your DataFrame to a new CSV file
df.to_csv(file_path)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['close'], label='Price (INR)')
plt.title('Bitcoin Price (BTC/INR) - Last 5 Years')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.show()

