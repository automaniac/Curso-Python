import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('500x500')


text = tk.Text(master=window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text = 'Um botão')
button.pack()


entry.bind('<FocusIn>', lambda event: print('Entrou'))
entry.bind('<FocusOut>', lambda event: print('Saiu'))

# window.bind('<Motion>', lambda evento: print(evento))
button.bind('<Alt-KeyPress-a>', lambda evento: print(evento))


window.mainloop()