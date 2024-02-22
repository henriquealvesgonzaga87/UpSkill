# Alterar
import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c
import ValidationData.validators_pt as vdpt
import ValidationData.ValidacaoDados as vd
import Clientes.PesquisaCliente as pc


def Alterar():
	print('Alterar:TipoAnalises')
	dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

	while True:
		Codigo= vd.LerNumero("IDTipoAnalise (0-Cancelar)?",0,99999,"inteiro")
		if Codigo == 0:
			return
		pos= -1
		Analise, pos = pc.PesquisaEmListaDic(dados["TipoAnalises"], pos+1,{"Código": Codigo})
		if Analise != None:
			print(Analise)
			op = input("Alterar (S/N)?")
			if op == "S":
				break
		else:
			print(f"O código {Codigo} não existe.")


	novoTipoAnalise= Analise
	while True:
		Codigo = vd.LerNumero(f"Tipo Cliente ({Analise['Código']})?", 1, 99,"inteiro")
		i = 0
		for x in dados["TipoAnalises"]:
			if x["Código"] == Codigo:
				print(f"O {Codigo} já existe como nome {x['Nome']}")
				i = 1
		if i == 0:
			break
	if Codigo is not None:
		novoTipoAnalise['Código'] = Codigo

	Nome = vd.LerNome2(f"Nome ({Analise['Nome']})?")
	if Nome is not None:
		novoTipoAnalise['Nome'] = Nome

	Preco = vd.LerNumero("Preço?", 1, 100000000, "naointeiro")
	if Preco is not None:
		novoTipoAnalise['Preço'] = Preco

	dados["TipoAnalises"][pos]=novoTipoAnalise
	ld.GravarJSON(c.nomeFicheiroTipoJSON, dados)


