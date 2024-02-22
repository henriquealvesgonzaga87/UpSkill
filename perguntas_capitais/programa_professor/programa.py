import time
from datetime import datetime
from perguntas_capitais.programa_professor.LerEscreverCSVDict import *
from LerGravarCSV import *
import random
import pyttsx3
import statistics


engine = pyttsx3.init()
nq = int(input("Digite a quantidade de questões que quer responder: "))
nome = input("Informe o seu nome: ").capitalize().strip()
MAX_TEMPO = 10
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

# for x in paises:
#     print(x)


def Pergunta(inicio, np, p, a):
    dh = datetime.fromtimestamp(inicio)
    print(dh)
    p = f"Qual é a capital de {p}? "
    print(p)
    engine.say(p)
    engine.runAndWait()
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


def VerificaResposta(a, r, tempo):
    for i in range(len(a)):
        if a[i][1] == 1:
            break
    # dic_pos_letra = {"": ""}
    if (r == 'A' and i == 0) or (r == 'B' and i == 1) or (r == 'C' and i == 2) or (r == 'D' or i == 3):
        if tempo > MAX_TEMPO:
            return False, f'Errada por limite de tempo {MAX_TEMPO}'
        else:
            return True, ''
    else:
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
tempos = []
tempos_corretas = []
tempos_erradas = []
i = 0
for p, a in paises:
    i += 1
    inicio = time.time()
    pergunta = Pergunta(inicio, i, p, a)
    r = Resposta()
    tempo = round(time.time() - inicio, 1)
    certa, obs = VerificaResposta(a, r, tempo)
    respostas.append((i, pergunta, certa, a, r, tempo, obs))
    tempos.append(tempo)
    if certa:
        tempos_corretas.append(tempo)
    else:
        tempos_erradas.append(tempo)
print(respostas)

titulos = ['N', 'Texto', 'Correta', 'Opçoes', 'Resposta', 'Tempo', 'Obs']
GravarListaEmFicheiroCSV(respostas, nome_formatado, delimitador=';', titulos=titulos)

print(Estatisticas(respostas))

e = Estatisticas(respostas)
tmin = min(tempos)
tmax = max(tempos)
tmean = statistics.mean(tempos)
e['tempo_mínimo'] = tmin
e['tempo_maximo'] = tmax
e['tempo_medio'] = tmean

if len(tempos_corretas) >= 1:
    tmin = min(tempos_corretas)
    tmax = max(tempos_corretas)
    tmean = statistics.mean(tempos_corretas)
    e['tempo_mínimo'] = tmin
    e['tempo_maximo'] = tmax
    e['tempo_medio'] = tmean
else:
    tmin = min(tempos_corretas)
    tmax = max(tempos_corretas)
    tmean = statistics.mean(tempos_corretas)
    e['tempo_mínimo'] = 0
    e['tempo_maximo'] = 0
    e['tempo_medio'] = 0

if len(tempos_erradas) >= 1:
    tmin = min(tempos_erradas)
    tmax = max(tempos_erradas)
    tmean = statistics.mean(tempos_erradas)
    e['tempo_mínimo'] = tmin
    e['tempo_maximo'] = tmax
    e['tempo_medio'] = tmean
else:
    tmin = min(tempos_erradas)
    tmax = max(tempos_erradas)
    tmean = statistics.mean(tempos_erradas)
    e['tempo_mínimo'] = 0
    e['tempo_maximo'] = 0
    e['tempo_medio'] = 0

lista_dicionario = [e]
GravarListaDeDicionarioCSV(lista_dicionario, nome_formatado, delimitador=';')
