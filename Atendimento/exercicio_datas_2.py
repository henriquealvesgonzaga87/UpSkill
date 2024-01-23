from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_ALL, '')
data_input = input("informe uma data (dd/mm/aaaa): ")
data_formatada = datetime.strptime(data_input, '%d/%m/%Y')
data_seg = data_formatada
while True:
    dia_semana = int(datetime.strftime(data_seg, '%w')) + 1
    if dia_semana == 2:
        break
    else:
        data_seg = data_seg - timedelta(days=1)
data_sex = data_seg + timedelta(days=4)

print(datetime.strftime(data_seg, 'Semana de %d a'), end=' ')
print(datetime.strftime(data_sex, '%d de %B de %Y'))
locale.setlocale(locale.LC_ALL, 'en_US')
print(datetime.strftime(data_seg, 'Week from %d to'), end=' ')
print(datetime.strftime(data_sex, '%dth %B, %Y'))
