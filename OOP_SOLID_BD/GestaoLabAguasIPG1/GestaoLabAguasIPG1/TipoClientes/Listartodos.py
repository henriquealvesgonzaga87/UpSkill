# Listar todos
import Menus.Menus

import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c



def Listartodos():
	dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

	print(f"{'Código':>6} {'Nome'}")
	for x in dados["TipoClientes"]:
		print(f"{x['Código']:^6} {x['Nome']}")

	Menus.Menus.Pausa('Listar todos')
	# Put the code here to implement the functionality

