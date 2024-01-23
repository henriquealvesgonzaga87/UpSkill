from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_ALL, '')
# Dicionário: {'chave ' : 'valor ', ... }
cursos = {'TC': 'TESP CiberSegurança', 'LEI': 'Licenciatura em Engenharia Informática '}
disciplinas = {'PI': 'Programação para a Internet ', 'AED': 'Algoritmos e Estruturas de Dados '}
tipos = {'F': '* Frequência', 'E': '* Exame ', "R": '* Recurso ', 'ATM': 'Atendimento '}

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
    return data_anterior


print(disciplinas['PI'])
for i in range(2):
    data = datetime.strptime()