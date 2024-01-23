# Resultado: Qualidade do ar ('BOA', 'REGULAR', ...)
# Dados: PTS - particulas do ar
# caso 1: pts = 377 - qualidade ?
qualidade_ar = ''
particulas_suspensas = float(input("Particulas em suspensão (ug/m3): "))
while particulas_suspensas < 0:
    particulas_suspensas = float(input("Particulas em suspensão (ug/m3): "))
if particulas_suspensas <= 40:
    qualidade_ar = 'BOA'
elif particulas_suspensas <= 120:
    qualidade_ar = 'REGULAR'
elif particulas_suspensas <= 375:
    qualidade_ar = 'INADEQUADA'
elif particulas_suspensas <= 625:
    qualidade_ar = 'MÁ'
elif particulas_suspensas <= 875:
    qualidade_ar = 'PÉSSIMA'
else:
    qualidade_ar = 'CRÍTICA'
print(f"Com {particulas_suspensas:.2f} ug/m3 a qualidade do ar está {qualidade_ar}")
