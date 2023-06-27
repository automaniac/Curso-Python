import json

json_string = '{"nome": "João", "idade": 30}'
objeto_python = json.loads(json_string)
print(objeto_python, type(objeto_python))

objeto_python = {"nome": "Maria", "idade": 25}
json_string = json.dumps(objeto_python)
print(json_string, type(json_string))

with open('RDA.json', 'r') as arquivo:
    objeto_rda = json.load(arquivo)

print('paciente', objeto_rda['patient'])

with open('exemplo.json', 'w') as arquivo:
    json.dump(objeto_python, arquivo)


