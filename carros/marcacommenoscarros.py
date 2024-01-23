from listamarcas import *
from quantidadecarrosmarca import *


def marcacommenoscarros(carros):
    lista = []
    marcas = listamarcas(carros)
    menor_numero = 9999999
    marca_menor_numero = ''
    for marca in marcas:
        quantidade = quantidadecarrosmarca(carros, marca)
        lista.append([marca, quantidade])
    for i, v in enumerate(lista):
        if v[1] < menor_numero:
            menor_numero = v[1]
            marca_menor_numero = v[0]
    return marca_menor_numero, menor_numero
