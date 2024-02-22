# Eliminar
import sys, csv
sys.path.append('../')

import Menus.Menus
from Configuracao.Configuracao import *
import ValidacaoDados.ValidacaoDados as vd
import ValidacaoDados.validators_pt as vd2


def PrintFicha(r):
	cols = "Número;Nome;ViaVerde;EMail;Telemovel;NIF;NCC;NISS;DataNascimento".split(";")
	for i in range(len(r)):
		print("{0:<20s}: {1:s}".format(cols[i], r[i]))

def LerListaCSV(nome_ficheiro):
	import csv, os
	lista = []
	with open(nome_ficheiro, 'r', newline='', encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=';')
		next(reader)
		for r in reader:
			lista.append(tuple(r))
	return lista

def GravarListaCSV(lista, nome):
	f = open(nome + ".csv", 'w', newline='', encoding='utf-8')
	w = csv.writer(f, delimiter=';')
	cols = "Número;Nome;ViaVerde;EMail;Telemovel;NIF;NCC;NISS;DataNascimento".split(";")
	w.writerow(cols)
	w.writerows(lista)
	f.close()

def Eliminar():
	print("-- E L I M I N A R -- ")
	nome_eliminar = input("Nome eliminar ?")
	# 2) ler dados ficheiro
	import csv
	lista = []
	import os
	path = os.getcwd()
	# print(path)
	nomef = path.replace("\\Pacientes", "") + "/" + nomeFicheiroPacientes
	lista = LerListaCSV(nomef)
	i = 0
	for v in lista:
		if v[1].find(nome_eliminar) >= 0:
			PrintFicha(v)
			op = input("Eliminar  (0-Abortar, 1-Eliminar 2-Continuar pesquisa)?")
			if op == '0':
				break
			elif op == '1':
				# Using pop() to remove a dict. pair
				# removes Mani
				medico_eliminado = lista.pop(i)
				print("Médico eliminado:")
				PrintFicha(medico_eliminado)
				GravarListaCSV(lista, nomef)
				break
		i = i + 1
# Eliminar()
