import csv
def LerDados(nome_ficheiro):
    lista = []
    with open(nome_ficheiro, 'rt', newline='') as f:
        reader = csv.reader(f, delimiter=';')
        reader.__next__()
        for r in reader:
            lista.append(r)
    return lista
