import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('App complexo')
window.geometry('600x600')
window.minsize(600,600)

# main layout widgets 
frame_menu = ttk.Frame(window)
frame_conteudo = ttk.Frame(window)

# main place layout 
frame_menu.place(x = 0, y = 0, relwidth = 0.3, relheight = 1)
frame_conteudo.place(relx = 0.3, y = 0, relwidth = 0.7, relheight = 1)

# menu widgets
botao_menu_esquerda = ttk.Button(frame_menu, text = 'Botão esquerda')
botao_menu_direita = ttk.Button(frame_menu, text = 'Botão direita')
botao_menu_baixo = ttk.Button(frame_menu, text = 'Botão baixo')

slider_menu_esquerda = ttk.Scale(frame_menu, orient = 'vertical')
slider_menu_direita = ttk.Scale(frame_menu, orient = 'vertical')

frame_toggle = ttk.Frame(frame_menu)
toggle_menu_esquerda = ttk.Checkbutton(frame_toggle, text = 'Check 1')
toggle_menu_direita = ttk.Checkbutton(frame_toggle, text = 'Check 2')

entry_menu = ttk.Entry(frame_menu)

# menu layout
frame_menu.columnconfigure((0,1,2), weight = 1, uniform = 'a')
frame_menu.rowconfigure((0,1,2,3,4), weight = 1, uniform = 'a')

botao_menu_esquerda.grid(row = 0, column = 0, sticky = 'nswe', columnspan = 2, padx = 4, pady = 4)
botao_menu_direita.grid(row = 0, column = 2, sticky = 'nswe', padx = 4, pady = 4)
botao_menu_baixo.grid(row = 1, column = 0, columnspan = 3, sticky = 'nsew', padx = 4, pady = 4)

slider_menu_esquerda.grid(row = 2, column = 0, rowspan = 2, sticky = 'nsew', pady = 20)
slider_menu_direita.grid(row = 2, column = 2, rowspan = 2, sticky = 'nsew', pady = 20)

# toggle layout
frame_toggle.grid(row = 4, column = 0, columnspan = 3, sticky = 'nsew')
toggle_menu_esquerda.pack(side = 'left', expand = True)
toggle_menu_direita.pack(side = 'left', expand = True)

# entry layout
entry_menu.place(relx = 0.5, rely = 0.95, relwidth = 0.9, anchor = 'center')

# main widgets 
frame_conteudo_vermelho = ttk.Frame(frame_conteudo)
label_conteudo_vermelho = ttk.Label(frame_conteudo_vermelho, text = 'Vermelho', background = 'red')
botao_conteudo_vermelho = ttk.Button(frame_conteudo_vermelho, text = 'Botão conteúdo vermelho')

frame_conteudo_azul = ttk.Frame(frame_conteudo)
label_conteudo_azul = ttk.Label(frame_conteudo_azul, text = 'Azul', background = 'blue')
botao_conteudo_azul = ttk.Button(frame_conteudo_azul, text = 'Botão conteúdo azul')

# main layout
frame_conteudo_vermelho.pack(side = 'left', expand = True, fill = 'both', padx = 20, pady = 20)
frame_conteudo_azul.pack(side = 'left', expand = True, fill = 'both', padx = 20, pady = 20)

label_conteudo_vermelho.pack(expand = True, fill = 'both')
botao_conteudo_vermelho.pack(expand = True, fill = 'both', pady = 10)

label_conteudo_azul.pack(expand = True, fill = 'both')
botao_conteudo_azul.pack(expand = True, fill = 'both', pady = 10)

# run
window.mainloop()