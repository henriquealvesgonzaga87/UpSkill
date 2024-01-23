def quantidadecarrosmarca(lista, marca_contar):
    total_quantidade = 0
    for i in lista:
        marca = i[1]
        if marca == marca_contar:
            total_quantidade += 1
    return total_quantidade
