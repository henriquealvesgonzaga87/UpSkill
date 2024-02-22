# Inserir
#This shorthand makes one module visible to the other:
import sys
sys.path.append('../')

import Menus.Menus
from Configuracao.Configuracao import *
import ValidacaoDados.ValidacaoDados as vd
import ValidacaoDados.validators_pt as vd2

def LerDadosLista(nome_ficheiro):
	import csv, os
	lista = []
	with open(nome_ficheiro, 'r', newline='', encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=';')
		next(reader)
		c = 0
		for r in reader:
			c = c + 1
			lista.append(tuple(r))
			#if c == 10:
			#	break;
	return lista

def PesquisaCampoID(lista, campoID, valor):
    for j in lista:
        if j[campoID] == str(valor):
            return j
    return None

def ObterUltimoNumero(pacientes):
	# print(len(pacientes))
	# print(pacientes[0])
	# print(pacientes[len(pacientes) - 1])
	# print(pacientes[-1][0])
   #return int(pacientes[len(pacientes) - 1][0])
	return int(pacientes[-1][0])  #-1: ultimo | primeiro contar do fim


def PesquisaNCC(pacientes, x):
	for p in pacientes:
		if p[6] == x:
			return p
	return None

def PesquisaEMail(pacientes, x):
	for p in pacientes:
		if p[3] == x:
			return p
	return None

def Pesquisa(pacientes, x, coluna):
	for p in pacientes:
		if p[coluna] == x:
			return p
	return None

def PesquisaParcial(pacientes, x, coluna):
	lista = []
	for p in pacientes:
		if p[coluna].find(str(x)) >=0:
			lista.append(p)
	return lista


def Inserir():
	import os
	p = os.getcwd().replace("\\Pacientes", "")
	nomef = os.path.join(p, nomeFicheiroPacientes)
	pacientes = LerDadosLista(nomef)
	# print(pacientes)
	# ['Número', 'Nome', 'ViaVerde', 'EMail', 'Telemovel', 'NIF', 'NCC', 'NISS', 'DataNascimento']
	numero = ObterUltimoNumero(pacientes) + 1
	print(numero)

	# reg = PesquisaCampoID(pacientes, 0, "10")
	# print (reg)
	# reg = PesquisaCampoID(pacientes, 2, "10733-269")
	# print (reg)
	# exit()

	# nome = vd.LerNome("Nome ?")
	# dataNascimento = vd.LerData("Data nascimento ?")
	while True:
		nCC = vd2.LerCC("Nº Cartão Cidadão ?")
		reg = PesquisaNCC(pacientes, nCC)
		if reg != None:
			break
		else:
			print ("Existe um pacientes com o mesmo NCC %s" % nCC)
			print(reg)
	while True:
		x = vd.LerEMail("E-Mail ?")
		reg = Pesquisa(pacientes, x, 3)
		if reg != None:
			break
		else:
			print("Existe um pacientes com o mesmo E-Mail %s" % x)
			print(reg)
	eMail = x
	# telemovel = vd.LerTelemovel("Telemóvel ? ")
	# nIF = vd2.LerNIF("NIF ?")
	while True:
		x = vd2.LerNIF("NIF ?")
		reg = Pesquisa(pacientes, x, 5)
		if reg != None:
			break
		else:
			print("Existe um pacientes com o mesmo NIF %s" % x)
			print(reg)
	nIF = x
	# nISS = vd2.LerNISS("NISS ?")
	# viaVerde = input("Via Verde ?")


	#nCC = vd2.LerCC("Nº Cartão Cidadão ?")

	nome = "Ana Maria"
	dataNascimento = "2002-06-28"
	nCC = "46162043" # "10039784-0"
	eMail = "ana@ipg.pt"
	telemovel = "961234567"
	nIF = "123456789"
	nISS = "12345678901"
	viaVerde = "12345-123"     # ^[0-9]{5}-[0-9]{3}$

	# ----- verificar existência de dados (NIF, EMail) iguais ------


	# gravar dados
	f = open(nomef, "at", encoding="utf-8")
	print(file=f)
	print(numero, nome, viaVerde, eMail, telemovel, nIF, nCC, nISS, dataNascimento,
					   file=f, sep=';', end='')
	f.close()

	Menus.Menus.Pausa('Paciente inserido com sucesso.')




# Inserir()
