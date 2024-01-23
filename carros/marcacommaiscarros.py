from listamarcas import *
from quantidadecarrosmarca import *


# Marca com mais carros
def marcacommaiscarros(carros):
    lista = []
    marcas = listamarcas(carros)
    maior_valor = 0
    marca_maior_numero = ''
    for marca in marcas:
        quantidade = quantidadecarrosmarca(carros, marca)
        lista.append([marca, quantidade])
    for i, v in enumerate(lista):
        if v[1] > maior_valor:
            maior_valor = v[1]
            marca_maior_numero = v[0]
    return marca_maior_numero, maior_valor
