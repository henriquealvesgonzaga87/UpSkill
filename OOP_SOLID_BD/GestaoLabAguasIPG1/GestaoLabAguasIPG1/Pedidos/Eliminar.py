# Eliminar
import Menus.Menus
import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c

#Eliminar
def Eliminar():

	op = 'N'

	print('Eliminar TipoAnalises')
	dados = ld.LerJSON(c.nomeFicheiroTipoJSON)
	while True:
		cod = int(input('IDPedido?'))
		f = 0
		for i in range(len(dados["Pedidos"])):
			x = dados["Pedidos"][i]
			if x["Código"] == cod:
				f = 1
				pos = i
				print(f"Pedido {x['Código']}")
				op = input("Desejas Eliminar: (S/N/C)")
				if op == 'S':
					break
				elif op == 'C':
					return

		if f == 0:
			print("Não encontrado!")
		else:
			break
	if op == 'S':

		dados["Pedidos"].pop(pos)
		dados["Resultados"].pop(pos)

		ld.GravarJSON(c.nomeFicheiroTipoJSON, dados)

	Menus.Menus.Pausa('Eliminar')