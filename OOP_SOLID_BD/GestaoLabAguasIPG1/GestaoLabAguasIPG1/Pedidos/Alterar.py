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
		Codigo= vd.LerNumero("ID Cliente (0-Cancelar)?",0,99999,"inteiro")
		if Codigo == 0:
			return
		pos= -1
		Pedido, pos = pc.PesquisaEmListaDic(dados["Pedidos"], pos+1,{"Código": Codigo})
		if Pedido != None:
			print(Pedido)
			op = input("Alterar (S/N)?")
			if op == "S":
				break
		else:
			print(f"O código {Codigo} não existe.")


	novoPedido= Pedido
	Codigo = vd.LerCod2(f"Tipo Cliente ({Pedido['Código']})?",)
	if Codigo is not None:
		novoPedido['Código'] = int(Codigo)
	
	CodigoCliente = vd.LerCod2(f"Tipo Cliente ({Pedido['CódigoCliente']})?")
	if Codigo is not None:
		novoPedido['CódigoCliente'] = int(CodigoCliente)
	
	CódigoTipoAnalise = vd.LerCod2(f"Tipo Cliente ({Pedido['CódigoTipoAnalise']})?")
	if Codigo is not None:
		novoPedido['CódigoTipoAnalise'] = int(CódigoTipoAnalise)

	dados["Pedidos"][pos]=novoPedido
	ld.GravarJSON(c.nomeFicheiroTipoJSON, dados)


