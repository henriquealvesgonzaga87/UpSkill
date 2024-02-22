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
		codigo = int(input("Código do Tipo?"))
		i = 0
		for x in dados["TipoAnalises"]:
			if x["Código"] == codigo:
				print(f"O {codigo} já existe como nome {x['Nome']}")
				i = 1
		if i == 0:
			break


	Nome = vd.LerNome2("Nome?")
	if Nome is None:
		confirma=input("Cancelar inserir(s/n)?")
		if confirma == 's':
			return

	Preco = vd.LerNumero("Preço?", 1, 100000000, "naointeiro")

	Componentes = []


	while True:
		Componente = input("Componente: ")
			
		Valor = vd.LerNumero("Valor Máximo: ", 0, 100000, "naointeiro")
		Unidade = input("Unidade: ")
		Simbolo = input("Simbolo: ")
		Obs = input("Observações a adicionar: ")
		Componentes.append({
                   "Parâmetro": Componente,
                    "Valor": Valor,
					"Unidade": Unidade,
                	"Simbolo": Simbolo,
                	"Obs": Obs
					
                },)
		op = input("Continuar?(s/n)")
		if op == "n" or op == "N":
			break

	
	dados["TipoAnalises"].append({"Código": codigo,
									  "Nome": Nome,
									  "Preço": Preco, 
									  "Parametros": Componentes,
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
