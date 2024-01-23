def listamarcamodeloquantidade(carros):
	lista = []
	lista_modelo = []
	total_quantidade = []
	total_quantidade_modelo = []
	for i in carros:
		marca = i[1]
		if marca in lista:
			posicao = lista.index(marca)
			total_quantidade[posicao] += 1
		else:
			lista.append(marca)
			total_quantidade.append(1)
	for j in carros:
		modelo = j[2]
		if modelo in lista_modelo:
			posicao_modelo = lista_modelo.index(modelo)
			total_quantidade_modelo[posicao_modelo] += 1
		else:
			lista_modelo.append(modelo)
			total_quantidade_modelo.append(1)
	return list(zip(lista, total_quantidade)), list(zip(lista_modelo, total_quantidade_modelo))
