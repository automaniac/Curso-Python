import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("800x800")

canvas = tk.Canvas(master=window, bg='white')

canvas.pack()


# canvas.create_rectangle((50, 20, 100, 200), fill='red', outline='green', width=10)
# canvas.create_oval((100, 100, 200, 200), fill='yellow')
# canvas.create_line((300, 0, 320, 50), fill='blue', width=1)
# canvas.create_window(
#     (200,200), 
#     window = ttk.Button(window,
#                         text='Botao', 
#                         command=lambda:print('Botao pressionado')
#                 )
#             )

tamanho = 10

def desenhar(evento):
    posx = evento.x
    posy = evento.y
    print(evento)
    canvas.create_oval((posx - tamanho, posy - tamanho, posx + tamanho, posy + tamanho), fill='black')

canvas.bind('<B1-Motion>', desenhar)
window.mainloop()