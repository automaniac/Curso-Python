import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("800x800")

itens = ['python', 'javascript', 'c']


combo_var = tk.StringVar(value='python')
combo = ttk.Combobox(window, textvariable=combo_var, values=itens)
combo.pack()


combo.bind('<<ComboboxSelected>>', lambda evento: print(combo_var.get()))


spin_var = tk.IntVar(value=5)
spin = ttk.Spinbox(window, from_ = 3, to=10, increment=1, textvariable=spin_var)
spin.pack()

spin.bind('<<Increment>>', lambda evento: print('subindo'))
spin.bind('<<Decrement>>', lambda evento: print('descendo'))


valores = ['A', 'B', 'C', 'D']
spin_var2 = tk.StringVar(value='A')
spin2 = ttk.Spinbox(window, textvariable=spin_var2, values=valores)
spin2.pack()


window.mainloop()