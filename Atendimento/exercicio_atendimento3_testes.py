from datetime import datetime, timedelta, time
import locale

locale.setlocale(locale.LC_ALL, '')
# Dicionário: {'chave ' : 'valor ', ... }
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
    ('TESPC', 'RC2', '03/02/20024 14:00', 'F'),
    ('TESPC', 'RC2', '14/02/2024 14:00', 'R')
]


def cria_hora_inicio_exame(lista):
    for i in lista:
        get_data = i[2].split(' ')
        get_hora_exame = get_data[1].split(':')
        # hora = int(get_hora_exame[0])
        hora_exame = timedelta(hours=int(get_hora_exame[0]), minutes=int(get_hora_exame[1]))
        return [hora_exame]


def cria_hora_inicio_atendimento(hora):
    if hora <= 12:
        hora_inicio = hora - timedelta(hours=1)
    else:
        hora_inicio = hora
    return hora_inicio


def cria_hora_final_atendimento(hora_inicio_atm):
    hora_final_atm = hora_inicio_atm + (timedelta(hours=3))
    return hora_final_atm


def cria_hora_final_exame(hora_inicio_ex):
    hora_final_ex = hora_inicio_ex + timedelta(hours=2)
    return hora_final_ex


def data_dia_anterior(data, dias):
    data_anterior = data
    data_anterior -= timedelta(days=dias)
    return data_anterior


def cria_data_exame(data):
    verifica_data_exame = int(datetime.strftime(data, '%w'))
    if verifica_data_exame == 6:
        data -= timedelta(days=2)
    elif verifica_data_exame == 0:
        data -= timedelta(days=2)
    return data


def formata_data(data):
    data = datetime.strftime(data, '%a %d/%m/%Y')
    return data


db = datasTexto


datas_atm = []
# for i in datasTexto:
#     get_data = i[2].split(' ')
#     get_hora_exame = get_data[1].split(':')
#     hora = int(get_hora_exame[0])
#     hora_exame = timedelta(hours=int(get_hora_exame[0]), minutes=int(get_hora_exame[1]))
hora_exame = cria_hora_inicio_exame(datasTexto)
hora_inicio_atendimento = cria_hora_inicio_atendimento(hora=hora_exame)
hora_final_atendimento = cria_hora_final_atendimento(hora_inicio_atendimento)
hora_final_exame = cria_hora_final_exame(hora_exame)
print(hora_exame, hora_final_exame, hora_inicio_atendimento, hora_final_atendimento)
#
#     data_exame = datetime.strptime(get_data[0], '%d/%m/%Y')
#     data_exame_formatada = cria_data_exame(data_exame)
#     verifica_data_exame = int(datetime.strftime(data_exame, '%w'))
#     if verifica_data_exame == 6:
#         data_exame -= timedelta(days=2)
#     elif verifica_data_exame == 0:
#         data_exame -= timedelta(days=2)
#     data_exame_formatada = datetime.strftime(data_exame, '%a %d/%m/%Y')
#
#     data_anterior2 = data_dia_anterior(data_exame, 2)
#     verifica_data_anterior2 = int(datetime.strftime(data_anterior2, '%w'))
#     if verifica_data_anterior2 == 6:
#         data_anterior2 -= timedelta(days=2)
#     elif verifica_data_anterior2 == 0:
#         data_anterior2 -= timedelta(days=2)
#     data_anterior2_formatada = datetime.strftime(data_anterior2, '%a %d/%m/%Y')
#
#     data_anterior1 = data_dia_anterior(data_exame, 1)
#     verifica_data_anterior1 = int(datetime.strftime(data_anterior1, '%w'))
#     if verifica_data_anterior1 == 6:
#         data_anterior1 -= timedelta(days=2)
#     elif verifica_data_anterior1 == 0:
#         data_anterior1 -= timedelta(days=2)
#     data_anterior1_formatada = datetime.strftime(data_anterior1, '%a %d/%m/%Y')
#
#     datas_atm.append([
#         i[0], i[1], data_anterior2_formatada, str(hora_inicio_atendimento), str(hora_final_atendimento), tipos['ATM']
#                       ])
#     datas_atm.append([
#         i[0], i[1], data_anterior1_formatada, str(hora_inicio_atendimento), str(hora_final_atendimento), tipos['ATM']
#                     ])
#     datas_atm.append([i[0], i[1], data_exame_formatada, str(hora_exame), str(hora_final_exame), i[3]])
#
# L = 10
#
# for k in resultado.keys():
#     print(k.ljust(L), end=' ' * L)
# print()
#
# for i, v in enumerate(datas_atm):
#     for j in v:
#         print(j.ljust(L), end=' ' * L)
#     print()
