# Eliminar
import Menus.Menus
import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c

#Eliminar
def Eliminar():

	op = 'N'

	print('Eliminar Clientes')
	dados = ld.LerJSON(c.nomeFicheiroTipoJSON)
	while True:
		cod = int(input('IDCliente?'))
		# existe ?
		# X = {'Código': '1', 'Nome': 'Empresa'}
		f = 0
		for i in range(len(dados["Clientes"])):
			x = dados["Clientes"][i]
			if x["IDCliente"] == cod:
				f = 1
				pos = i
				print(f"nome {x['Nome']}")
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

		dados["Clientes"].pop(pos)

		ld.GravarJSON(c.nomeFicheiroTipoJSON, dados)

	Menus.Menus.Pausa('Eliminar')