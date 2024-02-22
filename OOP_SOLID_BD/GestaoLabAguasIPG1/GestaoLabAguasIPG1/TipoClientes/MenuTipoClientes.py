# TipoClientes

import Menus.Menus
import  Configuration.Configuracao
import LerGravarDados.LerGravarDados as ld
import ValidationData.ValidacaoDados as vd
import ValidationData.validators_pt as vd2
from TipoClientes.Inserir import *
from TipoClientes.Alterar import *
from TipoClientes.Eliminar import *
from TipoClientes.Listartodos import *
from TipoClientes.ListartodosHTML import *



def Menu():
	while True:
		op = Menus.Menus.Menu("TipoClientes",
							  ['Inserir','Alterar','Eliminar','Listartodos',
							   'ListartodosHTML'], 5)
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
			ListartodosHTML()

