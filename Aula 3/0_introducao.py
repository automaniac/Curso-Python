import tkinter as tk
from tkinter import ttk

def botao_clicado():
    print('Cliquei')

window = tk.Tk()
window.geometry("800x800")

label = ttk.Label(master=window, text='Esse é meu texto')
label.pack()

text = tk.Text(master=window)
text.pack()

entry = ttk.Entry(master=window)
entry.pack()

botao = ttk.Button(master=window, text='Botao', command=botao_clicado)
botao.pack()

window.mainloop()

