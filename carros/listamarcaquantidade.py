from listamarcas import *
from quantidadecarrosmarca import *


def listamarcaquantidade(carros):
	lista = []
	marca = listamarcas(carros)
	for i in marca:
		quantidade = quantidadecarrosmarca(carros, i)
		lista.append([quantidade, i])
	sorted_lista = sorted(lista, reverse=True)
	return sorted_lista
