# Pacientes

import Menus.Menus
import Configuracao.Configuracao
import ValidacaoDados.ValidacaoDados as vd
import ValidacaoDados.validators_pt as vd2
# from Pacientes import *
from Pacientes.Inserir import *
from Pacientes.Alterar import *
from Pacientes.Eliminar import *
from Pacientes.Listartodos import *
from Pacientes.Pesquisanome import *
from Pacientes.PesquisaDataNascimento import *
from Pacientes.PesquisaNIF import *
from Pacientes.PesquisaNomeEmail import *

# print (dir(Pacientes))

def Menu():
	while True:
		op = Menus.Menus.Menu("Pacientes",['Inserir','Alterar','Eliminar','Listartodos',
										   'Pesquisa Nome',
										   'Pesquisa por Nome e E-Mail',
										   'Pesquisa Data Nascimento',
										   'Pesquisa NIF'], 8)
		if op == 0:
			break
		elif op == 1:
			Pacientes.Inserir.Inserir()
		elif op == 2:
			Alterar()
		elif op == 3:
			Eliminar()
		elif op == 4:
			Listartodos()
		elif op == 5:
			Pesquisanome()
		elif op == 6:
			PesquisaNomeEMail()
		elif op == 7:
			PesquisaDataNascimento()
		elif op == 8:
			PesquisaNIF()
