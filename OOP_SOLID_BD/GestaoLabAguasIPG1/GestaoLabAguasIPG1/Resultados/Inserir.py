# Inserir
import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c
import Menus.Menus
import Clientes.PesquisaCliente as pc
import ValidationData.validators_pt as vdpt
import ValidationData.ValidacaoDados as vd
import Resultados.MenuResultados as r
def Inserir():

	print("Inserir: Resultados")
	dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

	pos = -1
	d = -1
	e = []
	while True:
		if dados["Resultados"] == []:
			return
		cod = input("Introduza o código do Pedido de Analise(enter para voltar)")
		if cod == "":
			return
		Resultado, pos = pc.PesquisaEmListaDic(dados["Resultados"], pos + 1, {"Código": cod})
		for x in Resultado["Parametros"]:
			param = x["Parâmetro"]
			codigo = int(input(f"Introduza os valores para {param}: "))
			x["Valor"] = codigo
			if x["Valor"] >= x["ValorMax"]:
				d = 1

		if d == 1:
			NovoResultado = Resultado
			NovoResultado["Resultado"] = "Negativo"
		else:
			NovoResultado = Resultado
			NovoResultado["Resultado"] = "Positivo"
		ld.GravarJSON(c.nomeFicheiroTipoJSON, dados)

		break


