def listaano(lista):
    lista_ano = []
    for i in lista:
        verifica_ano = i[3]
        if verifica_ano not in lista_ano:
            lista_ano.append(verifica_ano)
    return sorted(lista_ano, reverse=True)
