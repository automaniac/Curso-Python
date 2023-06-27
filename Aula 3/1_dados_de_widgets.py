import tkinter as tk
from tkinter import ttk

def enviar():
    texto = entrada.get()
    print(texto)
    label_titulo['text'] = texto
    entrada['state'] = 'disabled'


def editar(texto):
    entrada['state'] = 'normal'
    print(texto)
    # entrada['text'] = texto



window = tk.Tk()
window.geometry("800x800")
label_titulo = ttk.Label(master = window, text = 'Titulo')
label_titulo.pack()

entrada = ttk.Entry(master = window)
entrada.pack()

botao_enviar = ttk.Button(master=window, text="Enviar", command= enviar)
botao_enviar.pack()

botao_editar = ttk.Button(master=window, text="Editar", command= lambda:editar('asdasd'))
botao_editar.pack()


window.mainloop()