def PesquisaEmListaDic(lista, pos, dic):
    chave = list(dic.keys())[0]
    valor = dic[chave]
    for i in range(pos, len(lista)):
        x = lista[i]
        if str(valor) in str(x[chave]):
            return x, i
    return None, None
