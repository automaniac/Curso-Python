# def funcao():
#     print('oi')

# def soma(a, b):
#     return a + b

# # def subtracao(a, b):
# #     return a - b
# subtracao = lambda a,b: a-b

# n1 = 4
# n2 = 7
# valor_soma = soma(n1, n2, 6)

# print(f'O valor da soma entre {n1} e {n2} é {valor_soma}')

# valor_subtracao = subtracao(n1, n2)

# print(f'O valor da subtracao entre {n1} e {n2} é {valor_subtracao}')


def somatorio(*args, **kwargs):
    soma = 0
    for arg in args:
        if kwargs['operacao'] == 'soma':
            soma = soma + arg
        else:
            soma = soma - arg
    print(soma)

somatorio(1,2,3,4,5,6,7,8,9,10, operacao='subtracao')

