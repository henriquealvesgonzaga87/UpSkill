# Eliminar

from ClasseEspecialidades import *
import Menus
bd = EspecialidadesCRUDSQLServer(server='.', database='ClinicaUpSkill')

def Eliminar():
	print('Eliminar')
	while True:
		cd = int(input("Código de especialidade a eliminar?"))
		dados = bd.PesquisaCodigo(cd)
		if dados is not None:
			print(dados)
			while True:
				e = input('Confirma eliminar  (S/N)?')
				if e != '':
					break
			if bd.Eliminar(cd):
				Menus.Pausa(f'Especialidade {dados} eliminada com sucesso')
				return
			else:
				Menus.Pausa(f'Ocorreu um erro ao eliminar a especialidade {dados}')
		else:
			Menus.Pausa(f'Especialidade {cd} não encontrada')
