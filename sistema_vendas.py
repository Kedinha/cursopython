#Desenvolvimento de interfaces graficas
#PYTHON 3.4
#CODING: utf8
from tkinter import*
import random
import time;
import datetime


root = Tk()
Tops = Frame (root, width=350, height=100, bd=3, relief="raise")
Tops.pack(side=TOP)
Label(root, text="Fala Galera!").pack()
Button (root, text="Enviar").pack()
root.geometry("350x350+0+0")
root.title("SISTEMA DE VENDAS")
root.configure(background='blue')



root.mainloop()
