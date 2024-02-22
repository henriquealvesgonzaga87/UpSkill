import Menus.Menus

import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c
import Menus.Menus

def Listartodos():
	print('ListarTodos')
	dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

	print(f"{'IDFuncionário':^9} {'Nome':20} {'Departamento':^20} {'Email':20} "
		  f"{'Telemovel':^9}")
	for x in dados["Funcionários"]:
		print(f"{x['IDFuncionário']:^9} {x['Nome']:20} {x['IDDepartamento']:^20} {x['Email']:20} {x['Telemovel']:9}")


	Menus.Menus.Pausa('Listar todos')
