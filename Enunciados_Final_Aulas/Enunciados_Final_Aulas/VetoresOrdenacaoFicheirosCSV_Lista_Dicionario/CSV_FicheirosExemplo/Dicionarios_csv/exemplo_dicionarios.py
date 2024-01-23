dados = [(1, 'Ana Catarina de Jesus Sandes') ,
(2, 'Daniela de Morais Furtado Patrício') ,
(3, 'João Carlos Frazão Lopes') ,
(4, 'João Paulo Gomes Baptista Afonso') ,
(5, 'José Luis Moço Rodrigues') ,
(6, 'Miguel Ângelo Moura Salah') ,
(7, 'Mohamed Ben Pereira') ,
(8, 'Pedro Alexandre Passinha Nunes') ,
(9, 'Ricardo Alexandre Neta Gonçalves Martins') ,
(10, 'Ricardo Miguel Garcia Freire') ,
(11, 'Sandro Manuel Martins Duarte') ,
(12, 'Tiago Daniel Silva Andrade') ,
(13, 'Tiago dos Santos Henriques') ,
(14, 'Tiago Nuno da Silva Gonçalves') ,
(15, 'Vital Pedro Ferreira da Cruz Santos')
]
# generate random floating point values
from random import seed
import random
seed(13)
n = len(dados)

import csv

csvfile = open('nomes.csv', 'w', newline='')
writer = csv.writer(csvfile, delimiter=';') # , quotechar='|', quoting=csv.QUOTE_MINIMAL)

csvfile_dic = open('nomes_dic.csv', 'wt', newline='', encoding='utf-8')
fieldnames = ['Número', 'Nome']
writer_dic = csv.DictWriter(csvfile_dic, fieldnames=fieldnames)
writer_dic.writeheader()
for i in range(n):
    r1 = dados[i % n ]
    r2 = dados[(i+1) % n ]
    nomes1 = r1[1].split(' ')
    nomes2 = r2[1].split(' ')
    nome = nomes2[0:1] + nomes1[-2:-1]     # lista
    nome = ' '.join(nome)               # string
    tel = random.randint(911111111, 969999999)
    num = r1[0]
    writer.writerow((num, nome))  # csv
    writer_dic.writerow({'Número': num, 'Nome': nome}) # dic, csv
    nome = nomes1[0:-1] + nomes2[-1:]     # lista
    nome = ' '.join(nome)
    print((num, nome), ',')


csvfile.close()
csvfile_dic.close()

csvfile = open('nomes.csv', 'r', newline='')
reader = csv.reader(csvfile, delimiter=';')
for i in range(n):
    for row in reader:
        print(row)
csvfile.close()

# dic
print ("dic" * 10)
csvfile_dic = open('nomes_dic.csv', 'r', newline='', encoding='utf-8')
reader = csv.DictReader(csvfile_dic)
for i in range(n):
    for row in reader:
        print(row["Número"], row["Nome"])
csvfile.close()


