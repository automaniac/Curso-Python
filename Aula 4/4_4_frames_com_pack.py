import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack parenting')
window.geometry('400x600')

# Top frame
top_frame = ttk.Frame(window) 
label_vermelho = ttk.Label(top_frame, text = 'Vermelho', background = 'red')
label_azul = ttk.Label(top_frame, text = 'Azul', background = 'blue')

# middle widget
label_verde = ttk.Label(window, text = 'Verde', background = 'green')

# bottom frame
bottom_frame = ttk.Frame(window)
label_laranja = ttk.Label(bottom_frame, text = 'Laranja', background = 'orange')
button_esquerda = ttk.Button(bottom_frame, text = 'Esquerda')
button_direita = ttk.Button(bottom_frame, text = 'Direita')



# top layout 
label_vermelho.pack(side = 'left', fill = 'both', expand = True)
label_azul.pack(side = 'left', fill = 'both', expand = True)
top_frame.pack(fill = 'both', expand = True)

# middle layout
label_verde.pack(expand = True)

# bottom layout
button_esquerda.pack(side = 'left', expand = True, fill = 'both')
label_laranja.pack(side = 'left', expand = True, fill = 'both')
button_direita.pack(side = 'left', expand = True, fill = 'both')
bottom_frame.pack(expand = True, fill = 'both', padx = 20, pady = 20)



# run
window.mainloop()