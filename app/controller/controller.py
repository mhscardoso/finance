import yfinance as yf
from datetime import datetime

# Criar uma função para obter o dado do dia
def getLast(stock: str):
    value = stock.upper()
    try:
        data = yf.download(tickers=value, period="1h", interval="1d")
    except:
        return "NaN"
    return data["Close"][0]

