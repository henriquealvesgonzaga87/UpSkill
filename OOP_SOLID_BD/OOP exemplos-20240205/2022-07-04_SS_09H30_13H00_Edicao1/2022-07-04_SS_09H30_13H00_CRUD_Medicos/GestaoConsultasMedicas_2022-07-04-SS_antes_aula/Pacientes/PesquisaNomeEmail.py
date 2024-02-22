# Pesquisa nome
import Menus.Menus
from Configuracao.Configuracao import *

# 1.1) ler o nome procurar
# 1.2) ler o email procurar
# 2) ler dados ficheiro
# 3) para cada registo: comparar o nome com o 'nome procurar'

#def Pesquisanome(nome_procurar):
def PesquisaNomeEMail():
	print('Pesquisa por nome')
	# 1) ler o nome procurar
	nome_procurar = input("Nome ?")
	email_procurar = input("E-Mail ?")
	# 2) ler dados ficheiro
	import csv
	lista = []
	import os
	path = os.getcwd()
	# print(path)
	nome = path.replace("\\Pacientes", "") + "/" + nomeFicheiroPacientes
	with open(nome, 'r', newline='', encoding='utf-8') as f:
	# with open("Pacientes/pacientes.csv", 'r', newline='', encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=';')
		next(reader)
		for r in reader:
			lista.append(tuple(r))
	# 3) para cada registo: comparar o nome com o 'nome procurar'
	#('3340', 'Rodolfo Carneiro Arouca Cardoso Caiado Almada Mateus', '17980-556', 'rodolforcaccam@sal.ipg.pt',	 '917777414', '236763153', '58941988', '49218454962', '2099-12-17')
	c = 0
	for r in lista:
		if r[1].find(nome_procurar) >=0 and r[3].find(email_procurar) >=0:     # -1 não
			c = c + 1
			print(r)
	print("Total resultados: ", c)
	Menus.Menus.Pausa('Prima Enter para continuar')
# nome_procurar = input("Nome ?")
# Pesquisanome(nome_procurar)
# Pesquisanome("Vivas")