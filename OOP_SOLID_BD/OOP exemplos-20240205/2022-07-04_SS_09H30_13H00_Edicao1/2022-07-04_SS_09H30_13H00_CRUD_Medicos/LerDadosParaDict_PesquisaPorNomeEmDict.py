def LerCSVDicionario(nome_ficheiro):
    import csv, os
    lista = []
    with open(nome_ficheiro, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        for r in reader:
            lista.append(tuple(r))
    return lista
def PesquisaNome(lista, nome_procurar):
    resultado = []
    for j in lista:
        if j[1].find(nome_procurar) >=0:
            #print(j)
            resultado.append(j)
    return resultado


lista = LerCSVDicionario("pacientes.csv")
lista = PesquisaNome(lista, "Maria")
print(len(lista), lista)
lista = PesquisaCodigo(lista, "360")
print(len(lista), lista)


