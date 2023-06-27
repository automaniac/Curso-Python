import random

numero_aleatorio = random.random()
# print(numero_aleatorio)

lista = ["maçã", "banana", "laranja"]

# print(random.choice(lista))

random.shuffle(lista)
print(lista)

amostra = random.sample(lista, 1)

print(amostra)



