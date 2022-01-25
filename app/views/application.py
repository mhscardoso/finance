from tkinter import *
from tkinter import ttk
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from models.model import Banco

db = Banco()

from controller.controller import *

# Aqui vai ficar a interface do usuário
class App:
    
    def __init__(self, master=None, username=None):
        self.master = master
        self.master.geometry("750x500")
        self.master.title("Finance")
        self.username = username

        self.abas = ttk.Notebook(self.master)
        self.abas.place(x = 0, y = 0, width = 750, height = 500)

        self.font_table_head = "Helvetica 15 bold"

        # Apenas trazendo os dados do usuario
        self.user = db.procuraUsername(self.username)[0]
        self.user_id = self.user[0]
        self.user_cash = self.user[3]

        # Cada aba do app
        self.frame_start = Frame(self.abas)

        self.frame_history = Frame(self.abas)

        self.frame_search = Frame(self.abas)

        self.frame_buy = Frame(self.abas)

        self.frame_sell = Frame(self.abas)

        self.frame_graph = Frame(self.abas)

        self.abas.add(self.frame_start, text="Inicio")
        self.abas.add(self.frame_history, text="Historico")
        self.abas.add(self.frame_search, text="Procura")
        self.abas.add(self.frame_buy, text="Compra")
        self.abas.add(self.frame_sell, text="Venda")
        self.abas.add(self.frame_graph, text="Grafico")

        self.abas.pack(expand=1, fill="both")

        # Tela de inicio -------------------------------------------------------------
        # Barra de topo
        self.barra_top1 = Frame(self.frame_start)
        self.barra_top1["pady"] = 10
        self.barra_top1["bg"] = "white"
        self.barra_top1.pack(fill="x")

        self.user1 = Label(self.barra_top1, text="Ola, {}".format(self.username))
        self.user1["padx"] = 150
        self.user1["bg"] = "white"
        self.user1.pack(side=LEFT)

        self.cash1 = Label(self.barra_top1, text="US$ {:.2f}".format(self.user_cash))
        self.cash1["padx"] = 150
        self.cash1["bg"] = "white"
        self.cash1.pack(side=RIGHT)

        # Tabela de pertences            
        self.table1 = Frame(self.frame_start, width=600)
        self.table1["pady"] = 20
        self.table1.pack()

        # Cabecalho da tabela
        table_items = ["Stock", "Shares", "Preco", "Total"]

        for item in table_items:
            c1 = Label(self.table1, text = item, font = self.font_table_head)
            c1["padx"] = 40
            c1["pady"] = 10
            c1.grid(row = 0, column = table_items.index(item))
        
        self.mostraPertences()


        # ----------------------------------------------------------------------------


        # Tela de Historico ----------------------------------------------------------
        # Barra de topo
        self.barra_top2 = Frame(self.frame_history)
        self.barra_top2["pady"] = 10
        self.barra_top2["bg"] = "white"
        self.barra_top2.pack(fill="x")

        self.user2 = Label(self.barra_top2, text="Ola, {}".format(self.username))
        self.user2["padx"] = 150
        self.user2["bg"] = "white"
        self.user2.pack(side=LEFT)

        self.cash2 = Label(self.barra_top2, text="US$ {:.2f}".format(self.user_cash))
        self.cash2["padx"] = 150
        self.cash2["bg"] = "white"
        self.cash2.pack(side=RIGHT)

        # Cabecalho da tabela          
        self.table2 = Frame(self.frame_history, width=600)
        self.table2["pady"] = 20
        self.table2.pack()

        # Cabecalho da tabela
        table_items2 = ["Stock", "Preco", "Shares", "Operacao"]

        for item in table_items2:
            c1 = Label(self.table2, text = item, font = self.font_table_head)
            c1["padx"] = 40
            c1["pady"] = 10
            c1.grid(row = 0, column = table_items2.index(item))

        self.show_history()        
        # ----------------------------------------------------------------------------


        # Tela de Procura ------------------------------------------------------------
        # Barra de topo
        self.barra_top3 = Frame(self.frame_search)
        self.barra_top3["pady"] = 10
        self.barra_top3["bg"] = "white"
        self.barra_top3.pack(fill="x")

        self.user3 = Label(self.barra_top3, text="Ola, {}".format(self.username))
        self.user3["padx"] = 150
        self.user3["bg"] = "white"
        self.user3.pack(side=LEFT)

        self.cash3 = Label(self.barra_top3, text="US$ {:.2f}".format(self.user_cash))
        self.cash3["padx"] = 150
        self.cash3["bg"] = "white"
        self.cash3.pack(side=RIGHT)

        # Formulario para pesquisa
        self.form1 = Frame(self.frame_search)
        self.form1["pady"] = 20
        self.form1.pack()

        self.msg_info = Label(self.form1, text="Digite o codigo da acao: ")
        self.msg_info.grid(row = 0, column = 0)

        self.search_entry = Entry(self.form1)
        self.search_entry["width"] = 15
        self.search_entry.grid(row = 0, column = 1)

        self.search_button = Button(self.form1, text="Procurar", command=self.search)
        self.search_button.grid(row = 0, column = 2)

        # Informacao pesquisada
        self.info = Label(self.form1, text = "")
        self.info["pady"] = 20
        self.info.grid(row = 1, column = 0, rowspan = 2)

        # ----------------------------------------------------------------------------

        # Tela de Compra -------------------------------------------------------------
        # Barra de topo
        self.barra_top4 = Frame(self.frame_buy)
        self.barra_top4["pady"] = 10
        self.barra_top4["bg"] = "white"
        self.barra_top4.pack(fill="x")

        self.user4 = Label(self.barra_top4, text="Ola, {}".format(self.username))
        self.user4["padx"] = 150
        self.user4["bg"] = "white"
        self.user4.pack(side=LEFT)

        self.cash4 = Label(self.barra_top4, text="US$ {:.2f}".format(self.user_cash))
        self.cash4["padx"] = 150
        self.cash4["bg"] = "white"
        self.cash4.pack(side=RIGHT)

        # Formulario para compra
        self.form2 = Frame(self.frame_buy)
        self.form2["pady"] = 20
        self.form2.pack()

        self.msg_info_compra = Label(self.form2, text="Digite o codigo da acao: ")
        self.msg_info_compra["pady"] = 10
        self.msg_info_compra.grid(row = 0, column = 0)

        self.buy_entry = Entry(self.form2)
        self.buy_entry["width"] = 15
        self.buy_entry.grid(row = 0, column = 1)

        self.msg_info_quotes = Label(self.form2, text="Digite quantas acoes: ")
        self.msg_info_quotes["pady"] = 10
        self.msg_info_quotes.grid(row = 1, column = 0)

        self.quotes_entry = Entry(self.form2)
        self.quotes_entry["width"] = 15
        self.quotes_entry.grid(row = 1, column = 1)

        self.buy_button = Button(self.form2, text="Comprar", command=self.buy)
        self.buy_button.grid(row = 3, column = 1, rowspan=3)

        # Informacao de compra
        self.info_buy = Label(self.form2, text = "")
        self.info_buy["pady"] = 20
        self.info_buy.grid(row = 4, column = 0, rowspan = 2)
        # ---------------------------------------------------------------------------


        # Tela de Venda -------------------------------------------------------------
        # Barra de topo
        self.barra_top5 = Frame(self.frame_sell)
        self.barra_top5["pady"] = 10
        self.barra_top5["bg"] = "white"
        self.barra_top5.pack(fill="x")

        self.user5 = Label(self.barra_top5, text="Ola, {}".format(self.username))
        self.user5["padx"] = 150
        self.user5["bg"] = "white"
        self.user5.pack(side=LEFT)

        self.cash5 = Label(self.barra_top5, text="US$ {:.2f}".format(self.user_cash))
        self.cash5["padx"] = 150
        self.cash5["bg"] = "white"
        self.cash5.pack(side=RIGHT)

        # Formulario para venda
        self.form3 = Frame(self.frame_sell)
        self.form3["pady"] = 20
        self.form3.pack()

        self.msg_info_venda = Label(self.form3, text="Digite o codigo da acao: ")
        self.msg_info_venda["pady"] = 10
        self.msg_info_venda.grid(row = 0, column = 0)

        self.sell_entry = Entry(self.form3)
        self.sell_entry["width"] = 15
        self.sell_entry.grid(row = 0, column = 1)

        self.msg_info_quotes_sell = Label(self.form3, text="Digite quantas acoes: ")
        self.msg_info_quotes_sell["pady"] = 10
        self.msg_info_quotes_sell.grid(row = 1, column = 0)

        self.quotes_sell_entry = Entry(self.form3)
        self.quotes_sell_entry["width"] = 15
        self.quotes_sell_entry.grid(row = 1, column = 1)

        self.sell_button = Button(self.form3, text="Vender", command=self.sell)
        self.sell_button.grid(row = 3, column = 1, rowspan=3)

        # Informacao de venda
        self.info_sell = Label(self.form3, text = "")
        self.info_sell["pady"] = 20
        self.info_sell.grid(row = 4, column = 0, rowspan = 2)
        # ---------------------------------------------------------------------------


        # Tela do Grafico ------------------------------------------------------------
        # Barra de topo
        self.barra_top6 = Frame(self.frame_graph)
        self.barra_top6["pady"] = 10
        self.barra_top6["bg"] = "white"
        self.barra_top6.pack(fill="x")

        self.user6 = Label(self.barra_top6, text="Ola, {}".format(self.username))
        self.user6["padx"] = 150
        self.user6["bg"] = "white"
        self.user6.pack(side=LEFT)

        self.cash6 = Label(self.barra_top6, text="US$ {:.2f}".format(self.user_cash))
        self.cash6["padx"] = 150
        self.cash6["bg"] = "white"
        self.cash6.pack(side=RIGHT)
        # ---------------------------------------------------------------------------


    # Funcao para procurar a acao
    def search(self):
        quote = self.search_entry.get()
        last = getLast(quote)
        self.info["text"] = "Ultimo preco: US$ {:.2f}".format(last)

    
    # Para comprar uma acao
    def buy(self):
        price = getLast(self.buy_entry.get())
        try:
            quotes = int(self.quotes_entry.get())
        except:
            return "Error"
        
        total_value = price * quotes
        if self.user_cash < total_value:
            self.info_buy["text"] = "Dinheiro insuficiente"
        else:
            self.user_cash -= total_value
            self.atualizaCash(self.user_cash)
            db.buy_model(self.user_id, self.buy_entry.get().upper(), price, quotes, self.user_cash)
            self.info_buy["text"] = "Compra realizada"
        
        self.show_history()
        self.mostraPertences()
    

    # Rapida atualizacao
    def atualizaCash(self, new_cash):
        self.cash1["text"] = "US$ {:.2f}".format(new_cash)
        self.cash2["text"] = "US$ {:.2f}".format(new_cash)
        self.cash3["text"] = "US$ {:.2f}".format(new_cash)
        self.cash4["text"] = "US$ {:.2f}".format(new_cash)
        self.cash5["text"] = "US$ {:.2f}".format(new_cash)
        self.cash6["text"] = "US$ {:.2f}".format(new_cash)

    # Parte visivel da venda    
    def sell(self):
        remain_shares = db.stocks(self.user_id, self.sell_entry.get())
        if remain_shares == 0:
            self.info_sell["text"] = "Impossivel realizar a venda"
            return
        
        try:
            quotes = int(self.quotes_sell_entry.get())
        except:
            self.info_sell["text"] = "O segundo campo deve ser um numero"
            return
        quote = self.sell_entry.get()

        if quotes > remain_shares:
            self.info_sell["text"] = "Impossivel realizar a venda"
            return

        price = getLast(quote)
        total_gain = price * quotes
        self.user_cash += total_gain
        self.atualizaCash(self.user_cash)
        db.sell_model(self.user_id, quote, price, quotes, self.user_cash)
        self.info_sell["text"] = "Venda realizada"

        self.show_history()
        self.mostraPertences()

    
    def show_history(self):
        history = db.get_history(self.user_id)

        history = reversed(history)
        history = list(history)

        for op in history:
            for i in range(1, 5):
                if i == 4:
                    if op[i] == 0:
                        c1 = Label(self.table2, text = "Compra")
                        c1["padx"] = 40
                        c1["pady"] = 5
                        c1.grid(row = history.index(op) + 1, column = i - 1)
                    else:
                        c1 = Label(self.table2, text = "Venda")
                        c1["padx"] = 40
                        c1["pady"] = 5
                        c1.grid(row = history.index(op) + 1, column = i - 1)
                elif i == 2:
                    c1 = Label(self.table2, text = "{:.2f}".format(op[i]))
                    c1["padx"] = 40
                    c1["pady"] = 5
                    c1.grid(row = history.index(op) + 1, column = i - 1)
                
                else:
                    c1 = Label(self.table2, text = op[i])
                    c1["padx"] = 40
                    c1["pady"] = 5
                    c1.grid(row = history.index(op) + 1, column = i - 1)
    

    def mostraPertences(self):
        pertences = db.verPertences(self.user_id)

        pertences = reversed(pertences)
        pertences = list(pertences)
        
        price = 0
        total = 0

        for op in pertences:
            for i in range(1, 5):
                if op[2] != 0:
                    if i < 3:
                        c1 = Label(self.table1, text = op[i])
                        c1["padx"] = 40
                        c1["pady"] = 5
                        c1.grid(row = pertences.index(op) + 1, column = i - 1)
                    elif i == 3:
                        price = getLast(op[1])
                        c1 = Label(self.table1, text = "{:.2f}".format(price))
                        c1["padx"] = 40
                        c1["pady"] = 5
                        c1.grid(row = pertences.index(op) + 1, column = i - 1)
                    elif i == 4:
                        total = price * op[2]
                        c1 = Label(self.table1, text = "{:.2f}".format(total))
                        c1["padx"] = 40
                        c1["pady"] = 5
                        c1.grid(row = pertences.index(op) + 1, column = i - 1)
                else:
                    if i < 3:
                        c1 = Label(self.table1, text = "")
                        c1["padx"] = 40
                        c1["pady"] = 5
                        c1.grid(row = pertences.index(op) + 1, column = i - 1)
                    elif i == 3:
                        price = getLast(op[1])
                        c1 = Label(self.table1, text = "")
                        c1["padx"] = 40
                        c1["pady"] = 5
                        c1.grid(row = pertences.index(op) + 1, column = i - 1)
                    elif i == 4:
                        total = price * op[2]
                        c1 = Label(self.table1, text = "")
                        c1["padx"] = 40
                        c1["pady"] = 5
                        c1.grid(row = pertences.index(op) + 1, column = i - 1)
    



