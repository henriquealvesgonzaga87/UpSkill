from salario_funcao import *

#obter_horas()
#obter_salario()
#obter_numero_real("Salário hora: ", 5, 50)
horas = obter_numero_real('Nº de horas: ', 0, 240)
salario_base = obter_numero_real('Valor salário hora: ', 5, 50)
salario_bruto = salario_base * horas

if salario_bruto <= 900:
    taxa_irs = 0
elif salario_bruto <= 1500:
    taxa_irs = 5
elif salario_bruto <= 2500:
    taxa_irs = 10
else:
    taxa_irs = 20
irs = salario_bruto * (taxa_irs / 100)
seguranca_social = salario_bruto * 0.11
total_descontos = irs + seguranca_social
salario_liquido = salario_bruto - total_descontos
