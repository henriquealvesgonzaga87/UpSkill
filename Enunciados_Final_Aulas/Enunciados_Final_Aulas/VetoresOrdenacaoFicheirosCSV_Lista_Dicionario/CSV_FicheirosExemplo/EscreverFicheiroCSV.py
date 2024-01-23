import csv

def EscreverFicheiroCSV(nome_ficheiro, cabecalhos, lista, delimitador=';', aspas='"', tipo_aspas=csv.QUOTE_MINIMAL):
    # csv.writer(csvfile, dialect='excel', **fmtparams)
    with open(nome_ficheiro, 'wt', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=delimitador, quotechar=aspas, quoting=tipo_aspas)
        writer.writerow(cabecalhos)
        writer.writerows(lista)
        # for r in lista:
        #     writer.writerow(r)


lista = [
    ('Instituto Politécnico da Guarda', 'Avenida Dr. Francisco Sá Carneiro, 50',
     '6300-559 Guarda'),
    ('Município da Guarda,Praça do Município', '6301-854 GUARDA'),
    ('Finanças de Guarda', 'Av. Monsenhor Mendes do Carmo, 13 r/c', '6300-586 Guarda')]

EscreverFicheiroCSV('moradas_aspas_esc.csv',
                    ['Nome', 'Morada', 'Codigo Postal'], lista)
