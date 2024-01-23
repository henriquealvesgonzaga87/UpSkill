def listacarrosmatriculacomecadapor(carros, texto):
	lista = []
	for i in carros:
		verifica_matricula = i[0]
		if texto == verifica_matricula[:2]:
			lista.append(i)
	return lista
