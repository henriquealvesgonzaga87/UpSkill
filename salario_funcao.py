def obter_horas():
    horas_minimas = 0
    horas_maximas = 240
    while True:
        try:
            horas = float(input("Nº de horas durante o mês: "))
            if horas_minimas <= horas <= horas_maximas:
                print(f"horas: {horas:.2f}")
                break
            else:
                print(f"O número de horas deve ser entre {horas_minimas} e de {horas_maximas}")
        except:
            print(f"Deve ser um número entre {horas_minimas} e {horas_maximas}")


def obter_salario():
    salario_minimo = 5
    salario_maximo = 50
    while True:
        try:
            salario_hora = float(input("Valor do salário hora: "))
            if salario_minimo <= salario_hora <= salario_maximo:
                print(f"valor: ${salario_hora:.2f}")
                break
            else:
                print(f"O valor deve ser entre {salario_minimo} e de {salario_maximo}")
        except:
            print(f"Deve ser um número entre {salario_minimo} e {salario_maximo}")


# solução professor


def obter_numero_real(msg, min, max):
    while True:
        try:
            numero = float(input(msg))
            if min <= numero <= max:
                return numero
            else:
                print(f"O valor deve estar entre {min} e {max}")
        except:
            print(f"deve digitar um número entre {min} e {max}")


obter_salario()
