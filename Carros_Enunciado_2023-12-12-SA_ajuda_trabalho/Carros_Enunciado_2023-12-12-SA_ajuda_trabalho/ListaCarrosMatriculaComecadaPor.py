def ListaCarrosMatriculaComecadaPor(carros, texto):
	lista = []
	for c in carros:
		# if str(c[0]).startswith(texto):   # True, False
		if str(c[0]).find(texto) == 0:  # pos: 0....len()-1
			lista.append(c)
	return lista

def ListaCarrosMatriculaContem(carros, texto):
	lista = []
	for c in carros:
		if str(c[0]).find(texto) >= 0:
			lista.append(c)
	return lista

#------------------------
# from ListaCarrosMatriculaComecadaPor import *
# lista = ListaCarrosMatriculaComecadaPor(carros, '99')
# print(len(lista), lista[0:10])


# Matricula;Marca;Modelo;Ano;IDUtente;IDCarro
# 06-FK-48;Renault;Espace;2007;14806663;1
