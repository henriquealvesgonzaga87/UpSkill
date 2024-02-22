# Especialidades

import Menus
from Inserir import *
from Alterar import *
from Eliminar import *
from Listartodos import *
from Pesquisanome import *
from Pesquisacodigo import *

def Menu():
	while True:
		op = Menus.Menu("Especialidades", ['Inserir', 'Alterar', 'Eliminar', 'Listar todos', 'Pesquisa nome', 'Pesquisa código'], 6)
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
			Pesquisacodigo()

Menu()