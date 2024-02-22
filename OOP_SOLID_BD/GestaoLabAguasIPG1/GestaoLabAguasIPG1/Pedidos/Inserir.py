# Inserir
import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c
import Menus.Menus
import ValidationData.validators_pt as vdpt
import ValidationData.ValidacaoDados as vd
import Clientes.PesquisaCliente as pc
import copy

def Inserir():

	print('Inserir:Clientes')
	dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

	

	while True:
		CodigoA = int(input("Codigo da Analise?"))
		i = 0
		for x in dados["Pedidos"]:
			if x["Código"] == CodigoA:
				print(f"O {CodigoA} já existe")
				i = 1
		if i == 0:
			break

	while True:
		IDCliente = vd.LerNumero("IDCliente?", 1, 99, "inteiro")
		i = 0
		for x in dados["Clientes"]:
			if x["IDCliente"] == (IDCliente):
				i = 1

		if i == 1:
			break
		if i == 0:
			print(f"O IDCliente com o Código {IDCliente} não existe")
	
	while True:
		IDTipoCliente = vd.LerNumero("Tipo Cliente?", 1, 99, "inteiro")
		i = 0
		for x in dados["TipoClientes"]:
			if x["Código"] == str(IDTipoCliente):
				i = 1

		if i == 1:
			break
		if i == 0:
			print(f"O Tipo de Cliente com o Código {IDTipoCliente} não existe")

	Data = vd.LerData(input("Digite a data(enter para voltar):"))
	if Data is None:
		return

	DataPrevistaResultados = vd.LerData(input("Digite a data prevista:"))
	if DataPrevistaResultados is None:
		DataPrevistaResultados = "Sem Data"

	while True:
		IDTipoAnalise = vd.LerNumero("TipoAnalise?", 1, 99, "inteiro")
		i = 0
		for x in dados["TipoAnalises"]:
			if x["Código"] == (IDTipoAnalise):
				i = 1
		if i == 1:
			pos = -1
			t = []
			Cliente, pos = pc.PesquisaEmListaDic(dados["TipoAnalises"], pos + 1, {"Código": IDTipoAnalise})
			dicionario_copia = Cliente["Parametros"]
			for x in Cliente["Parametros"]:
				t.append({"Parâmetro":x["Parâmetro"],"Valor": 0,"ValorMax":x["Valor"]})

			dados["Resultados"].append({"Código":CodigoA,"Data": Data,"CódigoCliente": IDCliente,"CódigoTipoAnalise": IDTipoAnalise,"Parametros":t})

			break
		if i == 0:
			print(f"O Tipo de Cliente com o Código {IDTipoAnalise} não existe")



	dados["Pedidos"].append({"Código": CodigoA,
								  "CódigoCliente": IDCliente,
							 "IDTipoCliente": IDTipoCliente,
								  "CódigoTipoAnalise":IDTipoAnalise,
							  "Data":str(Data),
							  "DataPrevistaResultados":str(DataPrevistaResultados),
							  "Parâmetros": dicionario_copia,})
	ld.GravarJSON(c.nomeFicheiroTipoJSON, dados)

# CREATE TABLE [dbo].[Cliente] (
#     [IDCliente] INT IDENTITY (1, 1) NOT NULL,
#     [IDTipoClienteFK] INT NOT NULL,
#     [Nome] NVARCHAR (100) NOT NULL,
#     [Email] NVARCHAR (50) NOT NULL,
#     [Telefone] NVARCHAR (15) NOT NULL,
#     [Telemovel] NVARCHAR (15) NOT NULL,
#     [NIF] NVARCHAR (10) NOT NULL,
#     [Morada] NVARCHAR (100) NOT NULL,
#     [CodigoPostal] NVARCHAR (8) NOT NULL,
#     [Localidade] NVARCHAR (100) NOT NULL,
#     [Logotipo] IMAGE NULL,
#     PRIMARY KEY CLUSTERED ([IDCliente] ASC),
#     FOREIGN KEY ([IDTipoClienteFK]) REFERENCES [dbo].[TipoCliente] ([IDTipoCliente])
#     );
