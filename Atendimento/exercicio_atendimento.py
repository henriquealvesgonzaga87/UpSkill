from datetime import datetime, timedelta, time
import locale


locale.setlocale(locale.LC_ALL, '')
# Dicionário: {'chave ' : 'valor ', ... }
cursos = {'TC': 'TESP CiberSegurança', 'LEI': 'Licenciatura em Engenharia Informática '}
disciplinas = {'PI': 'Programação para a Internet ', 'AED': 'Algoritmos e Estruturas de Dados '}
dic = {'F': '* Frequência', 'E': '* Exame ', "R": '* Recurso ', 'ATM': 'Atendimento '}
resultado = {'curso': '', 'disciplina': '', 'data': '', 'hora_inicio': '', 'hora_fim': '', 'tipo_atendimento': ''}

datasTexto = [
    ('TC', 'PI', '18/01/2024 10:00', 'F'),
    ('TC', 'PI', '29/01/2024 10:00', 'E'),
    ('TC', 'PI', '07/02/2024 14:00', 'R'),
    ('LEI', 'AED', '19/01/2024 10:00', 'F'),
    ('LEI', 'AED', '02/02/2024 14:00', 'E'),
    ('LEI', 'AED', '09/02/2024 10:00', 'R')
]

L = 10

for k in resultado.keys():
    print(k.ljust(L), end=' ' * L)
print()

for i, v in enumerate(datasTexto):
    data = v[2].split(' ')
    get_hora = data[1].split(':')
    hora = int(get_hora[0])
    minuto = int(get_hora[1])
    curso = v[0]
    disciplina = v[1]
    tipo = v[3]
    get_data = datetime.strptime(data[0], '%d/%m/%Y')
    data_exame = datetime.strftime(get_data, '%a %d-%m-%Y')
    hora_exame = timedelta(hours=hora, minutes=minuto)
    data_atendimento1 = get_data - timedelta(days=2)
    data_formatada_atendimento1 = datetime.strftime(data_atendimento1, '%a %d-%m-%Y')
    if hora <= 12:
        hora_inicio_atendimento1 = timedelta(hours=hora, minutes=minuto - 60)
    else:
        hora_inicio_atendimento1 = timedelta(hours=hora, minutes=minuto)
    hora_inicio_atendimento1_formatada = str(hora_inicio_atendimento1)
    data_atendimento2 = get_data - timedelta(days=1)
    data_formatada_atendimento2 = datetime.strftime(data_atendimento2, '%a %d-%m-%Y')
    hora_final_atendimento1 = hora_inicio_atendimento1 + timedelta(hours=3)
    hora_final_atendimento1_formatada = str(hora_final_atendimento1)
    hora_final_exame = hora_exame + timedelta(hours=2)
    resultado['curso'] = curso
    resultado['disciplina'] = disciplina
    resultado['data'] = data_formatada_atendimento1
    resultado['hora_inicio'] = hora_inicio_atendimento1_formatada
    resultado['hora_fim'] = hora_final_atendimento1_formatada
    resultado['tipo_atendimento'] = tipo

print(resultado)
