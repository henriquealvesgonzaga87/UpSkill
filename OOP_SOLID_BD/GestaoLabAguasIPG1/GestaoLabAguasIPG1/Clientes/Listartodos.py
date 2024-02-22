import Menus.Menus

import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c
import Menus.Menus

def Listartodos():
	print('Clientes')
	dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

	print(f"{'IDCliente':^9} {'Nome':20} {'Tipo Cliente':^20} {'Email':20} {'Telefone':9} "
		  f"{'Telemovel':^9}")
	for x in dados["Clientes"]:
		print(f"{x['IDCliente']:^9} {x['Nome']:20} {x['IDTipoCliente']:^20} {x['Email']:20} {x['Telefone']:9} {x['Telemovel']:9}")


	Menus.Menus.Pausa('Listar todos')
