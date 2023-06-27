pacientes = [
    {'idade': 20, 'altura': 1.70, 'nome': 'Catarina Souza', 'sexo': 'F', 'infectado_covid': False},
    {'idade': 19, 'altura': 1.82, 'nome': 'José Henrique', 'sexo': 'M', 'infectado_covid': True},
    {'idade': 22, 'altura': 1.65, 'nome': 'Ana Carolina', 'sexo': 'F', 'infectado_covid': True},
    {'idade': 25, 'altura': 1.78, 'nome': 'Luiz Carlos', 'sexo': 'M', 'infectado_covid': False}
]

# for paciente in pacientes:
#     # if paciente['idade']<20:
#     #     continue
#     if paciente['altura']<1.70:
#         break
#     print(paciente)

pacientes.append({'idade': 21, 'altura': 1.69, 'nome': 'Matheus Santos', 'sexo': 'M', 'infectado_covid': False})

for paciente in pacientes:
    print(paciente)

pacientes.pop()
print('')
for paciente in pacientes:
    print(paciente)