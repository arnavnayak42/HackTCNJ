import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import *


#Get the data for the stocks
stock_symbol = input("What is the desired stock symbol: ")
start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
end_date = datetime.now().strftime('%Y-%m-%d')
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)


#This is the 20 Day Moving Average
stock_data['MA20'] = stock_data['Close'].rolling(window=20).mean()

#This is the 50 Day Moving Average 
stock_data['MA50'] = stock_data['Close'].rolling(window=50).mean()

# Plot stock data
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'], label='Closing Price')
plt.plot(stock_data['MA20'], label='MA20')
plt.plot(stock_data['MA50'], label='MA50')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()

# Implement moving average crossover strategy
buy_signals = []
sell_signals = []
for i in range(1, len(stock_data)):
    if stock_data['MA20'][i] > stock_data['MA50'][i] and stock_data['MA20'][i - 1] <= stock_data['MA50'][i - 1]:
        buy_signals.append(stock_data.index[i])
    elif stock_data['MA20'][i] < stock_data['MA50'][i] and stock_data['MA20'][i - 1] >= stock_data['MA50'][i - 1]:
        sell_signals.append(stock_data.index[i])

# Visualize buy and sell signals
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'], label='Closing Price')
plt.plot(stock_data['MA20'], label='MA20')
plt.plot(stock_data['MA50'], label='MA50')
plt.scatter(buy_signals, stock_data.loc[buy_signals]['Close'], marker='^', color='green', label='Buy Signal')
plt.scatter(sell_signals, stock_data.loc[sell_signals]['Close'], marker='v', color='red', label='Sell Signal')
plt.title(f'Stock Price of {stock_symbol} ({datetime.strptime(start_date, "%Y-%m-%d").strftime("%b %Y")}-{datetime.strptime(end_date, "%Y-%m-%d").strftime("%b %Y")}) with Buy/Sell Signals')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()      