# Pesquisa nome

import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c
import Menus.Menus
import ValidationData.validators_pt as vdpt
import ValidationData.ValidacaoDados as vd
import Clientes.PesquisaCliente as pc
def PesquisaResultados():
	print('Pesquisas: Pesquisa Resultados')
	dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

	# Put the code here to implement the functionality

	resultado = vd.LerNome("Resultado (Positivo/Negativo) (enter para continuar)")

	if resultado is None:
		return

	pos = -1
	while True:
		id, pos = pc.PesquisaEmListaDic(dados["Resultados"], pos + 1, {"Resultado": resultado})
		if id != None:
			print(pos, id)
			op = input("Continuar pesquisa (s/n)")
			if op == 'n':
				break
		else:
			print(f'O resultado {resultado} não foi encontrado em resultados')
			return PesquisaResultados()

	Menus.Menus.Pausa('Pesquisa Resultados')

