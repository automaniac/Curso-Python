grau = 0.5
controlado = True
condicoes_padroes = True

if controlado and condicoes_padroes:
	if grau >= 0.9:
		print('Ótimo!')
	elif grau > 0.7:
		print('Razoável')
	elif grau > 0.5:
		print('Aceitável')
	else:
		print('Ruim')
else:
	print('Inconclusivo')