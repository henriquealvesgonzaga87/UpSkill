# Inserir
import Menus.Menus

import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c


def Inserir():
	print('Inserir tipo clientes')
	dados = ld.LerJSON(c.nomeFicheiroTipoJSON)
	while True:
		cod = input('Código?')
		if cod == '':
			return
		# existe ?
		# X = {'Código': '1', 'Nome': 'Empresa'}
		i = 0
		for x in dados["TipoClientes"]:
			if x ["Código"] == cod:
				print(f"O Código {cod} ja existe um nome {x['Nome']}")
				i = 1
		if i == 0:
			break

	while True:
		nome = input("Tipo cliente?")

		if nome == "":
			op = input("Desejas Sair? (S/N)")
			if op == "S":
				return
			else:
				continue

		i = 0
		for x in dados["TipoClientes"]:
			if x["Nome"] == nome:
				print(f"O nome {nome} já existe como código {x['Código']}")
				i = 1
		if i == 0:
			break

	dados["TipoClientes"].append({"Código":cod,"Nome":nome})
	ld.GravarJSON(c.nomeFicheiroTipoJSON, dados)




