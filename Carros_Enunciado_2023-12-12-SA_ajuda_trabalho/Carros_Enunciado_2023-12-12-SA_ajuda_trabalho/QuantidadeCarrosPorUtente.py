# Quantidade de carros por pessoa (IDUtente)
# 1 o mais resultados? lista
def QuantidadeCarrosPorUtente(carros):
    utentes = []
    qts = []
    for c in carros:
        IDUtente = c[4]
        if IDUtente in utentes:
            pos = utentes.index(IDUtente)
            qts[pos] = qts[pos] + 1
        else:
            utentes.append(IDUtente)
            qts.append(1)
    return sorted(list(zip(qts, utentes)), reverse=True)
def UtenteComMaisCarros_X(carros):
    return sorted(QuantidadeCarrosPorUtente(carros), reverse=True) [0][1]  #13734185-(7, '13734185'),

# um tuplo
def UtenteComMaisCarros(carros):
    return QuantidadeCarrosPorUtente(carros)[0][1]  #13734185-(7, '13734185'),
def UtenteComMaisCarrosQuantidade(carros):
    return ( QuantidadeCarrosPorUtente(carros)[0][1],    # ('13734185',7),
                QuantidadeCarrosPorUtente(carros)[0][0])
# lista
def UtentesComMaisCarros(carros):
    lista = []
    # devolver todos os elementos do vetor cujo nº carros
    #       = utente com mais carros
    qt_mais = UtenteComMaisCarrosQuantidade(carros)[1] -1
    c = 0
    for x in QuantidadeCarrosPorUtente(carros)[1:]:   # qt, utente
        if x[0] == qt_mais:
            lista.append(x[1])
        elif x[0] < qt_mais:
            break
        c = c + 1
    print(c)
    return lista
def UtentesTopNComMaisCarros(carros, top):
    return UtentesComMaisCarros(carros)[:top]

# Matricula;Marca;Modelo;Ano;IDUtente;IDCarro
# 06-FK-48;Renault;Espace;2007;14806663;1
