def listade(lista, coluna):
	r = []
	for x in lista:
		if x[coluna] not in r:
			r.append(x[coluna])
	return r
