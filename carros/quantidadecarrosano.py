def quantidadecarrosano(lista, ano_contar):
    total_quantidade = 0
    for i in lista:
        ano = i[3]
        if ano == ano_contar:
            total_quantidade += 1
    return total_quantidade
