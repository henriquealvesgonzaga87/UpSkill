from listaano import *
from quantidadecarrosano import *


# Ano com mais carros
def anocommaiscarros(carros):
    lista = []
    carro_ano = listaano(carros)
    maior_numero = 0
    ano_mais_carros = ''
    for ano in carro_ano:
        quantidade = quantidadecarrosano(carros, ano)
        lista.append([ano, quantidade])
    for i, v in enumerate(lista):
        if v[1] > maior_numero:
            maior_numero = v[1]
            ano_mais_carros = v[0]
    return ano_mais_carros, maior_numero
