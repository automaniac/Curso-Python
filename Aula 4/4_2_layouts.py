import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400')

# widgets 
label_vermelha = ttk.Label(window, text = 'Vermelho', background = 'red')
label_azul = ttk.Label(window, text = 'Azul', background = 'blue')

# pack
label_vermelha.pack(side = 'left', expand = True, fill = 'y')
label_azul.pack(side = 'left', expand = True, fill = 'both')

# grid 
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.columnconfigure(2, weight = 2)
window.columnconfigure((0,1,2), weight = 1)
window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)

label_vermelha.grid(row = 0, column = 1, sticky = 'nsew')
label_azul.grid(row = 1, column = 1, columnspan = 2, sticky = 'nsew')

# place
label_vermelha.place(x = 100 , y = 200, width = 200, height = 100)
label_azul.place(relx = 0.5, rely = 0.5, relwidth = 1, anchor = 'se')

# run
window.mainloop()