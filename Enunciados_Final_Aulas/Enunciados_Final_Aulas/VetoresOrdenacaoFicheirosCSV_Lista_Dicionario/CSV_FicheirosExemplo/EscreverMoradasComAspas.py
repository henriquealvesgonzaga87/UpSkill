import csv

from EscreverFicheiroCSV import *
from LerFicheiroCSV import *

# Nome;Morada;Codigo Postal
lista = [
    ('Instituto Politécnico da Guarda', 'Avenida Dr. Francisco Sá Carneiro, 50',
     '6300-559 Guarda'),
    ('Município da Guarda,Praça do Município', '6301-854 GUARDA'),
    ('Finanças de Guarda', 'Av. Monsenhor Mendes do Carmo, 13 r/c', '6300-586 Guarda')]

EscreverFicheiroCSV('moradas_aspas.csv',
                    ['Nome', 'Morada', 'Codigo Postal'],
                    lista,
                    delimitador=',',
                    aspas='"',
                    tipo_aspas=csv.QUOTE_ALL)

EscreverFicheiroCSV('moradas_aspas_v.csv',
                    ['Nome', 'Morada', 'Codigo Postal'],
                    lista,
                    delimitador=',',
                    aspas='|',
                    tipo_aspas=csv.QUOTE_ALL)

cab, lista = LerFicheiroCSV('moradas_aspas.csv', delimitador=',')
print(cab)
print(lista)
