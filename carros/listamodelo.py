def listamodelo(lista):
    lista_modelo = []
    for i in lista:
        verifica_modelo = i[2]
        if verifica_modelo not in lista_modelo:
            lista_modelo.append(verifica_modelo)
    return lista_modelo
