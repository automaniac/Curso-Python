import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Frames')

frame = ttk.Frame(window, width=200, height=200, borderwidth=10, relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side='left')

label_frame = ttk.Label(frame, text='Label no frame')
label_frame.pack()

button_frame = ttk.Button(frame, text='Botão no frame')
button_frame.pack()

label_fora = ttk.Label(window, text='Label fora do frame')
label_fora.pack(side='left')

window.mainloop()
