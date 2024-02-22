# Alterar
import Menus.Menus
import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c


def Alterar():
	dados = ld.LerJSON(c.nomeFicheiroTipoJSON)


	print('Alterar tipo clientes')

	while True:
		cod = input('Código?')
		# existe ?
		# X = {'Código': '1', 'Nome': 'Empresa'}
		f = 0
		for i in range(len(dados["TipoClientes"])):
			x = dados["TipoClientes"][i]
			if x ["Código"] == cod:
				f = 1
				pos = i
				print(f"nome {x['Nome']}")
				op = input("Desejas alterar: (S/N)")
				if op == 'S' or 's':
					break
				else:
					return

		if f == 0:
			print("Não encontrado!")
		else:
			break

	while True:
		nome = input("Novo Tipo de Cliente:? ")

		i = 0
		for x in dados["TipoClientes"]:
			if x["Nome"] == nome:
				print(f"O nome {nome} já existe como código {x['Código']}")
				i = 1
		if i == 0:
			break

	dados["TipoClientes"][pos]["Nome"] = nome
	ld.GravarJSON(c.nomeFicheiroTipoJSON, dados)

	Menus.Menus.Pausa('Alterar')