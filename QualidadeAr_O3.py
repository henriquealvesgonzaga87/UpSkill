while True:
    particulas_suspensas = float(input("Particulas em suspensão (ug/m3): "))
    if 0 <= particulas_suspensas <= 10000:
        if particulas_suspensas <= 20:
            qualidade_ar_pm = 'MUITO BOM'
        elif particulas_suspensas <= 35:
            qualidade_ar_pm = 'BOM'
        elif particulas_suspensas <= 50:
            qualidade_ar_pm = 'MÉDIO'
        elif particulas_suspensas <= 100:
            qualidade_ar_pm = 'FRACO'
        else:
            qualidade_ar_pm = 'MAU'
        break
    else:
        print("O valor inserido deve ser entre 0 e 10.000")


while True:
    ozonio = float(input("Informe o O3: "))
    if 0 <= ozonio <= 10000:
        if ozonio <= 80:
            qualidade_ar_oz = 'MUITO BOM'
        elif ozonio <= 100:
            qualidade_ar_oz = 'BOM'
        elif ozonio <= 180:
            qualidade_ar_oz = 'MÉDIO'
        elif ozonio <= 240:
            qualidade_ar_oz = 'FRACO'
        else:
            qualidade_ar_oz = 'MAU'
        break
    else:
        print("O valor inserido deve ser entre 0 e 10.000")

qualidade_ar = ''

if qualidade_ar_oz == 'MAU':
    qualidade_ar = qualidade_ar_oz
elif qualidade_ar_pm == 'MAU':
    qualidade_ar = qualidade_ar_pm
else:
    if qualidade_ar_pm == 'FRACO' or qualidade_ar_oz == 'FRACO':
        qualidade_ar = 'FRACO'
    elif qualidade_ar_pm == 'MÉDIO' or qualidade_ar_oz == 'MÉDIO':
        qualidade_ar = 'MÉDIO'
    elif qualidade_ar_pm == 'BOM' or qualidade_ar_oz == 'BOM':
        qualidade_ar = 'BOM'
    else:
        qualidade_ar = 'MUITO BOM'

print(f'''
Partículas suspensas: {particulas_suspensas} ug/m3
Ozônio: {ozonio} ug/m3
Qualidade do ar: {qualidade_ar}''')
