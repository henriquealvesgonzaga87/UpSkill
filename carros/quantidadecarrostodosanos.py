from listaano import *
from quantidadecarrosano import *

# lista carros por ano
def quantidadecarrostodosanos(carros):
    lista = []
    ano = listaano(carros)
    for i in ano:
        quantidade = quantidadecarrosano(carros, i)
        lista.append([i, quantidade])
    return lista
