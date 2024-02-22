# Medicos

import Menus.Menus
import Configuracao.Configuracao
import ValidacaoDados.ValidacaoDados as vd
import ValidacaoDados.validators_pt as vd2
from Medicos.Inserir import *
from Medicos.Alterar import *
from Medicos.Eliminar import *
from Medicos.Listartodos import *
from Medicos.Pesquisanome import *

def Menu():
	while True:
		op = Menus.Menus.Menu("Medicos",['Inserir','Alterar','Eliminar','Listartodos','Pesquisanome'], 5)
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

