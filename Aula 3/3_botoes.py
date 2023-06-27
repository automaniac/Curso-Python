import tkinter as tk
from tkinter import ttk

def botao_pressionado():
    check_var.set(5)


window = tk.Tk()
window.geometry("800x800")



botao_simples = ttk.Button(
    master=window, 
    text="Botao simples", 
    command= botao_pressionado
)
botao_simples.pack()

check_var = tk.IntVar(value=10)

botao_check = ttk.Checkbutton(
    master=window, 
    text='meu_checkbutton', 
    onvalue= 10, 
    offvalue=5, 
    variable=check_var,
    command= lambda:print(check_var.get())
)
botao_check.pack()


variavel_radio = tk.IntVar(value=1)

radio_button = ttk.Radiobutton(
    master=window, 
    text='rb 1', 
    value = 1,  
    variable=variavel_radio
)
radio_button.pack()

radio_button2 = ttk.Radiobutton(
    master=window, 
    text='rb 2', 
    value = 2,  
    variable=variavel_radio
)
radio_button2.pack()

window.mainloop()