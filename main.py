import numpy as np
import pandas as pd
import csv

#Data Source
import yfinance as yf

#Data Collection
ticker = ''
ticker = input("Enter")
#tickers
data = yf.download(tickers=ticker, period='1D', interval='1m')
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified
  print(data)