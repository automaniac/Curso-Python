# nome = 'João Pedro'
# idade = 20
# altura = 1.80
# sexo = 'M'
# infectado_covid = False

paciente = { 
    'nome':'João Pedro',
    'idade':20,
    'altura':1.80,
    'sexo':'M',
    'infectado_covid':False
}
print(paciente)
print(paciente['nome'], paciente['altura'])
paciente['infectado_covid'] = True
paciente['diagnostico'] = 'Covid'
print(paciente)
