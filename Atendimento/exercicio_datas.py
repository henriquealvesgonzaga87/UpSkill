from datetime import datetime, timedelta
import locale
# data atual = do computador
# data_seg = ...
# data_sexta = ...
# escrever com strftime ...

locale.setlocale(locale.LC_ALL, '')
data_atual = datetime.now()
for x in range(10):
    print(data_atual)
    print(datetime.strftime(data_atual, "%Y"))
    print(datetime.strftime(data_atual, "%w %A")) # dia da semana de 0 a 6
    data_atual = data_atual + timedelta(days=1)

data_atual = datetime.now()
data_seg = data_atual
while True:
    dia_semana = int(datetime.strftime(data_seg, '%w')) + 1
    if dia_semana == 2:
        break
    else:
        data_seg = data_seg - timedelta(days=1)
print(data_atual, datetime.strftime(data_atual, '%w %A'))
print(datetime.strftime(data_seg, '%w %A'))

data_atual = datetime.now()
data_formatada = datetime.strptime('2024-01-10', '%Y-%m-%d')
data_sex = data_seg + timedelta(days=4)

dia_seg = 8
dia_sex = 12
mes_seg = 1
mes_sex = 1
if mes_seg != mes_sex:
    nome_mes_seg = 'janeiro'
else:
    nome_mes_seg = ''
# print(datetime.strftime(data_sex, '%d de %B de %Y'))
# print(data_formatada)
