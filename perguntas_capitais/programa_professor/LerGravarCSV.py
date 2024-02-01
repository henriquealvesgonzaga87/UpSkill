def GravarListaEmFicheiroCSV(lista, nome_ficheiro, delimitador=';', titulos=None):
    """
    :param lista:
    :param nome_ficheiro:
    :param delimitador:
    :param titulos:
    :return:
    """
    import csv
    with open(nome_ficheiro, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=delimitador)
        if titulos is not None:
            writer.writerow(titulos)
        writer.writerows(lista)


def LerFicheiroCSVParaLista(nome_ficheiro, delimitador,tem_titulos=False):
    """
    :param nome_ficheiro:
    :param delimitador:
    :param tem_titulos:
    :return:
    """
    import csv
    lista = []
    titulos = []
    with open(nome_ficheiro, 'rt', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=delimitador)
        if tem_titulos:
            # Skips the heading:    # Using next() method
            titulos = next(reader)  # ou titulos = reader.__next__()
        for r in reader:
            lista.append(r)
    return titulos, lista
