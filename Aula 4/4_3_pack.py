import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Pack')
window.geometry('400x600')

label_vermelho = ttk.Label(window, text='Vermelho', background='red')
label_azul = ttk.Label(window, text='Azul', background='blue')
label_verde = ttk.Label(window, text='Verde', background='green')
button = ttk.Button(window, text='Botão')

label_vermelho.pack(side='top', expand=True, fill='both', padx=10, pady=10)
label_azul.pack(side='left', expand=True, fill='both')
label_verde.pack(side='top', expand=True, fill='both')
button.pack(side='top', expand=True, fill='both')

window.mainloop()
