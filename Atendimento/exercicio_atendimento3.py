from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_ALL, '')
cursos = {'TC': 'TESP CiberSegurança', 'LEI': 'Licenciatura em Engenharia Informática '}
disciplinas = {'PI': 'Programação para a Internet ', 'AED': 'Algoritmos e Estruturas de Dados '}
tipos = {'F': '* Frequência', 'E': '* Exame ', "R": '* Recurso ', 'ATM': 'Atendimento '}
resultado = {'curso': '', 'disciplina': '', 'data': '', 'hora_inicio': '', 'hora_fim': '', 'tipologia': ''}

datasTexto = [
    ('LCDIA', 'AA1', '02/02/2024 14:00', 'E'),
    ('LCDIA', 'AA1', '08/02/2024 10:00', 'R'),
    ('LEI', 'PI', '05/02/2024 17:00', 'E'),
    ('LEI', 'PI', '10/02/2024 10:00', 'R')
]

datasTexto1 = [
    ('LEI', 'EE', '17/01/2024 14:00', 'F'),
    ('LEI', 'EE', '03/02/2024 14:00', 'E'),
    ('LEI', 'EE', '14/02/2024 17:00', 'R'),
    ('MCM', 'RSC', '24/01/2024 14:00', 'F'),
    ('MCM', 'RSC', '02/02/2024 14:00', 'E'),
    ('MCM', 'RSC', '10/02/2024 11:00', 'R'),
    ('TESPC', 'RC2', '17/01/2024 14:00', 'E'),
    ('TESPC', 'RC2', '03/02/2024 14:00', 'F'),
    ('TESPC', 'RC2', '14/02/2024 14:00', 'R')
]


def data_dia_anterior(data, dias):
    data_anterior = data
    data_anterior -= timedelta(days=dias)
    return data_anterior


def verifica_data(data_anterior):
    verifica_data_anterior = int(datetime.strftime(data_anterior, '%w'))
    if verifica_data_anterior == 6:
        data_anterior -= timedelta(days=2)
    elif verifica_data_anterior == 0:
        data_anterior -= timedelta(days=2)
    return data_anterior


def verifica_dia_numeral_semana(dia):
    verifica_semana = int(datetime.strftime(dia, '%w'))
    return verifica_semana


def horario_atendimento(hora):
    if hora <= 12:
        hora_inicio = hora_exame - timedelta(hours=1)
    else:
        hora_inicio = hora_exame
    hora_final = hora_inicio + (timedelta(hours=3))
    return hora_final


db = datasTexto1
datas_atm = []
for i in db:
    tipo = i[3]
    get_data = i[2].split(' ')
    get_hora_exame = get_data[1].split(':')
    hora = int(get_hora_exame[0])
    hora_exame = timedelta(hours=int(get_hora_exame[0]), minutes=int(get_hora_exame[1]))
    if hora <= 12:
        hora_inicio_atendimento = hora_exame - timedelta(hours=1)
    else:
        hora_inicio_atendimento = hora_exame
    hora_final_atendimento = hora_inicio_atendimento + (timedelta(hours=3))
    hora_final_exame = hora_exame + timedelta(hours=2)

    data_exame = datetime.strptime(get_data[0], '%d/%m/%Y')
    verifica_data_exame = verifica_data(data_exame)
    verifica_dia_semana_exame = verifica_dia_numeral_semana(data_exame)

    data_anterior2 = data_dia_anterior(data_exame, 2)
    verifica_data_anterior2 = verifica_data(data_anterior2)
    verifica_dia_semana_atendimento2 = verifica_dia_numeral_semana(data_anterior2)

    data_anterior1 = data_dia_anterior(data_exame, 1)
    verifica_data_anterior1 = verifica_data(data_anterior1)
    verifica_dia_semana_atendimento1 = verifica_dia_numeral_semana(data_anterior1)

    if verifica_data_exame == verifica_data_anterior2:
        data_exame += timedelta(days=2)
        verifica_data_exame = verifica_data(data_exame)
        if hora_exame <= timedelta(hours=12):

            hora_inicio_atendimento = timedelta(hours=14, minutes=0)
            hora_final_atendimento = hora_inicio_atendimento + (timedelta(hours=3))
        else:
            hora_inicio_atendimento = timedelta(hours=9, minutes=0)
            hora_final_atendimento = hora_inicio_atendimento + (timedelta(hours=3))

    elif verifica_data_exame == verifica_data_anterior1:
        data_exame += timedelta(days=1)
        verifica_data_exame = verifica_data(data_exame)
        if hora_exame <= timedelta(hours=12):
            hora_inicio_atendimento = timedelta(hours=14, minutes=0)
            hora_final_atendimento = hora_inicio_atendimento + (timedelta(hours=3))
        else:
            hora_inicio_atendimento = timedelta(hours=9, minutes=0)
            hora_final_atendimento = hora_inicio_atendimento + (timedelta(hours=3))

    data_exame_formatada = datetime.strftime(verifica_data_exame, '%a %d/%m/%Y')

    data_anterior2_formatada = datetime.strftime(verifica_data_anterior2, '%a %d/%m/%Y')

    data_anterior1_formatada = datetime.strftime(verifica_data_anterior1, '%a %d/%m/%Y')

    datas_atm.append([
        i[0], i[1], data_anterior2_formatada, str(hora_inicio_atendimento), str(hora_final_atendimento), tipos['ATM']
                      ])
    datas_atm.append([
        i[0], i[1], data_anterior1_formatada, str(hora_inicio_atendimento), str(hora_final_atendimento), tipos['ATM']
                    ])
    datas_atm.append([i[0], i[1], data_exame_formatada, str(hora_exame), str(hora_final_exame), i[3]])

L = 10

lista_ordenada = sorted(datas_atm, key=lambda x: x[2])

for k in resultado.keys():
    print(k.ljust(L), end=' ' * L)
print()

for i, v in enumerate(lista_ordenada):
    for j in v:
        print(j.ljust(L), end=' ' * L)
    print()
