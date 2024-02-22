# Clientes

import Menus.Menus
import  Configuration.Configuracao
import LerGravarDados.LerGravarDados as ld
import ValidationData.ValidacaoDados as vd
import ValidationData.validators_pt as vd2
from Clientes.Inserir import *
from Clientes.Alterar import *
from Clientes.Eliminar import *
from Clientes.Listartodos import *
from Clientes.Pesquisanome import *
from Clientes.Pesquisacodigo import *

def Menu():
	while True:
		op = Menus.Menus.Menu("Clientes",['Inserir','Alterar','Eliminar','Listartodos','Pesquisanome','PesquisaIDTipoClientes'], 6)
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
			Pesquisacódigo()

