# Listar todos
from ClasseEspecialidades import *
import Menus
bd = EspecialidadesCRUDSQLServer(server='.', database='ClinicaUpSkill')

def Listartodos():
	print('Listar todas as especialidades')
	registos = bd.getDadosTabelaLista()
	print('{0:<12s}'.format('IDEspecialidade'), end='')
	print(' {0:<50s}'.format('Especialidade'))
	for r in registos:
		print('{0:^12d}'.format(r[0]), end='')
		print(' {0:<20s}'.format(r[1]))
	Menus.Pausa()


