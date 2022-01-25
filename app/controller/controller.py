import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates

# Criar uma função para obter o dado do dia
def getLast(stock: str):
    value = stock.upper()
    try:
        data = yf.download(tickers=value, period="1h", interval="1d")
    except:
        return "NaN"
    return data["Close"][0]


def getMany(stock: str, code: int = None):
    """stock: codigo da acao
        code: opcao (1 - """
    
    value = stock.upper()
    try:
        data = yf.download(tickers=value, period="15d", interval="1d")
    except:
        return
    return data
