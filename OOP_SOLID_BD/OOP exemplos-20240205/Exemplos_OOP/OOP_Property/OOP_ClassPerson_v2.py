# Defina uma classe para representar pessoas. Considere os seguintes atributos:
# Nome, E-Mail, Telefone, Peso, Altura, Data nascimento.
#
# Defina os seguinte métodos:
# - Idade em anos
# - Idade em dias
# - Idade numa dada data
# - Numero de dias para aniversário
# - dia da semana do aniversário da pessoa para um dado ano
# - indice de massa corporal
# Notas:
# 1) Os métodos 'set' validar os dados de acordo com o seu domínio de valores admissíveis.
#
# ---------------------------------
# Define a class to represent people. Consider the following attributes:
# Name, E-Mail, Phone, Weight, Height, Date of birth.
#
# Define the following methods:
# - Age in years
# - Age in days
# - Age on a given date
# - Number of days to birthday
# - Day of the week of the person's birthday for a given year
# - Body mass index
# Notes:
# 1) The 'set' methods must validate the data according to its domain of admissible values..


import locale
locale.setlocale(locale.LC_ALL, '')
from datetime import datetime, timedelta, date
# https://www.programiz.com/python-programming/datetime/strptime
# tabela com significado do formato

# define class: class <name_of_class>:
class Person:
    #attributes
    # constructor
    def __init__(self, Name, EMail, Phone, Weight, Height, DateofBirth):
        self.Name = Name   # Notice: sem _ | without _
        self.EMail= EMail
        self.Phone = Phone
        self.Weight = Weight
        self.Height = Height
        self.DateofBirth = DateofBirth

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, name):
        import re
        # if name != '':
        if re.search("^[A-Z][a-z]{2,8} [A-Z][a-z]{2,8}$", name):
            self._Name = name  # _ to the name of the attribute
        else:
            print('Name %s not allowed' % name)

    @property
    def DateofBirth(self):              # <=> get
        return self._DateofBirth

    @DateofBirth.setter                 # <=> set
    def DateofBirth(self, date):
        # Notice: com _ | with _
        if not isinstance(date, datetime):
            print('Date of Birth %s is not type of datetime (is) ' % date)
            return
        if date <= datetime.now():
            self._DateofBirth = date
        else:
            print('Date of Birth %s not allowed' % date)


    @property
    def EMail(self):
        return self._Email

    @EMail.setter
    def EMail(self, email):
        import re
        if re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):  # No match
            self._Email = email  # _ to the name of the attribute
        else:
            print('E-Mail %s not allowed' % email)

    def __str__(self):
        return str(self.__dict__)

    # setters and getters

    # funcionalidades
    def getAgeInYears(self):
        self.getAgeInYearsInData(datetime.now().strftime('%Y-%m-%d')) # datetime -> texto

    def getAgeInYearsInData(self, data):
        data = datetime.strptime(data, "%Y-%m-%d")  # texto -> datatime
        # 21 - 23 | 15 - 23   | 22 - 23
        if data.year - self.DateofBirth.year >= 2:
            anos = data.year - self.DateofBirth.year - 1  # anos completos
        else:
            anos = 0
        if data.month > self.DateofBirth.month:
            anos = anos + 1
        elif data.month == self.DateofBirth.month:
            if data.day >= self.DateofBirth.day:
                anos = anos + 1

        return anos

    def getBirthdayDays(self):
        # TODO
        # (now - self.DateofBirth).days
        # t4 = datetime(year=2018, month=7, day=12)
        return (datetime.now() - self.DateofBirth)

    def NumberDaysToBirthday(self):
        agora = datetime.now()
        dataAniversario = datetime(year=agora.year,
                                   month=self.DateofBirth.month,
                                   day=self.DateofBirth.day)
        agora = datetime(year=agora.year, month=agora.month, day=agora.day)
        d = (dataAniversario - agora).days
        return d

    def NumberDaysToBirthdayReal(self):
        import math
        agora = datetime.now()
        dataAniversario = datetime(year=agora.year,
                                   month=self.DateofBirth.month,
                                   day=self.DateofBirth.day,
                                   hour=self.DateofBirth.hour,
                                   minute=self.DateofBirth.minute,
                                   second=self.DateofBirth.second)
        d = ((dataAniversario - agora).seconds) / (24 * 3600.0)
        # devolve a diferença em segundos entre as horas das datas. Ignona od dias.
        return round(d + self.NumberDaysToBirthday(), 2)


    def DayOfWeekOfBirthday(self, year):
        dataAniversario = datetime(year=year,
                            month=self.DateofBirth.month,
                            day=self.DateofBirth.day)
        # %w	Weekday as a decimal number.	0, 1, ..., 6
        # %W	Week number of the year (Monday as the first day of the week).
        # All days in a new year preceding the first Monday are considered to be in week 0.
        return int(dataAniversario.strftime('%w')) + 1

    def NameOfDayOfWeekOfBirthday(self, year, tipo='A'):
        dataAniversario = datetime(year=year,
                            month=self.DateofBirth.month,
                            day=self.DateofBirth.day)
        # %a	Abbreviated weekday name.	Sun, Mon, ...
        # %A	Full weekday name.	Sunday, Monday, ...
        if tipo not in ('a', 'A'):
            tipo = 'A'
        return dataAniversario.strftime('%' + tipo)


t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
print(type(t4))
# create an object
ana = Person('Ana Silva', 'ana@ipg.pt', 961234567, 65.5, 174, '2000-01-01')
print('Sem DateofBirth ', ana)
ana.DateofBirth = datetime.strptime('2000-01-01 18:05:08', "%Y-%m-%d %H:%M:%S")
print("Ana construtor: ", ana)
maria = Person('Maria', 'ana@ipg.pt', 961234567, 65.5, 174,
               datetime.strptime('2000-04-12 18:05:08', "%Y-%m-%d %H:%M:%S"))

datas = ['2000-04-13 18:05:08', '2000-04-14 18:05:08', '2000-04-15 18:05:08',
    '2021-04-14 18:05:08', '2022-04-14 18:05:08']
for d in datas:
    d = datetime.strptime(d, "%Y-%m-%d %H:%M:%S")
    maria.DateofBirth = d
    print("Idade ", d, maria.getAgeInYears(), maria.getBirthdayDays(),
          maria.getAgeInYearsInData('2026-12-25'), maria.DateofBirth,
          maria.NumberDaysToBirthday(), maria.NumberDaysToBirthdayReal())

for ano in range(2020, 2030):
    print(ano, maria.DateofBirth, maria.DayOfWeekOfBirthday(ano),
          maria.NameOfDayOfWeekOfBirthday(ano),
          maria.NameOfDayOfWeekOfBirthday(ano,'a'))

print("Maria construtor: ", maria)
print("Idade ", maria.getAgeInYears())

print("x",ana)
print(ana.Name)
print(ana.EMail)
print( ana.DateofBirth)
ana.Name = 'Ana'; print(ana)
ana.Name = '007'; print(ana)
ana.Name = ''; print(ana)
ana.Name = 'Ana Silva'; print(ana)
ana.EMail = 'email inválido'; print(ana)
exit()


agora = datetime.now() # current date and time
print (agora.strftime("%m/%d/%Y, %H:%M:%S %a %W"))


print(ana)
ana.Name = '007'
ana.setName('007')
print(ana)
ana.setEMail('007')
print(ana)





# attributes are by default public.
ana.Height = -178
print(ana)




