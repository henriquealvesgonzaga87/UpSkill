from lerdados import *
from anocommaiscarros import *
from listacarrosmatriculacomecadapor import *
from listacarrosmatriculacontem import *
from listacarrosmatriculaterminadaspor import *
from listamarcamodeloquantidade import *
from listamarcaquantidade import *
from listamarcas import *
from listamodelo import *
from marcacommaiscarros import *
from marcacommenoscarros import *
from modelocommaiscarros import *
from quantidadecarros import *
from quantidadecarrosdadoano import *
from quantidadecarrosmarca import *
from quantidadecarrosmodelo import *
from quantidadecarrospormarcatodos import *
from quantidadecarrosporutente import *
from quantidadecarrostodosanos import *
from quantidadeordenadatodosmodelos import *


ano_mais_carros = anocommaiscarros(carros)
print(f"Ano: {ano_mais_carros[0]} - quantidade: {ano_mais_carros[1]}")
lista_ano_carros = listaano(carros)
print(lista_ano_carros)
matricula_comeca = listacarrosmatriculacomecadapor(carros, '88')
print(matricula_comeca[:10])
matricula_contem = listacarrosmatriculacontem(carros, 'fg')
print(matricula_contem[:10])
matricula_termina = listacarrosmatriculaterminadaspor(carros, '85')
print(matricula_termina[:10])
lista_resultado = listamarcamodeloquantidade(carros)
print(lista_resultado)
lista_marca_quantidade = listamarcaquantidade(carros)
print(lista_marca_quantidade)
lista_marcas = listamarcas(carros)
print(lista_marcas)
lista_modelo = listamodelo(carros)
print(lista_modelo)
marca_mais_carros = marcacommaiscarros(carros)
print(f"Marca c/ mais carros: {marca_mais_carros[0]}; quantidade: {marca_mais_carros[1]}")
marca_menos_carros = marcacommenoscarros(carros)
print(f"Marca c/ menos carros: {marca_menos_carros[0]}; quantidade: {marca_menos_carros[1]}")
modelo_mais_carros = modelocommaiscarros(carros)
print(f"Modelo c/ mais carros: {modelo_mais_carros[0]}; quantidade: {modelo_mais_carros[1]}")
print(f"Quantidade de carros registrados: {quantidadecarros(carros)}")
quantidade_carros_ano = quantidadecarrosdadoano(carros, '2007')
print(f"ano a verificar: {quantidade_carros_ano[0]}; quantidade: {quantidade_carros_ano[1]}")
marca_verificar = 'BMW'
qtde_carros_marca = quantidadecarrosmarca(carros, marca_verificar)
print(f"Marca a verificar: {marca_verificar}; quantidade: {qtde_carros_marca}")
modelo = 'corsa'
quantidade_carros_modelo = quantidadecarrosmodelo(carros, modelo)
print(f"Modelo a verificar: {modelo}; quantidade: {quantidade_carros_modelo}")
quantidade_carros_por_marca = quantidadecarrospormarcatodos(carros)
print(quantidade_carros_por_marca)
qtde_carros_utente = quantidadecarrosporutente(carros)
print(qtde_carros_utente[:10])
carros_por_ano = quantidadecarrostodosanos(carros)
print(carros_por_ano)
qtde_ordenada_modelos = quantidadeordenadatodosmodelos(carros)
print(qtde_ordenada_modelos)
