import random
lista_paises_capitais = {'Alemanha': 'Berlim', 'Áustria': 'Viena', 'Bélgica': 'Bruxelas',
                         'Bielorrússia': 'Minsk', 'Bulgária': 'Sofia', 'Chipre': 'Nicósia',
                         'Croácia': 'Zagreb', 'Dinamarca': 'Copenhague', 'Eslováquia': 'Bratislava',
                         'Espanha': 'Madrid', 'Finlândia': 'Helsinki', 'França': 'Paris', 'Grécia': 'Atenas',
                         'Hungria': 'Budapeste', 'Irlanda': 'Dublin', 'Itália': 'Roma', 'Letônia': 'Riga',
                         'Mônaco': 'Mônaco', 'Noruega': 'Oslo', 'Países Baixos': 'Amsterdão',
                         'Polônia': 'Varsóvia', 'Portugal': 'Lisboa', 'Tchéquia': 'Praga',
                         'Romênia': 'Bucareste', 'Sérvia': 'Belgrado', 'Suécia': 'Estocolmo',
                         'Suíça': 'Berna', 'Ucrânia': 'Kiev'}

# pais = random.choice(list(lista_paises_capitais.keys()))

def verifica_resposta(resposta_user, resposta):
    quantidade_respostas_corretas = 0
    quantidade_respostas_incorretas = 0
    if resposta_user == resposta:
        quantidade_respostas_corretas += 1
        print("Correto")
    else:
        quantidade_respostas_incorretas += 1
        print("Incorreto")
    return quantidade_respostas_corretas, quantidade_respostas_incorretas


def gera_quiz(quantidade_perguntas, lista_capitais):
    paises = []
    respostas = []
    resposta_user = ''
    for i in range(quantidade_perguntas):
        opcao_resposta = random.choice(list(lista_capitais.items()))
        pais = opcao_resposta[0]
        resposta = opcao_resposta[1]
        if pais not in paises:
            paises.append(pais)
        respostas.append(resposta)
        for j in range(3):
            respostas.append(random.choice(list(lista_paises_capitais.values())))
        random.shuffle(respostas)
        print(paises)
        print(respostas)
        pergunta_ao_user = f"Qual é a capital do país {pais}?"
        print(pergunta_ao_user)
        opcoes = f"""{respostas[0]}
{respostas[1]}
{respostas[2]}
{respostas[3]}"""
        print(opcoes)
        resposta_user = input("Sua resposta: ").capitalize()
        respostas.clear()
        check_resposta = verifica_resposta(resposta_user, resposta)
    print(check_resposta)
    return resposta_user, check_resposta


quiz = gera_quiz(2, lista_paises_capitais)

