import Menus.Menus

import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c
import Menus.Menus

def Listartodos():
	print('Pedidos')
	dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

	print(f"{'Código':<10} {'CódigoCliente':<15} {'CódigoTipoAnalise':<20} {'Data':<25} {'DataPrevistaResultados':<25}")
	for x in dados["Pedidos"]:
		print(
			f"{x['Código']:<10} {x['CódigoCliente']:<15} {x['IDTipoCliente']:<20} {x['Data']:<25} {x['DataPrevistaResultados']:<25}")

	Menus.Menus.Pausa('Listar todos')
