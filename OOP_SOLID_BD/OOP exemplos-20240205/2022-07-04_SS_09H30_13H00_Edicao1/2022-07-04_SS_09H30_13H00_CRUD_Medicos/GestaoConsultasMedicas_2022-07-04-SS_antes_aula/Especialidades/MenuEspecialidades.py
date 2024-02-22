# Especialidades

import Menus.Menus
import Configuracao.Configuracao
import ValidacaoDados.ValidacaoDados as vd
import ValidacaoDados.validators_pt as vd2
from Especialidades.Inserir import *
from Especialidades.Alterar import *
from Especialidades.Eliminar import *
from Especialidades.Listartodos import *
from Especialidades.Pesquisanome import *

def Menu():
	while True:
		op = Menus.Menus.Menu("Especialidades",['Inserir','Alterar','Eliminar','Listartodos','Pesquisanome'], 5)
		if op == 0:
			break
		elif op == 1:
			Inserir()
		elif op == 2:
			Alterar()
		elif op == 3:
			Eliminar()
		elif op == 4:
			Listartodos()
		elif op == 5:
			Pesquisanome()

