f = open('Carros_Donos/donos.txt', 'rt', encoding='utf-8')
linhas = f.readline()   # lê a 1º linha
linhas = f.readlines()  # lista em que cada elemento contém uma linha do ficheiro
f.close()
# print(linhas)


def ListarFuncoesAtributos(classe):
    print("Classe: ", classe)
    funcoes_atributos = dir (classe)
    for x in funcoes_atributos:
        if not x.startswith('__'):
            print(x)


print('funcoes_atributos = dir (str)')
funcoes_atributos = dir (str)
for x in funcoes_atributos:
    if not x.startswith('__'):
        print(x)

print ('vars(str):',vars(str))


lista = []
for x in linhas:
    x = x.rstrip('\n')
    print(x)
    lista.append(x)

nome = "RODOLFO PINHEIRO QUEIROS ARANTES"
print(nome.capitalize())
print(nome.upper())
print(nome.lower())
min_v = min(lista)
max_v = max(lista)
print('Min: ', min_v)
print('Max: ', max_v)

lista = [10, 20, 30,45, 8, 12, 90]
max_v = max(lista)
min_v = min(lista)
sum_v = sum(lista)
print('Min: ', min_v)
print('Max: ', max_v)
print('Sum: ', sum_v)

import seedir as sd
import os
sd.seedir(os.getcwd(), style='emoji')
# import os
# import seedir as sd
# os.system("del *.xml /s")
# os.system("del *.pyc /s")
# os.system("del *.iml /s")
# os.system("del .name /s")
# os.system("del .gitignore /s")
# os.system("del __pycache__ /s /q")
# sd.seedir(os.getcwd(), style='emoji')


import string
ListarFuncoesAtributos(str)
ListarFuncoesAtributos(string)
print(string.__all__)
print(str.__dict__)


def Display(x):
    temp = vars(x)
    for item in temp:
        print("%-25s : %s" % (item, temp[item]))

Display(str)


# Estatísticas com nomes:
#
# Nomes, Apelidos

#
# nome = 'Abel Cardoso Carraínho Nunes'
# v = nome.split(' ')
# nome1 = v[0]
# # apelido = v[len(v)-1]
# apelido = v[-1]
# print(nome1, apelido)
# exit()

f = open("nomes.txt", "rt", encoding='utf-8')
linhas = f.readlines()
f.close()
# print(linhas)
max = 0
nomes = []
apelidos = [[]]
for x in linhas:
    # x = x.rstrip('\n')
    # vetor = x.split('\t')
    # vetor = vetor[0:2]
    # nome, numero = vetor
    nome, numero = x.rstrip('\n').split('\t')[0:2]
    if len(nome) > 54:
        print(f"{nome:<54} {numero}")
    # --- max tamanho nome
    if len(nome) > max:
        max = len(nome)
    # ---------
    n1 = nome.split(' ')
    nome, apelido = n1[0], n1[-1]
    if nome in nomes:
        p = nomes.index(nome)
        apelidos[p].append(apelido)
    else:
        nomes.append(nome)
        apelidos.append([apelido])
print(max)
for i in range(len(nomes)):
    nome = nomes[i]
    apelido = apelidos[i]
    print(f"{nome:10} ({len(apelido):2}): {apelido}")

# for line in file:
#     output = line.title()


# 0) Quantidade de nomes
# 1) Nome com maior tamanho
# 2) Nome com menor tamanho
# 3) Quantidade de pessoas por nome, ex:
#     Ana: 350
#     Carlos: 30
# 4) Quantidade de pessoas por apelido, ex:
#     Silva: 2500
#     Gomes: 301
# 5) Quantidade de nomes por quantidade de palavras no nome()
#   2: 50
#   3: 120
#   4: 5233
#   5:
#   ...
# 6) Para cada nome (primeiro) obter todos os apelidos
#     Abel: Carvalho, Nunes, Pontes
#     Carla: Gomes, Silva
#
#
# nomes.txt
# Braima Mendes	1706441
# Maria Correia Ramos	1705821
# Mutlu	1704356
# Fernando Adai Gomes Indi	1706480
# Carvalho Vera Cruz	1012054
# ...


# -1) Obter lista de nomes (milhares)

# 0) Quantidade de nomes
# 1) Nome com maior tamanho
# 2) Nome com menor tamanho
# 3) Quantidade de pessoas por nome, ex:
#     Ana: 350
#     Carlos: 30
# 4) Quantidade de pessoas por apelido, ex:
#     Silva: 2500
#     Gomes: 301
# 5) Quantidade de nomes por quantidade de palavras no nome()
#   2: 50
#   3: 120
#   4: 5233
#   5:
#   ...
# 6) Para cada nome (primeiro) obter todos os apelidos
#     Abel: Carvalho, Nunes, Pontes
#     Carla: Gomes, Silva
#
#
# nomes.txt
# Braima Mendes	1706441
# Maria Correia Ramos	1705821
# Mutlu	1704356
# Fernando Adai Gomes Indi	1706480
# Carvalho Vera Cruz	1012054
def lerdados(nomeFicheiro):
    f = open(nomeFicheiro, "rt", encoding="UTF-8")
    linhas = f.readlines()
    f.close()
    # print(linhas)

    numeros_nomes = []
    for x in linhas:
        x = x.rstrip("\n")
        v = x.split("\t")
        nome, numero = v
        # print(f"{nome:<{60}} {numero}")
        numeros_nomes.append((numero, nome))
    return numeros_nomes


numeros_nomes = lerdados("Nomes.txt")

# 6) Para cada nome (primeiro) obter todos os apelidos
#     Abel: Carvalho, Nunes, Pontes
#     Carla: Gomes, Silva

def nomeapelidos(lista):
    apelidos = [[]]
    nomes = []
    for x in lista:
        #primeironome = x[1].split(" ")[0]
        #ultimonome = x[1].split(" ")[-1]
        n = x[1].split(" ")
        primeironome = n[0]
        ultimonome = n[-1]
        if primeironome in nomes:
            p = nomes.index(primeironome)
            if ultimonome not in apelidos[p]:
                apelidos[p].append(ultimonome)
        else:
            nomes.append(primeironome)
            apelidos.append([ultimonome])

    return list(zip(nomes, apelidos))
r = nomeapelidos(numeros_nomes)
r = sorted(r, key=lambda x: len(x[1]), reverse=True)
for x in r:
    print(x[0], len(x[1]),x[1])
print("Quantidade de Nomes diferentes:", len(r))

# print (numeros_nomes)

def tamanhonomemaior(lista):
    max = 0
    for x in lista:
        # x = ('1706441', 'Luis Braima Mendes'),
        if len(x[1]) > max:
            max = len(x[1])
    return max

max = tamanhonomemaior(numeros_nomes)
#print(max)

def nomemaior(lista):
    max = tamanhonomemaior(lista)
    maiores = []
    for x in lista:
        # x = ('1706441', 'Luis Braima Mendes'),
        if len(x[1]) == max:
            maiores.append(x)
    return maiores

nomesmaiores = nomemaior(numeros_nomes)
print(nomesmaiores)

def tamanhonomemenor(lista):
    min = 9999999
    for x in lista:
        # x = ('1706441', 'Luis Braima Mendes'),
        if len(x[1]) < min:
            min = len(x[1])
    return min

def nomemenor(lista):
    min = tamanhonomemenor(lista)
    menores = []
    for x in lista:
        # x = ('1706441', 'Luis Braima Mendes'),
        if len(x[1]) == min:
            menores.append(x)
    return menores

nomesmenores = nomemenor(numeros_nomes)
print(nomesmenores)

def pessoasxnome(lista):
    nomes = []
    qts = []
    for x in lista:
        primeironome = x[1].split(" ")[0]
        if primeironome in nomes:
            p = nomes.index(primeironome)
            qts[p] = qts[p]+1
        else:
            nomes.append(primeironome)
            qts.append(1)
    return list(zip(nomes, qts))

nomesqts = pessoasxnome(numeros_nomes)
t = 0
for x in nomesqts:
    print(x)
    t = t + x[1]
print("Quantidade de Nomes", len(numeros_nomes), "de", t)

nomesqts.sort()    #ordenar por nome + quantidade
#print(nomesqts)
ordenada = sorted(nomesqts)
print(ordenada)

def myFunc(e):
  return e[1]

ordenada = sorted(nomesqts, key=myFunc, reverse=True)
print(ordenada)

ordenada = sorted(nomesqts, key=lambda x: x[1], reverse=True)
print(ordenada)




