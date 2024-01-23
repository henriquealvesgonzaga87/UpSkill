pontos = 0
sim = "sim"
nao = "nao"
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]
for i in perguntas:
    while True:
        try:
            print(i)
            resposta = input("Sim ou nao para as perguntas: ").lower().strip()
            while resposta != sim and resposta != nao:
                print(i)
                resposta = input("Sim ou nao para as perguntas: ").lower().strip()
            if resposta == sim:
                pontos += 1
                break
            elif resposta == nao:
                break
            if resposta != sim or resposta != nao:
                print(f"A sua resposta deve ser {sim} ou {nao}")
        except:
            print(f"A sua resposta é inválida, deve ser {sim} ou {nao}")

if pontos == 2:
    situacao_pessoa = 'Suspeita'
elif 3 <= pontos <= 4:
    situacao_pessoa = "Cúmplice"
elif pontos == 5:
    situacao_pessoa = "Assassina"
else:
    situacao_pessoa = "Inocente"
print(f"Com as respostas dadas, foram acmuludados {pontos} pontos e a pessoa é considerada {situacao_pessoa}")
