import tkinter as tk
from tkinter import ttk
import random

first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

window = tk.Tk()
window.geometry("800x800")

tabela = ttk.Treeview(window, columns=('nome', 'sobrenome', 'email'), show='headings')
tabela.heading('nome', text = 'Nome')
tabela.heading('sobrenome', text = 'Sobrenome')
tabela.heading('email', text = 'Email')

tabela.pack(fill='both', expand=True)

for i in range(100):
    nome = random.choice(first_names)
    sobrenome = random.choice(last_names)
    email = nome + '.' + sobrenome + '@gmail.com'
    tabela.insert(parent='', index=0, values=(nome, sobrenome, email))


tabela.bind('<<TreeviewSelect>>', lambda evento: print(tabela.selection()))
def deletar(evento):
    for i in tabela.selection():
        tabela.delete(i)
tabela.bind('<Delete>', deletar)

def modificar(evento):
    for i in tabela.selection():
        tabela.item(i, values=('A', 'B', 'C'))
tabela.bind('a', modificar)


window.mainloop()