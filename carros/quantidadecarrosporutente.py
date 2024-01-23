# Quantidade de carros por pessoa (IDUtente)
def quantidadecarrosporutente(carros):
    lista = []
    total_quantidade = []
    for i in carros:
        idutente = i[4]
        if idutente in lista:
            posicao = lista.index(idutente)
            total_quantidade[posicao] += 1
        else:
            lista.append(idutente)
            total_quantidade.append(1)
    return sorted(list(zip(lista, total_quantidade)), reverse=True)


def utentecommaiscarros(carros):
    return quantidadecarrosporutente(carros)[0][1]


def utentecommaiscarrosquantidade(carros):
    return (quantidadecarrosporutente(carros)[0][1],
            quantidadecarrosporutente(carros)[0][0])


def utentescommaiscarros(carros):
    lista = []
    # devolver todos os elementos do vetor cujo nº carros
    #       = utente com mais carros
    qt_mais = utentecommaiscarrosquantidade(carros)[1] - 1
    c = 0
    for x in quantidadecarrosporutente(carros)[1:]:  # qt, utente
        if x[0] == qt_mais:
            lista.append(x[1])
        elif x[0] < qt_mais:
            break
        c = c + 1
    print(c)
    return lista


def utentestopncommaiscarros(carros, top):
    return utentescommaiscarros(carros)[:top]
