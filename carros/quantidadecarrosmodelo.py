def quantidadecarrosmodelo(lista, modelo_contar):
    total_quantidade = 0
    for i in lista:
        modelo = i[2]
        if modelo.lower() == modelo_contar:
            total_quantidade += 1
    return total_quantidade
