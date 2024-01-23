hipotermias = ["leve", "moderada", "grave"]
sintomas = [
            "sensação de frio, tremor, diminuição da atividade motora",
            "prostado, sonolento, quase inconciente",
            "a pessoa fica quase inconciente e imóvel"
]
temperatura_minima = 0
temperatura_maxima = 35
situacao_pessoa = []
while True:
    try:
        temperatura_pessoa = float(input(
            f"Informe a temperatura da pessoa entre {temperatura_minima}º e {temperatura_maxima}º: "))
        if temperatura_minima <= temperatura_pessoa <= temperatura_maxima:
            break
        else:
            print(f"O valor deve ser entre {temperatura_minima}º e {temperatura_maxima}º")
    except:
        print(f"Valor inválido. Deve ser um número entre {temperatura_minima} e {temperatura_maxima}")

if temperatura_pessoa <= 30:
    situacao_pessoa.append(hipotermias[2])
    situacao_pessoa.append(sintomas[0])
    situacao_pessoa.append(sintomas[1])
elif temperatura_pessoa <= 33:
    situacao_pessoa.append(hipotermias[1])
    situacao_pessoa.append(sintomas[2])
    situacao_pessoa.append(sintomas[3])
    situacao_pessoa.append(sintomas[4])
else:
    situacao_pessoa.append(hipotermias[0])
    situacao_pessoa.append(sintomas[5])
    situacao_pessoa.append(sintomas[6])
