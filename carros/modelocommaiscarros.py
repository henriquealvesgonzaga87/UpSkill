from listamodelo import *
from quantidadecarrosmodelo import *


def modelocommaiscarros(carros):
    lista = []
    modelo = listamodelo(carros)
    maior_numero = 0
    modelo_maior_numero = ''
    for i in modelo:
        quantidade = quantidadecarrosmodelo(carros, i)
        lista.append([i, quantidade])
    for i, v in enumerate(lista):
        if v[1] > maior_numero:
            maior_numero = v[1]
            modelo_maior_numero = v[0]
    return modelo_maior_numero, maior_numero
