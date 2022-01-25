from tkinter import *

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from models.model import Banco

from views.register import Register
from views.application import App

db = Banco()

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
            user_db = db.procuraUsername(self.user.get())
            username = user_db[0][1]
            self.master.destroy()
            root = Tk()
            App(root, username)
            root.mainloop()

        else:
            self.resposta["text"] = "Usuario ou senha invalidos"
            
    def registrar(self):
        root = Tk()
        Register(root)
        root.mainloop()
