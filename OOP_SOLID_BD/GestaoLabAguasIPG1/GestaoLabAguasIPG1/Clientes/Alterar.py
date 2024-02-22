# Alterar
import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c
import ValidationData.validators_pt as vdpt
import ValidationData.ValidacaoDados as vd
import Clientes.PesquisaCliente as pc


def Alterar():
	print('Alterar:Clientes')
	dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

	while True:
		IDCliente= vd.LerNumero("ID Cliente (0-Cancelar)?",0,99999,"inteiro")
		if IDCliente == 0:
			return
		pos= -1
		Cliente, pos = pc.PesquisaEmListaDic(dados["Clientes"], pos+1,{"IDCliente": IDCliente})
		if Cliente != None:
			print(Cliente)
			op = input("Alterar (S/N)?")
			if op == "S":
				break
		else:
			print(f"O código {IDCliente} não existe.")


	novoCliente = Cliente
	IDTipoCliente = vd.LerNumero(f"Tipo Cliente ({Cliente['IDTipoCliente']})?", 1, 99,"inteiro")
	if IDTipoCliente is not None:
		novoCliente['IDTipoCliente'] = IDTipoCliente

	Nome = vd.LerNome2(f"Nome ({Cliente['Nome']})?")
	if Nome is not None:
		novoCliente['Nome'] = Nome

	x = vd.LerEMail2("Email?")
	if x is not None:
		novoCliente['Email'] = x

	x = vd.LerTelefone("Telefone?")
	if x is not None:
		novoCliente['Telefone'] = str(x)
	x = vd.LerTelemovel2("Telemovel?")
	if x is not None:
		novoCliente['Telemovel'] = str(x)
	while True:
		Nif=input("Nif?")
		if Nif == "":
			Nif = None
			break
		if vdpt.controlNIF(Nif):
			break
	if Nif is not None:
		novoCliente['Nif'] = x

	x = vd.LerNome2("Morada?")
	if x is not None:
		novoCliente['Morada'] = x

	while True:
		Codigop = input("Codigo Postal?")
		if Codigop == "":
			Codigop = None
			break
		if vd.Lercodigopostal(Codigop):
			break
	if Codigop is not None:
		novoCliente['CodigoPostal'] = Codigop

	x = vd.LerNome2("Localidade?")
	if x is not None:
		novoCliente['Localidade'] = x

	dados["Clientes"][pos]=novoCliente
	ld.GravarJSON(c.nomeFicheiroTipoJSON, dados)


