def listacarrosmatriculacontem(carros, texto):
	lista = list()
	for i in carros:
		verifica_matricula = i[0]
		if texto.upper() in verifica_matricula:
			lista.append(i)
	return lista
