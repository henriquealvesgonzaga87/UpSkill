# Pedidos

import Menus.Menus
import  Configuration.Configuracao
import LerGravarDados.LerGravarDados as ld
import ValidationData.ValidacaoDados as vd
import ValidationData.validators_pt as vd2
from Pedidos.Inserir import *
from Pedidos.Alterar import *
from Pedidos.Eliminar import *
from Pedidos.Listartodos import *
from Pedidos.PesquisaTipoAnalise import *
from Pedidos.PesquisaTipoCliente import *
from Pedidos.PesquisaCliente import *
from Pedidos.PesquisaData import *
from Pedidos.PesquisaTipoAnalise import *

def Menu():
	while True:
		op = Menus.Menus.Menu("Pedidos",['Inserir','Alterar','Eliminar','Listartodos','PesquisaTipoAnalise','PesquisaCliente','PesquisaTipoCliente','PesquisaData'], 8)
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
			PesquisaTipoAnalise()
		elif op == 6:
			PesquisaCliente()
		elif op == 7:
			PesquisaTipoCliente()
		elif op == 8:
			PesquisaData()
