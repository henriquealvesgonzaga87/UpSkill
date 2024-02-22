# Clientes

import Menus.Menus
import  Configuration.Configuracao
import LerGravarDados.LerGravarDados as ld
import ValidationData.ValidacaoDados as vd
import ValidationData.validators_pt as vd2
from Funcionarios.Inserir import *
from Funcionarios.Alterar import *
from Funcionarios.Eliminar import *
from Funcionarios.Listartodos import *
from Funcionarios.Pesquisanome import *
from Funcionarios.Pesquisacodigo import *

def Menu():
	while True:
		op = Menus.Menus.Menu("Clientes",['Inserir','Alterar','Eliminar','Listartodos','Pesquisanome','PesquisaDepartamento'], 6)
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

