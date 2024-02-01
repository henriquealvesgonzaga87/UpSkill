lista_paises_capitais = {'Alemanha': 'Berlim', 'Áustria': 'Viena', 'Bélgica': 'Bruxelas',
                         'Bielorrússia': 'Minsk', 'Bulgária': 'Sofia', 'Chipre': 'Nicósia',
                         'Croácia': 'Zagreb', 'Dinamarca': 'Copenhague', 'Eslováquia': 'Bratislava',
                         'Espanha': 'Madrid', 'Finlândia': 'Helsinki', 'França': 'Paris', 'Grécia': 'Atenas',
                         'Hungria': 'Budapeste', 'Irlanda': 'Dublin', 'Itália': 'Roma', 'Letônia': 'Riga',
                         'Mônaco': 'Mônaco', 'Noruega': 'Oslo', 'Países Baixos': 'Amsterdão',
                         'Polônia': 'Varsóvia', 'Portugal': 'Lisboa', 'Tchéquia': 'Praga',
                         'Romênia': 'Bucareste', 'Sérvia': 'Belgrado', 'Suécia': 'Estocolmo',
                         'Suíça': 'Berna', 'Ucrânia': 'Kiev'}
qtde_perguntas = int(input("Quantas perguntas quer responder (0 a 28): "))
i = 0
for k, v in lista_paises_capitais.items():
    resposta = input(f"Qual é a capital de {k}: ").capitalize()
    if resposta == v:
        print("correto")
    else:
        print("errado")
    i += 1
    if i == qtde_perguntas:
        break
