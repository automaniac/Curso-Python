import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("800x800")


variavel_escala = tk.DoubleVar(value=15)
escala = ttk.Scale(master=window,
                   from_=0, 
                   to=100, 
                   length = 100, 
                   orient='vertical', 
                   variable = variavel_escala)
escala.pack()

barra_de_progresso = ttk.Progressbar(window,  
                                     length = 100, 
                                     mode = 'indeterminate',
                                     variable=variavel_escala
                                     )
barra_de_progresso.pack()

# barra_de_progresso.start(100)

window.mainloop()