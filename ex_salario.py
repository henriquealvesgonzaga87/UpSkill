def obter_valor(msg, minimo, maximo):
    while True:
        try:
            valor = float(input(msg))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"O valor informado deve estar no intervalo de {minimo} a {maximo}")
        except:
            print(f"O valor deve ser um numero entre {minimo} e {maximo}")


horas_trabalhadas = obter_valor("Informe as horas trabalhadas: ", 0, 240)
valor_hora_salario = obter_valor("Informe o valor do salário em horas: ", 3, 200)
salario_bruto = horas_trabalhadas * valor_hora_salario
irs = 0
total_irs = 0
taxa_deducao = 0
taxa_iss = 11 / 100
total_iss = salario_bruto * taxa_iss

if 886.57 <= salario_bruto < 932.14:
    taxa_irs = 14.5
    taxa_deducao = (taxa_irs / 100) * 2.3 * (1093.31 - salario_bruto)
elif 932.14 <= salario_bruto < 999.14:
    taxa_irs = 21
    taxa_deducao = (taxa_irs / 100) * 2.3 * (1350.22 - salario_bruto)
elif 999.14 <= salario_bruto < 999.14:
    taxa_irs = 21
    taxa_deducao = 114.14
elif 999.14 <= salario_bruto < 1106.93:
    taxa_irs = 26.5
    taxa_deducao = 169.09
elif 1106.93 <= salario_bruto < 1600.36:
    taxa_irs = 28.5
    taxa_deducao = 191.23
elif 1600.36 <= salario_bruto < 1961.36:
    taxa_irs = 35
    taxa_deducao = 295.26
elif 1961.36 <= salario_bruto < 2529.05:
    taxa_irs = 37
    taxa_deducao = 334.48
elif 2529.05 <= salario_bruto < 3694.46:
    taxa_irs = 38.72
    taxa_deducao = 377.86
elif 3694.46 <= salario_bruto < 5469.90:
    taxa_irs = 40.05
    taxa_deducao = 427.18
elif 5469.90 <= salario_bruto < 6420.55:
    taxa_irs = 42.72
    taxa_deducao = 573.22
elif 6420.55 <= salario_bruto < 20064.21:
    taxa_irs = 44.95
    taxa_deducao = 716.08
elif salario_bruto >= 20064.21:
    taxa_irs = 47.17
    taxa_deducao = 1162.51
else:
    taxa_irs = 0

irs = salario_bruto * (taxa_irs / 100)
total_irs = irs - taxa_deducao
total_descontos = total_irs + total_iss
salario_liquido = salario_bruto - total_descontos
L = 25
T = 8
if salario_bruto >= 1E5:
    T = 10
print("=" * (L + T))
print(f"Salário bruto".ljust(L, '.') + ":", f"{salario_bruto:{T},.2f}€")
print(f"Horas {horas_trabalhadas} x valor horas {valor_hora_salario}".ljust(L, '.'))
print("-" * (L + T))
print(f"IRS marginal({taxa_irs}%)".ljust(L, '.') + ":", f"{irs:{T},.2f}€")
print(f"Parcela a abater".ljust(L, '.') + ":", f"{taxa_deducao:{T},.2f}€")
print(f"IRS ({taxa_irs})".ljust(L, '.') + ":", f"{total_irs:{T},.2f}€")
print(f"ISS ({taxa_iss})".ljust(L, '.') + ":", f"{total_iss:{T},.2f}€")
print(f"Total Descontos".ljust(L, '.') + ":", f"{total_descontos:{T},.2f}€")
print("-" * (L + T))
print(f"Salário Liquído".ljust(L, '.') + ":", f"{salario_liquido:{T},.2f}€")
print("=" * (L + T))
