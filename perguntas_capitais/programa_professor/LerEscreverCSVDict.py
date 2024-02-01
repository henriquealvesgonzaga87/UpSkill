import csv


def LerCSVParaListadeDicionarios(nome_ficheiro, delimitador=';'):
    dados = {}
    with open(nome_ficheiro, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=delimitador)
        # for r in reader:
        #     lista[r['']] = r  # load all records - dict of dicts
        dic = [r for r in reader] # load all records - list of dicts
    return dic


def LerCSVParaDicionariodeDicionarios(nome_ficheiro, chave, delimitador=';'):
    dados = {}
    with open(nome_ficheiro, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=delimitador)
        dic_dic = {}
        for r in reader:
             dic_dic[r[chave]] = r  # load all records - dict of dicts
        # lista = [r for r in reader]  # load all records - list of dicts
    return dic_dic


def GravarListaDeDicionarioCSV(lista_dicionarios, nome_ficheiro, delimitador=';'):
    with open(nome_ficheiro, 'w', newline='', encoding='utf-8') as csvfile:
        # a) 1 linha da lista. b) chaves da linha. c) conversão para lista
        titulos = list(lista_dicionarios[0].keys())
        writer = csv.DictWriter(csvfile, delimiter=delimitador, fieldnames=titulos)
        writer.writeheader()
        writer.writerows(lista_dicionarios)
        # for r in lista_dicionarios:
        #     writer.writerow(r)


def GravarDicionarioDeDicionarioCSV(dicionario_dicionarios, nome_ficheiro, delimitador=';'):
    with open(nome_ficheiro, 'w', newline='', encoding='utf-8') as csvfile:
        # a) chaves para lista e chave1. b) 1º dicionario da chave1.
        # c) chaves da chave1 e conversão para lista
        chave1 = list(dicionario_dicionarios.keys())[0]
        dic1 = dicionario_dicionarios[chave1]
        titulos = list(dic1.keys())
        writer = csv.DictWriter(csvfile, delimiter=delimitador, fieldnames=titulos)
        writer.writeheader()
        for d in dicionario_dicionarios.values():
            writer.writerow(d)
