import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Variaveis do tkinter')
window.geometry("800x800")

variavel_string = tk.StringVar(value='valor_inicial')

label_titulo = ttk.Label(master = window, text = 'Titulo', textvariable=variavel_string)
label_titulo.pack()



entrada = ttk.Entry(master = window, textvariable=variavel_string)
entrada.pack()

window.mainloop()