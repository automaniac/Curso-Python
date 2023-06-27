import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Grid')
window.geometry('600x400')

# widgets 
label_vermelho = ttk.Label(window, text = 'Vermelho', background = 'red')
label_azul = ttk.Label(window, text = 'Azul', background = 'blue')
label_verde = ttk.Label(window, text = 'Verde', background = 'green')
label_amarelo = ttk.Label(window, text = 'Amarelo', background = 'yellow')
button_cima = ttk.Button(window, text = 'Botão cima')
button_meio = ttk.Button(window, text = 'Botão meio')

# definição do grid
window.columnconfigure((0,1,2), weight = 1, uniform = 'a')
window.columnconfigure(3, weight = 2, uniform = 'a')
window.rowconfigure(0, weight = 1, uniform = 'a')
window.rowconfigure(1, weight = 1, uniform = 'a')
window.rowconfigure(2, weight = 1, uniform = 'a')
window.rowconfigure(3, weight = 1, uniform = 'a')

# dispor os widgets
label_vermelho.grid(row = 0, column = 0, sticky = 'nsew')
label_azul.grid(row = 1, column = 1, rowspan = 3, sticky = 'nsew')
label_verde.grid(row = 1, column = 0, columnspan = 3, sticky = 'nsew', padx = 20, pady = 10)
label_amarelo.grid(row = 3, column = 3, sticky = 'se')

# exercise 
# add the buttons and the entry field
button_cima.grid(row = 0, column = 3, sticky = 'nesw')
button_meio.grid(row = 2, column = 2, sticky = 'nesw')


# run
window.mainloop()