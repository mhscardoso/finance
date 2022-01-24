from tkinter import *
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from models.model import Banco

db = Banco()

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