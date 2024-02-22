#!/usr/bin/python
from datetime import datetime, timedelta, date
import locale
locale.setlocale(locale.LC_ALL, '')

from Classe_Pessoa_DataNascimento import Pessoa

# dd/mm/YY H:M:S
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


pessoa = Pessoa('Bela Cruz Ferreira', datetime.strptime('1965-07-04 18:05:08', "%Y-%m-%d %H:%M:%S"), 'bcruz@ipg.pt', '961234567')
# pessoa.Display()
print("*"*60)
pessoa.Ficha()
pessoa.setNome('Ana Maria Costa')
pessoa.Ficha()
pessoa.setNome('')
pessoa.PlayTexto('Ficha de:')
pessoa.Ficha()


print('Nome completo...: ', pessoa.getNome())
print('Nome............: ', pessoa.getPrimeiroNome())
print('Apelido.........: ', pessoa.getApelido())
print('Iniciais........: ', pessoa.getIniciais())

print('Idade...........: ', pessoa.getIdade(), type(pessoa.getIdade()))
print('Idade dias......: ', pessoa.getIdadeDias(), type(pessoa.getIdadeDias()))
print('Idade meses.....: ', pessoa.getIdadeMeses(), type(pessoa.getIdadeMeses()))
print('Idade anos......: ', pessoa.getIdadeAnos(), type(pessoa.getIdadeAnos()))
print('Idade anos calen: ', pessoa.getIdadeAnosCalendario(), type(pessoa.getIdadeAnosCalendario()))
print('Idade AAA/MM/DD.: ', pessoa.getIdadeAnosMesesDias(), type(pessoa.getIdadeAnosMesesDias()))

d = datetime.strptime('2022-12-31', "%Y-%m-%d")
print(f'Idade em anos a {d.strftime("%Y-%m-%d")} : ', pessoa.getIdadeAnosData(d))
d = datetime.strptime('1975-04-25', "%Y-%m-%d")
print(f'Idade em anos a {d.strftime("%Y-%m-%d")} : ', pessoa.getIdadeAnosData(d))
pessoa.ApresentacaoOral()

exit()
for d in [datetime.strptime('1975-06-04 18:05:08', "%Y-%m-%d %H:%M:%S"),
          datetime.strptime('1962-07-05 08:25:24', "%Y-%m-%d %H:%M:%S"),
          datetime.strptime('1992-08-04 18:05:08', "%Y-%m-%d %H:%M:%S")]:
    pessoa = Pessoa('Bela Cruz Ferreira',d , 'bcruz@ipg.pt', '961234567')
    # pessoa.Display()
    print("*"*60)
    pessoa.Ficha()
    pessoa.setNome('Ana Maria Costa')
    pessoa.Ficha()
    pessoa.setNome('')
    pessoa.Ficha()

    print('Nome completo...: ', pessoa.getNome())
    print('Nome............: ', pessoa.getPrimeiroNome())
    print('Apelido.........: ', pessoa.getApelido())
    print('Iniciais........: ', pessoa.getIniciais())

    print('Idade...........: ', pessoa.getIdade(), type(pessoa.getIdade()))
    print('Idade dias......: ', pessoa.getIdadeDias(), type(pessoa.getIdadeDias()))
    print('Idade meses.....: ', pessoa.getIdadeMeses(), type(pessoa.getIdadeMeses()))
    print('Idade anos......: ', pessoa.getIdadeAnos(), type(pessoa.getIdadeAnos()))
    print('Idade anos calen: ', pessoa.getIdadeAnosCalendario(), type(pessoa.getIdadeAnosCalendario()))
    print('Idade AAA/MM/DD.: ', pessoa.getIdadeAnosMesesDias(), type(pessoa.getIdadeAnosMesesDias()))
    pessoa.ApresentacaoOral()
