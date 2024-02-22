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
		IDFuncionario = vd.LerNumero("ID Cliente (0-Cancelar)?",0,99999,"inteiro")
		if IDFuncionario == 0:
			return
		pos= -1
		Func, pos = pc.PesquisaEmListaDic(dados["Funcionários"], pos+1,{"IDFuncionário": IDFuncionario})
		if Func != None:
			print(Func)
			op = input("Alterar (S/N)?")
			if op == "S":
				break
		else:
			print(f"O código {IDFuncionario} não existe.")


	novoCliente = Func
	Departamento = vd.LerNumero(f"Departamento ({Func['IDDepartamento']})?", 1, 99,"inteiro")
	if Departamento is not None:
		novoCliente['IDDepartamento'] = Departamento

	Nome = vd.LerNome2(f"Nome ({Func['Nome']})?")
	if Nome is not None:
		novoCliente['Nome'] = Nome

	x = vd.LerEMail2("Email?")
	if x is not None:
		novoCliente['Email'] = x

	x = vd.LerTelemovel2("Telemovel?")
	if x is not None:
		novoCliente['Telemovel'] = str(x)

	dados["Clientes"][pos]=novoCliente
	ld.GravarJSON(c.nomeFicheiroTipoJSON, dados)


