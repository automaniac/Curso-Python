import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Place')
window.geometry('400x600')

# widgets 
label_vermelha = ttk.Label(window, text = 'Vermelho', background = 'red')
label_azul = ttk.Label(window, text = 'Azul', background = 'blue')
label_verde = ttk.Label(window, text = 'Verde', background = 'green')
button = ttk.Button(window, text = 'Botão')

# layout 

label_azul.lift(aboveThis = label_verde)

label_vermelha.place(x = 300, y = 100, width = 100, height = 200)
label_azul.place(relx = 0.2, rely = 0.1, relwidth = 0.4, relheight = 0.5)
label_verde.place(x = 80, y = 100, width = 160, height = 300)
button.place(relx = 1, rely = 1, anchor = 'se')

# frame 
frame = ttk.Frame(window)
frame_label_amarela = ttk.Label(frame, text = 'Frame amarelo', background = 'yellow')
frame_button = ttk.Button(frame, text = 'Botão do frame')

# frame layout
frame.place(relx = 0, rely = 0, relwidth = 0.3, relheight = 1)
frame_label_amarela.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.5)
frame_button.place(relx = 0, rely = 0.5, relwidth = 1, relheight = 0.5)


# run
window.mainloop()