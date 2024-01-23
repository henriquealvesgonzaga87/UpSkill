import csv
# Leitura de ficheiro \ac{CSV}
def LerFicheiroCSV(nome_ficheiro, delimitador):
    import csv
    lista = []
    with open(nome_ficheiro, 'rt', newline='',  encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=delimitador)
        cab = reader.__next__()
        for r in reader:
            lista.append(r)
    return cab, lista

# cab, lista = LerFicheiroCSV("moradas_aspas.csv", delimitador=',')
# print(cab)
# for m in lista:
#     print(m)

