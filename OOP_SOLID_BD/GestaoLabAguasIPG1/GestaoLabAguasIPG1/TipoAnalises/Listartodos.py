# Listar todos
import Menus.Menus
import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c

def Listartodos():
	dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

	print(f"{'Código':6} {'Nome':20} {'Preço':5}")
	for x in dados["TipoAnalises"]:
		print(f"{x['Código']:6} {x['Nome']:20} {x['Preço']:5}")

	Menus.Menus.Pausa('Listar todos')
	# Put the code here to implement the functionality


