# Inserir
import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c
import Menus.Menus
import ValidationData.validators_pt as vdpt
import ValidationData.ValidacaoDados as vd

def Inserir():
	print('Inserir:Clientes')
	dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

	while True:
		IDCliente = int(input("Cliente?"))
		i = 0
		for x in dados["Clientes"]:
			if x["IDCliente"] == IDCliente:
				print(f"O {IDCliente} já existe como nome {x['Nome']}")
				i = 1
		if i == 0:
			break



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

	Nome = vd.LerNome2("Nome(enter para voltar)?")
	if Nome is None:
		return

	Email= vd.LerEMail("Email?")
	Telefone = vd.LerTelefone("Telefone?")
	Telemovel= vd.LerTelemovel("Telemovel?")
	while True:
		Nif=input("Nif?")
		if vdpt.controlNIF(Nif):
			break
	Morada = input("Morada?")

	while True:
		Codigop = input("Codigo Postal?")
		if vd.Lercodigopostal(Codigop):
			print("Código Postal Incorreto")
			break

	Localidade = input("Localidade?")

	dados["Clientes"].append({"IDCliente": IDCliente,
								  "IDTipoCliente": IDTipoCliente,
								  "Nome":Nome,
							  "Nif":Nif,
							  "Email":Email,
							  "Telefone":Telefone,
							  "Telemovel":Telemovel,
							  "Morada":Morada,
							  "CodigoPostal":Codigop,
							  "Localidade":Localidade})
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
