import time

tempo_inicio = time.time()
tempo_inicio_formatado = time.ctime()
print(tempo_inicio)
print('Hora atual:', tempo_inicio_formatado)

print('esperando 2s')
time.sleep(2)
print('2s se passaram')

for i in range(1, 6):
    print(i)
    time.sleep(1)

tempo_final = time.time()

print('Se passaram ',tempo_final - tempo_inicio, 'segundos')