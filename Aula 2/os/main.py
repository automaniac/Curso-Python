import os

diretorio_atual = os.getcwd()

# print('caminho atual:', diretorio_atual)

diretorio_arquivo = os.path.abspath(os.path.dirname(__file__))

# print('caminho arquivo:', diretorio_arquivo)

os.chdir(diretorio_arquivo)

# diretorio_atual = os.getcwd()

# print('caminho atual:', diretorio_atual)

# lista = os.listdir()

# print(lista)

if os.path.exists('pasta/arquivo.txt'):
    os.remove('pasta/arquivo.txt')
else:
    print('arquivo não existe')

if not os.path.exists('novo_diretorio'):
    os.mkdir('novo_diretorio')
else:
    print('diretorio ja existe')

os.system('dir')