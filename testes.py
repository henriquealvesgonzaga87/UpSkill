from datetime import datetime, timedelta, time
import locale

locale.setlocale(locale.LC_ALL, '')
# Dicionário: {'chave ' : 'valor ', ... }
cursos = {'TC': 'TESP CiberSegurança', 'LEI': 'Licenciatura em Engenharia Informática'}
disciplinas = {'PI': 'Programação para a Internet', 'AED': 'Algoritmos e Estruturas de Dados'}
tipos = {'F': '* Frequência', 'E': '* Exame', "R": '* Recurso', 'ATM': 'Atendimento'}
resultado = {'curso': '', 'disciplina': '', 'data': '', 'hora_inicio': '', 'hora_fim': '', 'tipologia': ''}

datasTexto = [
    ('TC', 'PI', '18/01/2024 10:00', 'F'),
    ('TC', 'PI', '29/01/2024 10:00', 'E'),
    ('TC', 'PI', '07/02/2024 14:00', 'R'),
    ('LEI', 'AED', '19/01/2024 10:00', 'F'),
    ('LEI', 'AED', '02/02/2024 14:00', 'E'),
    ('LEI', 'AED', '09/02/2024 10:00', 'R')
]


def data_dia_anterior(data, dias):
    data_anterior = data
    data_anterior -= timedelta(days=dias)
    if data_anterior.weekday() == 6:
        data_anterior -= timedelta(days=2)
    elif data_anterior.weekday() == 0:
        data_anterior -= timedelta(days=2)
    return data_anterior


def linha(cur, dis, d, tipo_ext):
    if tipo_ext <= 'Atendimento':
        if d.hour <= 12:
            d = datetime.combine(d.date(), time(9, 0))
        else:
            d = datetime.combine(d.date(), time(14, 0))
    dd = datetime.strftime(d, '%a %d/%m/%Y')
    das = datetime.strftime(d, '%H:%M')
    d += timedelta(hours=3)
    ate = datetime.strftime(d, '%H:%M')
    return [cur, dis, dd, das, ate, tipo_ext]


def datas_atendimeto(datasTexto):
    lista = []
    for cur, dis, datas_s, tipo in datasTexto:
        data = datetime.strptime(datas_s, '%d/%m/%Y %H:%M')
        d2 = data_dia_anterior(data, 2)
        d1 = data_dia_anterior(data, 1)
        lista.append(linha(cur, dis, d2, tipos['ATM']))
        lista.append(linha(cur, dis, d1, tipos['ATM']))
        lista.append(linha(cur, dis, data, tipos[tipo]))
    return sorted(lista, key=lambda x: datetime.strptime(x[2] + ' ' + x[3], '%a %d/%m/%Y %H:%M'))


def escrever_lista(lista):
    print(f"{'Curso':5} {'Disciplina':10} {'Dia':14} {'Das':5} {'ás':5} {'Tipo'}")
    for cur, dis, dd, das, ate, tipo_ext in lista:
        print(f"{cur:5} {dis:10} {dd:14} {das:5} {ate:5} {tipo_ext}")
        d_ava = datetime.strptime(dd + ' ' + das, '%a %d/%m/%Y %H:%M')


def ajustar_horas(lista):
    for i in range(len(lista)):
        cur, dis, dd, das, ate, tipo_ext = lista[i]
        if tipo_ext != 'Atendimento':
            print(cur, dis, dd, das, ate, tipo_ext)
            d_ava = datetime.strptime(dd + ' ' + das, '%a %d/%m/%Y %H:%M')
            for j in range(i-1):
                cur2, dis2, dd2, das2, ate2, tipo_ext2 = lista[j]
                d2 = datetime.strptime(dd2 + ' ' + das2, '%a %d/%m/%Y %H:%M')
                if colidem(d_ava, d2):
                    if d2.hour <= 12:
                        d2 = datetime.combine(d2.date(), time(14, 0))
                    else:
                        d2 = datetime.combine(d2.date(), time(9, 0))
                    nova_linha = linha(cur2, dis2, d2, tipos['ATM'])
                    lista[j] = nova_linha
    return lista


def colidem(d1, d2):
    if d1.date() == d2.date():
        ini1 = d1.hour
        fim1 = d1.hour + 2
        ini2 = d2.hour
        fim2 = d2.hour + 2
        col = False
        if ini1 >= ini2 and ini1 <= fim2:
            col = True
        return col


lista = datas_atendimeto(datasTexto)
escrever_lista(lista)


#
# datas_atm = []
# for i in datasTexto:
#     get_data = i[2].split(' ')
#     get_hora_exame = get_data[1].split(':')
#     hora = int(get_hora_exame[0])
#     hora_exame = timedelta(hours=int(get_hora_exame[0]), minutes=int(get_hora_exame[1]))
#     if hora <= 12:
#         hora_inicio_atendimento = hora_exame - timedelta(hours=1)
#     else:
#         hora_inicio_atendimento = hora_exame
#     hora_final_atendimento = hora_inicio_atendimento + (timedelta(hours=3))
#     hora_final_exame = hora_exame + timedelta(hours=2)
#     data_exame = datetime.strptime(get_data[0], '%d/%m/%Y')
#     data_exame_formatada = datetime.strftime(data_exame, '%a %d/%m/%Y')
#     data_anterior2 = data_dia_anterior(data_exame, 2)
#     data_anterior2_formatada = datetime.strftime(data_anterior2, '%a %d/%m/%Y')
#     data_anterior1 = data_dia_anterior(data_exame, 1)
#     data_anterior1_formatada = datetime.strftime(data_anterior1, '%a %d/%m/%Y')
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
