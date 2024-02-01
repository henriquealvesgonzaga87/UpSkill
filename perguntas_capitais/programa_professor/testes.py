from perguntas_capitais.programa_professor.LerEscreverCSVDict import *
import random
from datetime import datetime
import pyttsx3

def narrador():
    engine = pyttsx3.init()
    vozes = engine.getProperty('voices')
    for voz in vozes:
        if "portugal" in voz.name.lower():
            engine.setProperty('voice', voz.id)
            break
    return engine
def falar(engine, texto):
    engine.say(texto)
    engine.runAndWait()

paises = []
lista = LerCSVParaListadeDicionarios("paises_geonames.com.txt.csv", delimitador='\t')

for d in lista:
    pais = d["Country"]
    capital_correta = d["Capital"]
    # Escolher 3 capitais incorretas aleatoriamente de outros países
    capitais_incorretas = random.sample([d["Capital"] for d in lista if d["Capital"] != capital_correta], 3)
    # Montar as opções com a capital correta e as incorretas
    opcoes = [(capital_correta, 1)] + [(capital, 0) for capital in capitais_incorretas]
    random.shuffle(opcoes)  # Misturar as opções
    paises.append((pais, opcoes))

def realizar_quiz(paises, tempo_maximo=10):
    engine = narrador()
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    SMQ = f"\t\t  Super Mega Quiz"
    falar(engine, SMQ)
    print(SMQ)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    num_perguntas = int(input("A quantas perguntas deseja responder? "))
    perguntas_selecionadas = random.sample(paises, num_perguntas)
    total_corretas = 0

    letras_opcoes = ['A', 'B', 'C', 'D']
    numquestao = 1
    for pais, opcoes in perguntas_selecionadas:
        pergunta = f"Qual é a capital do {pais}?"
        comprimento = len(pergunta)
        asteriscos = "*" *comprimento
        print("=================")
        questao = f"  Questão {numquestao} "
        print(questao)
        falar(engine, questao)
        print(asteriscos)
        print(pergunta)
        numquestao += 1
        falar(engine, pergunta)
        for indice in range(len(opcoes)):
            opcao = f"{letras_opcoes[indice]} - {opcoes[indice][0]}"
            print(opcao)
            falar(engine, opcao)

        inicio = datetime.now()#tempo inicial
        print(f"Tempo inicial: {inicio.strftime('%H:%M:%S')}")
        print("Atenção: Tem 10 segundos para responder à questão")
        resposta_utilizador = input("Resposta (A, B, C, D)? ").upper()
        fim = datetime.now()#tempo final
        duracao = (fim - inicio).total_seconds()#tempo usado
        print(f"Tempo: {duracao:.2f} segundos")

        letra_resposta_correta = None
        for indice in range(len(opcoes)):
            if opcoes[indice][1] == 1:
                letra_resposta_correta = letras_opcoes[indice]
                break

        resposta_correta = resposta_utilizador == letra_resposta_correta
        if duracao > tempo_maximo:
            print(f"A sua resposta {resposta_utilizador} está {'correta' if resposta_correta else 'incorreta'}.")
            print("No entanto, foi considerada incorreta por ter excedido o tempo máximo.")
        elif resposta_correta:
            print("Resposta correta!")
            total_corretas += 1
        else:
            print(f"Resposta incorreta! A resposta correta era {letra_resposta_correta}.")

    total_perguntas = len(perguntas_selecionadas)
    total_erradas = total_perguntas - total_corretas
    percentagem_corretas = (total_corretas / total_perguntas) * 100
    percentagem_erradas = (total_erradas / total_perguntas) * 100

    print(f"\nFim do quiz! Respondeu a {total_perguntas} perguntas.")
    print(f"Respostas corretas: {total_corretas} - {percentagem_corretas:.2f}%")
    print(f"Respostas erradas: {total_erradas} - {percentagem_erradas:.2f}%")

    return total_perguntas, total_corretas, total_erradas, percentagem_corretas, percentagem_erradas

def salvar_estatisticas_csv(nome_jogador, total_perguntas, total_corretas, total_erradas, percentagem_corretas, percentagem_erradas):

    with open("estatisticas_quiz.csv", "a", newline='', encoding='utf-8') as arquivo_csv:
        campos = ['Nome do Jogador', 'Total de Perguntas', 'Respostas Corretas', 'Respostas Erradas', 'Percentagem Corretas',
                  'Percentagem Erradas']
        escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)

        arquivo_csv.seek(0, 2)  # Verifica se é o final do arquivo
        if arquivo_csv.tell() == 0:  # Se o arquivo estiver vazio, escreve o cabeçalho
            escritor.writeheader()

        escritor.writerow({
            'Nome do Jogador': nome_jogador,
            'Total de Perguntas': total_perguntas,
            'Respostas Corretas': total_corretas,
            'Respostas Erradas': total_erradas,
            'Percentagem Corretas': f"{percentagem_corretas:.2f}%",
            'Percentagem Erradas': f"{percentagem_erradas:.2f}%"
        })

    print("Estatísticas salvas com sucesso!")

total_perguntas, total_corretas, total_erradas, percentagem_corretas, percentagem_erradas = realizar_quiz(paises)
nome_jogador = input("Por favor, insira o seu nome para guardar a sua pontuação: ")
salvar_estatisticas_csv(nome_jogador, total_perguntas, total_corretas, total_erradas, percentagem_corretas, percentagem_erradas)