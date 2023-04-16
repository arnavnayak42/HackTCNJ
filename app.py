"""
@author: Arjun Ravikumar, Ethen Chou, Arnav Nayak, Kevin Yarramsetty
Sunday, 1:17 AM, 4-16-23
Analyze Historical Stock Trends and use this information to model potential future changes in stock valuation

"""


import yfinance as yf
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import pandas as pd
from datetime import *
from sklearn.linear_model import LinearRegression


# Pull data from Yahoo Finance
stock_symbol = input("Enter The Stock Abriviation: ")
start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
end_date = datetime.now().strftime('%Y-%m-%d')
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Calculate 20-day Moving Average
stock_data['MA20'] = stock_data['Close'].rolling(window=20).mean()

# Calculate 50-day Moving Average
stock_data['MA50'] = stock_data['Close'].rolling(window=50).mean()

# Linear regression model 
X = pd.DataFrame(range(len(stock_data)))
y = stock_data['Close']
model = LinearRegression().fit(X, y)

# Using Linear Regression Model to predict future stock prices
future_dates = pd.date_range(end_date, periods=30)
future_X = pd.DataFrame(range(len(stock_data), len(stock_data) + 30))
future_y = model.predict(future_X)

# Find buy and sell signals based on Moving Averages
buy_signals = []
sell_signals = []
for i in range(1, len(stock_data)):
    if stock_data['MA20'][i] > stock_data['MA50'][i] and stock_data['MA20'][i - 1] <= stock_data['MA50'][i - 1]:
        buy_signals.append(stock_data.index[i])
    elif stock_data['MA20'][i] < stock_data['MA50'][i] and stock_data['MA20'][i - 1] >= stock_data['MA50'][i - 1]:
        sell_signals.append(stock_data.index[i])

# Plot the stock data with buy/sell signals and predicted prices
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'], label='Closing Price')
plt.plot(stock_data['MA20'], label='MA20')
plt.plot(stock_data['MA50'], label='MA50')
plt.scatter(buy_signals, stock_data.loc[buy_signals]['Close'], marker='^', color='green', label='Buy Signal')
plt.scatter(sell_signals, stock_data.loc[sell_signals]['Close'], marker='v', color='red', label='Sell Signal')
plt.plot(future_dates, future_y, label='Predicted Price')


#Graph Details 
plt.title(f'Stock Price of {stock_symbol} ({datetime.strptime(start_date, "%Y-%m-%d").strftime("%b %Y")}-{datetime.strptime(end_date, "%Y-%m-%d").strftime("%b %Y")}) with Buy/Sell Signals and Predicted Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()


# Plotly Graph (GUI)
fig = go.Figure()
fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], name='Closing Price'))
fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['MA20'], name='MA20'))
fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['MA50'], name='MA50'))
fig.add_trace(go.Scatter(x=buy_signals, y=stock_data.loc[buy_signals]['Close'], mode='markers', marker=dict(symbol='triangle-up', color='green'), name='Buy Signal'))
fig.add_trace(go.Scatter(x=sell_signals, y=stock_data.loc[sell_signals]['Close'], mode='markers', marker=dict(symbol='triangle-down', color='red'), name='Sell Signal'))
fig.add_trace(go.Scatter(x=future_dates, y=future_y, mode='lines', name='Predicted Price'))

#Update and Display Graph 
fig.update_layout(title=f'Stock Price of {stock_symbol} ({datetime.strptime(start_date, "%Y-%m-%d").strftime("%b %Y")}-{datetime.strptime(end_date, "%Y-%m-%d").strftime("%b %Y")}) with Buy/Sell Signals and Predicted Prices',
                  xaxis_title='Date',
                  yaxis_title='Price (USD)',
                  legend=dict(x=0, y=1, traceorder='normal'))

fig.show()

