# from momento import Momento as mo

# year = mo.anoja()
# month = mo.mesja()

# print(f"{year}/{month}NB-HE160")
from tkinter import *
from tkinter import ttk

class Janela:
    def __init__(self, janin):
        # self.janela = ttk.Frame(janin, padding=10)
        self.frm = ttk.Frame(janin, padding=10)
        self.grade = self.frm.grid()
        # self.titulo = ttk.Label(self.frm, text="Olha a bagunça...").grid(column=2, row=1)
        self.nome = ttk.Entry(self.frm,  text="Your name",).grid(column=2, row=2)
        self.chave = ttk.Entry(self.frm,  text="Your Key",).grid(column=2, row=3)
        self.bfim = ttk.Button(self.frm, text="Quit", command=janin.destroy).grid(column=2, row=4)


#     def findar():
        
#     # def limpar():



janin = Tk()

Janela(janin)

janin.mainloop()
