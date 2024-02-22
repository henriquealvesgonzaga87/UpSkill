# Alterar
import sys, csv, os
sys.path.append('../')

import Menus.Menus
from Configuracao.Configuracao import *
import ValidacaoDados.ValidacaoDados as vd
import ValidacaoDados.validators_pt as vd2


def PrintFicha(r):
	cols = "Número;Nome;ViaVerde;EMail;Telemovel;NIF;NCC;NISS;DataNascimento".split(";")
	print("-" * 30)
	for i in range(len(r)):
		print("{0:<20s}: {1:s}".format(cols[i], r[i]))

def LerListaCSV(nome_ficheiro):
	lista = []
	with open(nome_ficheiro, 'r', newline='', encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=';')
		next(reader)
		for r in reader:
			# lista.append(tuple(r))
			lista.append(list(r))
	return lista

def GravarListaCSV(lista, nome):
	f = open(nome, 'w', newline='', encoding='utf-8')
	w = csv.writer(f, delimiter=';')
	cols = "Número;Nome;ViaVerde;EMail;Telemovel;NIF;NCC;NISS;DataNascimento".split(";")
	w.writerow(cols)
	w.writerows(lista)
	f.close()

def Alterar():
	print("-- A L T E R A R -- ")
	nome_alterar = input("Nome alterar ?")
	# 2) ler dados ficheiro
	path = os.getcwd()
	# print(path)
	nomef = path.replace("\\Pacientes", "") + "/" + nomeFicheiroPacientes
	lista = LerListaCSV(nomef)
	i = 0  # posicao registo a alterar
	for v in lista:
		if v[1].find(nome_alterar) >= 0:
			PrintFicha(v)
			op = input("Alterar  (0-Cancelar, 1-Alterar 2-Continuar pesquisa)?")
			if op == '0':
				break
			elif op == '1':
				nome = input("Novo nome?")
				# ... restantes dados
				lista[i][1] = nome
				# ...
				GravarListaCSV(lista, nomef)
				print("Médico alterado:")
				PrintFicha(lista[i])
				break
		i += 1
# Alterar()
