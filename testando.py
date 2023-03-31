# from momento import Momento as mo

# year = mo.anoja()
# month = mo.mesja()

# print(f"{year}/{month}NB-HE160")
from tkinter import *
from tkinter import ttk
# import getpass

class Janela:
    def __init__(self):
        # self.janela = ttk.Frame(janin, padding=10)
        self.tk = Tk()
        self.frm0 = ttk.Frame(self.tk, padding=10)
        self.grade = self.frm.grid()
        # self.titulo = ttk.Label(self.frm, text="Olha a bagunça...").grid(column=2, row=1)
        self.nome = ttk.Entry(self.frm0, text="Your name").grid(column=2, row=2)
        self.chave = ttk.Entry(self.frm0, text="Your Key", show="*").grid(column=2, row=3)
        self.bfim = ttk.Button(self.frm0, text="Quit", command=self.bclicked_fim).grid(column=2, row=4)
        self.bok = ttk.Button(self.frm0, text="OK", command=self.bclicked_logar).grid(column=1, row=4)
        mainloop()

    def bclicked_fim(self):
        self.frm.quit()
        
    def bclicked_logar(self):
        return self.nome, self.chave

    def opera(self):
        self.nick = self.nome
        
        self.frm = ttk.Frame(self.tk, padding=10)
        self.grade1 = self.frm1.grid()


Janela()
ok = Janela.bclicked_logar
if ok != None:
    Janela.opera
else:
    print("Encerrado por falta de usuário.")
    Janela.bclicked_fim

# mainloop()
