# carros por um dado ano
def quantidadecarrosdadoano(carros, ano):
    quantidade_total = 0
    for i in carros:
        verifica_ano = i[3]
        if verifica_ano == ano:
            quantidade_total += 1
    return ano, quantidade_total
