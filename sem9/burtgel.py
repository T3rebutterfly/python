import tkinter as tk
from tkinter import *
from tkinter import ttk
from random import choice

window = tk.Tk()
window.title('Бүртгэлийн програм')

# menu start
menubar = Menu(window)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label = 'Бүртгэх')
filemenu.add_command(label = 'Нэвтрэх')
filemenu.add_command(label = 'Засварлах')
filemenu.add_command(label = 'Устгах')
filemenu.add_separator()
filemenu.add_command(label = 'Гарах', command = window.quit)
menubar.add_cascade(label = 'Цэс', menu = filemenu)

window.config(menu = menubar)

# data
Ovog = ['Bat',]
Ner = ['Bold',]
Nas = ['26']
Utas = ['99455623']

# treeview
table = ttk.Treeview(window, columns = ('Овог', 'Нэр', 'Нас', 'Утас'), show = 'headings')
table.heading('Овог', text = 'Овог')
table.heading('Нэр', text = 'Нэр')
table.heading('Нас', text = 'Нас')
table.heading('Утас', text = 'Утас')
table.pack()

for i in range(4):
    Овог = choice(Ovog)
    Нэр = choice(Ner)
    Нас = choice(Nas)
    Утас = choice(Utas)
    data = (Овог, Нэр, Нас, Утас)
    table.insert(parent = '', index = 0, values = data)
#run    
window.mainloop()