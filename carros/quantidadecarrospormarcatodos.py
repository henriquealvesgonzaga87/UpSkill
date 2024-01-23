from listamarcas import *
from quantidadecarrosmarca import *


def quantidadecarrospormarcatodos(lista):
    r = []
    marcas = listamarcas(lista)
    for m in marcas:
        qt = quantidadecarrosmarca(lista, m)
        r.append([m, qt])
    return sorted(r)
