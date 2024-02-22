# Inserir
from ClasseEspecialidades import *
import Menus
bd = EspecialidadesCRUDSQLServer(server='.', database='ClinicaUpSkill')


def Inserir():
	print('Inserir')
	while True:
		e = input('Especialidade ?')
		if e != '':
			break
	if bd.Inserir(e):
		Menus.Pausa(f'Especialidade {e} inserida com sucesso')
	else:
		Menus.Pausa(f'Ocorreu um erro ao inserir a especialidade {e}')


