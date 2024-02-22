# Alterar
from ClasseEspecialidades import *
import Menus
bd = EspecialidadesCRUDSQLServer(server='.', database='ClinicaUpSkill')

def Alterar():
	print('Alterar')
	while True:
		cd = int(input("Código de especialidade a alterar?"))
		dados = bd.PesquisaCodigo(cd)
		if dados is not None:
			print(dados)
			while True:
				e = input('Especialidade ?')
				if e != '':
					break
			if bd.AtualizaNome(cd, e):
				Menus.Pausa(f'Especialidade {cd} alterada para {e} com sucesso')
				return
			else:
				Menus.Pausa(f'Ocorreu um erro ao alterar a especialidade {cd}')
		else:
			Menus.Pausa(f'Especialidade {cd} não encontrada')

