# Conheça a sua nova componente de preço “Energia e Estrutura Comercial”
# Potência 10,35 kVA | Opção Bi-horária
# Energia e Estrutura Comercial Valor em vigor até
# 31 de dezembro de 2023
#
# Valor em vigor a partir de
# 1 de janeiro de 2024
#                               2023	2012
# Energia Vazio (€/kWh)         0.1847 0.1441
# Energia Fora de Vazio (€/kWh) 0.2256 0.1912
# Potência (€/dia)              0.0693 0.1112
#
# Cilindro para aquecimento de águas quentes.
# Potência 10,35 kVA | Opção Bi-horária:
# 08:00 - 22:00 - Horas cheias
# 22:00 - 08:00 - Horas vazio


preco_vazio = 0.1847
preco_cheias = 0.2256

potencia_necessaria = 1500  # W
producao_solar_f3 = 2200
producao_solar = producao_solar_f3 / 3
horas = 2
rede = potencia_necessaria - producao_solar
rede_necessaria = rede
if rede < 0:
	rede_necessaria = 0
else:
	rede_necessaria = rede

# com / sem iva
iva = 0.23
custo_dia = round(preco_cheias * horas * rede_necessaria / 1000, 3) * (1 + iva)
custo_noite = round(preco_vazio * horas * potencia_necessaria / 1000, 3) * (1 + iva)

if (custo_dia <= custo_noite):
	ligar = True
else:
	ligar = False

print(f"Necessidade   {potencia_necessaria:.2f}")
print(f"Produão Solar {producao_solar:.2f}")
print(f"Rede          {rede:.2f}")
print(f"Rede          {rede_necessaria:.2f}")

print(f"Custo dia     {custo_dia*100:.2f} cent.")
print(f"Custo noite   {custo_noite*100:.2f} cent.")
print(f"Ligar         {ligar}")

# qual o valor de produção solar para a qual compensa ligar o cilindro durante o dia?
# dia                       noite
pn = potencia_necessaria
# (pn-ps) * h * preco_cheias =  pn * h * preco_vazio
# (pn-ps)   =  (pn * h * preco_vazio) / (h * preco_cheias)
# -ps = (pn * h * preco_vazio) / (h * preco_cheias) - pn
ps = pn - (pn * horas * preco_vazio) / (horas * preco_cheias)
print(ps, ps * 3)
preco_cheias = preco_cheias * (1 + iva)
preco_vazio = preco_vazio * (1 + iva)
ps = pn - (pn * horas * preco_vazio) / (horas * preco_cheias)
print(ps, ps * 3)

# calcular poupanca: intervalo tempo: 1s, 1min, etc

