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
		IDFuncionario = int(input("IDFuncionario?"))
		i = 0
		for x in dados["Funcionários"]:
			if x["IDFuncionário"] == IDFuncionario:
				print(f"O {IDFuncionario} já existe como nome {x['Nome']}")
				i = 1
		if i == 0:
			break



	while True:
		Departamento = vd.LerNumero("Departamento?", 1, 99, "inteiro")
		i = 0
		for x in dados["Departamentos"]:
			if x["Código"] == str(Departamento):
				i = 1

		if i == 1:
			break
		if i == 0:
			print(f"O Departamento com o Código {Departamento} não existe")

	Nome = vd.LerNome2("Nome(enter para voltar)?")
	if Nome is None:
		return

	Email= vd.LerEMail("Email?")
	Telemovel= vd.LerTelemovel("Telemovel?")

	dados["Funcionários"].append({"IDFuncionário": IDFuncionario,
								  "IDDepartamento": Departamento,
								  "Nome":Nome,
							  "Email":Email,
							  "Telemovel":Telemovel
							  })
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
