from tkinter import *
from tkinter import ttk
from matplotlib import container
from model import Banco
from controller import *

db = Banco()

# Aqui vai ficar a interface do usuário
class App:
    
    def __init__(self, master=None, username=None):
        self.master = master
        self.master.title("Finance")

        # Containers para os elementos

        # Container para dizer olah
        self.container1 = Frame(self.master)
        self.container1["pady"] = 10
        self.container1.pack()

        # Container para texto
        self.container2 = Frame(self.master)
        self.container2["pady"] = 10
        self.container2.pack()

        # Container para o preco
        self.container3 = Frame(self.master)
        self.container3["pady"] = 10
        self.container3.pack()

        # Parte de compra
        self.container4 = Frame(self.master)
        self.container4["pady"] = 10
        self.container4.pack()

        # Info. do usuario
        self.user = db.procuraUsername(username)[0]
        self.user_id = self.user[0]
        self.cash = self.user[3]

        # Mensagem de olah
        self.hello = Label(self.container1, text=f"Olá, {username}")
        self.hello.pack(side=LEFT)

        self.l_cash = Label(self.container1, text="{:.2f}".format(self.cash))
        self.l_cash.pack()

        # Campo de entrada da stock
        self.quote = Entry(self.container2)
        self.quote["width"] = 15
        self.quote.pack(side=LEFT)

        def search():
            quote = self.quote.get()
            last = getLast(quote)
            self.msg["text"] = "Ultimo preco: US$ {:.2f}".format(last)

        self.search = Button(self.container2, text="Procurar", command=search)
        self.search.pack()

        # Mensagem de preco
        self.msg = Label(self.container3, text="")
        self.msg.pack()

        # Entry de quantidade de acoes
        self.quotes = Entry(self.container4)
        self.quotes["width"] = 15
        self.quotes.pack(side=LEFT)

        def buy():
            price = getLast(self.quote.get())
            try:
                self.quotes = int(self.quotes.get())
            except:
                return "Error"
            
            total_value = price * self.quotes
            if self.cash < total_value:
                return "Not enough"
            else:
                self.cash -= total_value
                self.l_cash["text"] = "{:.2f}".format(self.cash)

        self.buy = Button(self.container4, text="Comprar", command=buy)
        self.buy.pack()


class Login:

    def __init__(self, master=None):

        self.master = master
        self.master.title("Finance")

        # Containers para os elementos
        self.container1 = Frame(self.master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(self.master)
        self.container2["padx"] = 20
        self.container2.pack()

        self.container3 = Frame(self.master)
        self.container3["padx"] = 20
        self.container3.pack()

        self.container4 = Frame(self.master)
        self.container4["pady"] = 10
        self.container4.pack()

        self.container5 = Frame(self.master)
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(self.master)
        self.container6["pady"] = 5
        self.container6.pack()

        # Titulo no topo
        self.title = Label(self.container1, text="Finance Login")
        self.title.pack()

        # Guia de usuario
        self.l_user = Label(self.container2, text="Username ")
        self.l_user.pack(side=LEFT)

        self.user = Entry(self.container2)
        self.user["width"] = 30
        self.user.pack()

        # Guia de senha
        self.l_pass = Label(self.container3, text="Senha ")
        self.l_pass["padx"] = 14
        self.l_pass.pack(side=LEFT)

        self.passw = Entry(self.container3)
        self.passw["width"] = 30
        self.passw["show"] = "*"
        self.passw.pack()

        # Botao de login
        self.login = Button(self.container4, text="Login", command=self.login)
        self.login.pack()

        # Botao de registro
        self.registro = Button(self.container5, text="Registre-se", command=self.registrar)
        self.registro.pack()

        # Mensagem de resposta
        self.resposta = Label(self.container6, text="")
        self.resposta.pack()
    
    def login(self):
        if db.confereDados(self.user.get(), self.passw.get()):
            self.resposta["text"] = "Aprovado"
            username = db.procuraUsername(self.user.get())[0][1]
            self.master.destroy()
            root = Tk()
            App(root, username)
            root.mainloop()

        else:
            self.resposta["text"] = "Usuario ou senha invalidos"
            
    def registrar(self):
        self.master.destroy()
        root = Tk()
        Register(root)
        root.mainloop()


class Register:

    def __init__(self, master=None):
        self.master = master
        self.master.title("Finance")

        # Containers para os elementos
        self.container1 = Frame(self.master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(self.master)
        self.container2["padx"] = 20
        self.container2.pack()

        self.container3 = Frame(self.master)
        self.container3["padx"] = 20
        self.container3.pack()

        self.container4 = Frame(self.master)
        self.container4["pady"] = 10
        self.container4.pack()

        self.container5 = Frame(self.master)
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(self.master)
        self.container6["pady"] = 5
        self.container6.pack()

        # Titulo no topo
        self.title = Label(self.container1, text="Finance Registro")
        self.title.pack()

        # Guia de usuario
        self.l_user = Label(self.container2, text="Username ")
        self.l_user.pack(side=LEFT)

        self.user = Entry(self.container2)
        self.user["width"] = 30
        self.user.pack()

        # Guia de senha
        self.l_pass = Label(self.container3, text="Senha ")
        self.l_pass["padx"] = 14
        self.l_pass.pack(side=LEFT)

        self.passw = Entry(self.container3)
        self.passw["width"] = 30
        self.passw["show"] = "*"
        self.passw.pack()

        # Botao de registro
        self.login = Button(self.container4, text="Registre-se", command=self.registrar)
        self.login.pack()

        # Botao de voltar ao login
        self.registro = Button(self.container5, text="Retornar ao Login", command=self.retornaLogin)
        self.registro.pack()

        # Mensagem de resposta
        self.resposta = Label(self.container6, text="")
        self.resposta.pack()
    
    def registrar(self):
        self.resposta["text"] = db.insereUsuario(self.user.get(), self.passw.get())
        if self.resposta["text"] == "Usuario cadastrado com sucesso":
            self.retornaLogin()
    
    def retornaLogin(self):
        self.master.destroy()
        root = Tk()
        Login(root)
        root.mainloop()


root = Tk()
Login(root)
root.mainloop()
