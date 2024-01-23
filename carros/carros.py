# from lerdados import *
# from listamarcas import *
# from quantidadecarrosmarca import *
# from quantidadecarrospormarcatodos import *
# from quantidadecarros import *
# from quantidadecarrosporutente import *
# from marcacommaiscarros import *
# from marcacommenoscarros import *
# from modelocommaiscarros import *
# from anocommaiscarros import *
# from quantidadecarrosdadoano import *
# from quantidadecarrostodosanos import *
# from listacarrosmatriculacomecadapor import *
# from listacarrosmatriculaterminadaspor import *
# from listacarrosmatriculacontem import *
# from quantidadeordenadatodosmodelos import *
# from listamarcaquantidade import *
# from listamarcamodeloquantidade import *
#
# carros = lerdados('carros.txt')
# marca = listamarcas(carros)
# marca_carro = str(input("Digite uma marca do carro: ")).upper()
# modelo_carro = str(input("Digite o modelo: ")).upper()
# ano_carro = int(input("Digite o ano para saber a quantidade de carros: "))
# inicio_matricula = str(input("Digite os 2 primeiros digitos da matricula: ")).upper()
# fim_matricula = str(input("Digite os dois últimos numeros da matícula: ")).upper()
# digitos_matricula = str(input("digite dois digitos para saber a matricula: ")).upper()
# quantidade = quantidadecarrosmarca(lista=carros, marca_contar=marca_carro)
# print(f"Quantidade de carros da marca {marca_carro.title()}: {quantidade} - ({quantidade / len(carros) * 100:.2f}% do total de carros)")
# print(f"{marca}, quantidade: {len(marca)}")
# # for j in marca:
# #     print(f"{j}", end="; ")
# # print(f"quantidade: {len(marca)}")
# # lista_marcas_ordenadas = sorted(marca)
# # print(lista_marcas_ordenadas)
# # lista_coluna = listade(carros, 1)
# # print(lista_coluna)
# quantidade_carros = quantidadecarrospormarcatodos(carros)
# print(quantidade_carros)
# quantidade_total_carros = quantidadecarros(carros)
# print(f"A quantidade de total de carros é {quantidade_total_carros}")
# lista = quantidadecarrosporutente(carros)
# print(len(lista), lista[:10])
# print(utentecommaiscarros(carros))
# print(utentecommaiscarrosquantidade(carros))
# utente_mais_carro = utentescommaiscarros(carros)
# print(len(utente_mais_carro), utente_mais_carro[:10])
# mais_carros = marcacommaiscarros(carros)
# print(mais_carros)
# menos_carros = marcacommenoscarros(carros)
# print(menos_carros)
# modelo_mais_carro = modelocommaiscarros(carros)
# print(modelo_mais_carro)
# carros_ano = anocommaiscarros(carros)
# print(carros_ano)
# carros_dado_ano = quantidadecarrosdadoano(carros, str(ano_carro))
# print(carros_dado_ano)
# carros_todos_anos = quantidadecarrostodosanos(carros)
# matricula_comecada_por = listacarrosmatriculacomecadapor(carros, inicio_matricula)
# print(matricula_comecada_por)
# matricula_terminada_por = listacarrosmatriculaterminadaspor(carros, fim_matricula)
# print(matricula_terminada_por)
# matricula_contem = listacarrosmatriculacontem(carros, digitos_matricula)
# print(matricula_contem)
# modelo_quantidade = quantidadecarrosmodelo(carros, modelo_carro)
# print(modelo_quantidade)
# modelo_quantidade_ordenada = quantidadeordenadatodosmodelos(carros)
# print(modelo_quantidade_ordenada)
# marca_quantidade_ordenada = listamarcaquantidade(carros)
# print(marca_quantidade_ordenada)
# lista_ordenada_marca_modelo = listamarcamodeloquantidade(carros, marca_carro, modelo_carro)
# print(lista_ordenada_marca_modelo)
