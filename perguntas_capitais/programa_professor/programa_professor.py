import time
from datetime import datetime
from perguntas_capitais.programa_professor.LerEscreverCSVDict import *
from LerGravarCSV import *
import random


nq = int(input("Digite a quantidade de questões que quer responder: "))
nome = input("Informe o seu nome: ").capitalize().strip()
data_hora_quiz = datetime.strftime(datetime.now(), '%d%m%Y %H%M')
nome_formatado = f"{nome} {data_hora_quiz}" + '.csv'
paises = []
lista = LerCSVParaListadeDicionarios("paises_geonames.com.txt.csv", delimitador="\t")
while True:
    n = random.randint(0, len(lista) - 1)
    p = lista[n]['Country']
    c = lista[n]['Capital']
    opcoes = [(c, 1)]
    while True:
        n = random.randint(0, len(lista) - 1)
        p2 = lista[n]['Country']
        c2 = lista[n]['Capital']
        if p != p2 and not (c2, 0) in opcoes:
            opcoes.append((c2, 0))
        if len(opcoes) == 4:
            break
    # escolher nomes de capitais 3 de todos (252) diferentes de c
    random.shuffle(opcoes)
    paises.append((p, opcoes))
    if nq == len(paises):
        break

for x in paises:
    print(x)


def Pergunta(inicio, np, p, a):
    dh = datetime.fromtimestamp(inicio)
    print(dh)
    p = f"Qual é a capital de {p}? "
    print(p)
    i = 0
    for c in 'ABCD':
        print(f"{c} - {a[i][0]}")
        i += 1
    return p


def Resposta():
    while True:
        r = input("Resposta (A, B, C, D): ").upper()
        if r in 'ABCD':
            return r


def VerificaResposta(a, r):
    for i in range(len(a)):
        if a[i][1] == 1:
            break
    # dic_pos_letra = {"": ""}
    if (r == 'A' and i == 0) or (r == 'B' and i == 1) or (r == 'C' and i == 2) or (r == 'D' or i == 3):
        return True, 'exc...'
    return False, ''


def Estatisticas(respostas):
    corretas = 0
    erradas = 0
    for r in respostas:
        if r[2] == True:
            corretas += 1
        else:
            erradas += 1
    pc = corretas / len(respostas) * 100
    pe = erradas / len(respostas) * 100
    return {'Corretas': corretas, 'Erradas': erradas, 'Perc_corretas': round(pc), 'Perc_Erradas': round(pe)}


respostas = []
i = 0
for p, a in paises:
    i += 1
    inicio = time.time()
    pergunta = Pergunta(inicio, i, p, a)
    r = Resposta()
    tempo = round(time.time() - inicio, 1)
    certa, obs = VerificaResposta(a, r)
    respostas.append((i, pergunta, certa, a, r, tempo, obs))
print(respostas)

titulos = ['N', 'Texto', 'Correta', 'Opçoes', 'Resposta', 'Tempo', 'Obs']
GravarListaEmFicheiroCSV(respostas, nome_formatado, delimitador=';', titulos=titulos)

print(Estatisticas(respostas))
