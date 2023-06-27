import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self, title, size):
        width, height = size
        super().__init__()
        self.title(title)
        self.geometry(f'{width}x{height}')
        self.minsize(width, height)
        
        self.criar_widgets()
        self.dispor_widgets()

    def criar_widgets(self):
        self.frame_menu = FrameMenu(self)
        self.frame_conteudo = FrameConteudo(self)

    def dispor_widgets(self):
        self.frame_menu.place(x = 0, y = 0, relwidth = 0.3, relheight = 1)
        self.frame_conteudo.place(relx = 0.3, y = 0, relwidth = 0.7, relheight = 1)

class FrameMenu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.criar_widgets()
        self.dispor_widgets()

    def criar_widgets(self):
        self.botao_menu_esquerda = ttk.Button(self, text = 'Botão esquerda')
        self.botao_menu_direita = ttk.Button(self, text = 'Botão direita')
        self.botao_menu_baixo = ttk.Button(self, text = 'Botão baixo')

        self.slider_menu_esquerda = ttk.Scale(self, orient = 'vertical')
        self.slider_menu_direita = ttk.Scale(self, orient = 'vertical')

        self.frame_toggle = ttk.Frame(self)
        self.toggle_menu_esquerda = ttk.Checkbutton(self.frame_toggle, text = 'Check 1')
        self.toggle_menu_direita = ttk.Checkbutton(self.frame_toggle, text = 'Check 2')
    
        self.entry_menu = ttk.Entry(self)

    def dispor_widgets(self):
        self.columnconfigure((0,1,2), weight = 1, uniform = 'a')
        self.rowconfigure((0,1,2,3,4), weight = 1, uniform = 'a')

        self.botao_menu_esquerda.grid(row = 0, column = 0, sticky = 'nswe', columnspan = 2, padx = 4, pady = 4)
        self.botao_menu_direita.grid(row = 0, column = 2, sticky = 'nswe', padx = 4, pady = 4)
        self.botao_menu_baixo.grid(row = 1, column = 0, columnspan = 3, sticky = 'nsew', padx = 4, pady = 4)

        self.slider_menu_esquerda.grid(row = 2, column = 0, rowspan = 2, sticky = 'nsew', pady = 20)
        self.slider_menu_direita.grid(row = 2, column = 2, rowspan = 2, sticky = 'nsew', pady = 20)

        self.frame_toggle.grid(row = 4, column = 0, columnspan = 3, sticky = 'nsew')
        self.toggle_menu_esquerda.pack(side = 'left', expand = True)
        self.toggle_menu_direita.pack(side = 'left', expand = True)

        # entry layout
        self.entry_menu.place(relx = 0.5, rely = 0.95, relwidth = 0.9, anchor = 'center')

class FrameConteudo(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.criar_widgets()
        self.dispor_widgets()

    def criar_widgets(self):
        self.frame_conteudo_vermelho = FrameSecao(self, 'Vermelho', 'botao vermelho',  'red')
        self.frame_conteudo_azul = FrameSecao(self, 'Azul', 'botao azul', 'blue')
        self.frame_conteudo_verde = FrameSecao(self, 'Verde','botao verde', 'green')
    def dispor_widgets(self):
        self.frame_conteudo_vermelho.pack(side = 'left', expand = True, fill = 'both', padx = 20, pady = 20)
        self.frame_conteudo_azul.pack(side = 'left', expand = True, fill = 'both', padx = 20, pady = 20)
        self.frame_conteudo_verde.pack(side='left', expand = True, fill = 'both', padx = 20, pady = 20)


class FrameSecao(ttk.Frame):
    def __init__(self, parent, texto_label, texto_botao, cor):
        super().__init__(parent)

        self.texto_label = texto_label
        self.texto_botao = texto_botao
        self.cor = cor

        self.criar_widgets()
        self.dispor_widgets()

    def criar_widgets(self):
        self.label_secao = ttk.Label(self, text = self.texto_label, background = self.cor)
        self.botao_secao = ttk.Button(self, text = self.texto_botao)


    def dispor_widgets(self):
        self.label_secao.pack(expand = True, fill = 'both')
        self.botao_secao.pack(expand = True, fill = 'both', pady = 10)


if __name__ == '__main__':
    window = MainWindow('App complexo', (600, 600))
    window.mainloop()
