def listamarcas(lista):
    lista_marcas = []
    for i in lista:
        verifica_marca = i[1]
        if verifica_marca not in lista_marcas:
            lista_marcas.append(verifica_marca)
    return lista_marcas
