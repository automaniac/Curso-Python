import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title("Tab Widget")

notebook = ttk.Notebook(window)

frame_processo_1 = ttk.Frame(notebook)
label_processo_1 = ttk.Label(frame_processo_1, text='Titulo 1')
label_processo_1.pack()
button_processo_1 = ttk.Button(frame_processo_1, text='Botao do processo 1')
button_processo_1.pack()

frame_processo_2 = ttk.Frame(notebook)
label_processo_2 = ttk.Label(frame_processo_2, text='Titulo 2')
label_processo_2.pack()
entry_processo_2 = ttk.Entry(frame_processo_2)
entry_processo_2.pack()

notebook.add(frame_processo_1, text='Processo 1')
notebook.add(frame_processo_2, text='Processo 2')
notebook.pack()

window.mainloop()
