import QuantidadeCarrosPorUtente
from LerDados import *
import QuantidaDeCarros

f = open("estatisticas.txt", "wt", encoding='UTF-8')
# Quantos carros existem?
carros = LerDados("carros.txt")
qt = QuantidaDeCarros.QuantidaDeCarros(carros)
s = f"Quantidade de carros: {qt}"
print(s)
print(s, file=f)
#-------------------------
from QuantidadeCarrosPorUtente import *
lista = QuantidadeCarrosPorUtente(carros)
print(len(lista), lista[0:10])

lista = UtentesComMaisCarros(carros)
print(len(lista), lista[0:10])

#------------------------
from ListaCarrosMatriculaComecadaPor import *
lista = ListaCarrosMatriculaComecadaPor(carros, '99')
print(len(lista), lista[0:10])

f.close()
exit()
