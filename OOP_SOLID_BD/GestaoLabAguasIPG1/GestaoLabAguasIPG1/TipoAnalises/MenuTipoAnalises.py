# TipoAnalises

import Menus.Menus
import  Configuration.Configuracao
import LerGravarDados.LerGravarDados as ld
import ValidationData.ValidacaoDados as vd
import ValidationData.validators_pt as vd2
from TipoAnalises.Inserir import *
from TipoAnalises.Alterar import *
from TipoAnalises.Eliminar import *
from TipoAnalises.Listartodos import *
from TipoAnalises.Pesquisanome import *
from TipoAnalises.Pesquisapreco import *

def Menu():
	while True:
		op = Menus.Menus.Menu("TipoAnalises",['Inserir','Alterar','Eliminar','Listartodos','Pesquisanome','PesquisaPreço'], 6)
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
		elif op == 6:
			Pesquisapreco()

