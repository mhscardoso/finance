from matplotlib.pyplot import ylabel
import yfinance as yf
import mplfinance as mpf
import pandas as pd


# Criar uma função para obter o dado do dia
def getLast(stock: str):
    value = stock.upper()
    try:
        data = yf.download(tickers=value, period="1h", interval="1d")
    except:
        return "NaN"
    return data["Close"][0]


def getMany(stock: str, code: int = None):
    """
        stock: codigo da acao
        code: opcao (1 - [period = 1mo, interval = 1d];
                     2 - [period = 2d , interval = 1h];
                     3 - [period = 1d , interval = 5m]
    """
    
    if code not in [1, 2, 3]:
        return
    
    tipo = []

    if code == 1:
        tipo.append("1mo")
        tipo.append("1d")
    elif code == 2:
        tipo.append("1wk")
        tipo.append("1h")
    else:
        tipo.append("1d")
        tipo.append("5m")

    value = stock.upper()
    try:
        data = yf.download(tickers=value, period=tipo[0], interval=tipo[1])
    except:
        return
    return data[["Open", "High", "Low", "Close", "Volume"]]


def generateGraph(stock, tipo):
    data = getMany(stock, tipo)

    if tipo == 1:
        info = "Um mês - Gráfico Diário"
    elif tipo == 2:
        info = "2 dias - Gráfico de uma hora"
    else:
        info = "1 dia - Gráfico de 5 min."

    return mpf.plot(data, type=f"candle", style="charles", title=f"{stock.upper()} - {info}", ylabel="Preço", ylabel_lower="Shares Traded", volume=True, returnfig=True)



