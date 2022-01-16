from cgitb import text
from tkinter import *
from turtle import left


class Login():

    def __init__(self, master=None):

        master.title("Finance")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["pady"] = 20
        self.container4.pack()

        self.title = Label(self.container1, text="Finance Login")
        self.title.pack()

        self.l_user = Label(self.container2, text="Username ")
        self.l_user.pack(side=LEFT)

        self.user = Entry(self.container2)
        self.user["width"] = 30
        self.user.pack()

        self.l_pass = Label(self.container3, text="Senha ")
        self.l_pass["padx"] = 14
        self.l_pass.pack(side=LEFT)

        self.passw = Entry(self.container3)
        self.passw["width"] = 30
        self.passw["show"] = "*"
        self.passw.pack()

        self.login = Button()


root = Tk()
Login(root)
root.mainloop()
