from listamodelo import *


def quantidadeordenadatodosmodelos(carros):
	lista = []
	modelo = listamodelo(carros)
	quantidade = 0
	for i in modelo:
		if i in modelo:
			quantidade += 1
		lista.append([quantidade, i])
	sorted_lista = sorted(lista, key=lambda x: x[1])
	return sorted_lista

