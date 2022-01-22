import yfinance as yf
from datetime import datetime

# Criar uma função para obter o dado do dia
def getLast(stock: str):
    value = stock.upper()
    data = yf.download(tickers=value, period="1d", interval="1d")
    return data["Close"][0]


print(getLast("AAPL"))
