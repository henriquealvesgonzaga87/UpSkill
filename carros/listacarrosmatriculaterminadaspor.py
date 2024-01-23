def listacarrosmatriculaterminadaspor(carros, texto):
	lista = list()
	for i in carros:
		verifica_matricula = i[0]
		if texto in verifica_matricula[-2:]:
			lista.append(i)
	return lista
