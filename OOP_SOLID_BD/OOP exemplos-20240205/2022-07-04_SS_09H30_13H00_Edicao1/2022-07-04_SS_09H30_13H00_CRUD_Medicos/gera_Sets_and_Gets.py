from collections import namedtuple

atributos = "Número;Nome;ViaVerde;EMail;Telemovel;NIF;NCC;NISS;DataNascimento".split(';')
print("# Criar objecto com base em dicionário")
x=''
for a in atributos:
    x += f"r['{a}'], "
print(f"obj = Class({x.rstrip(', ')})")

atributos = "Numero;Nome;ViaVerde;EMail;Telemovel;NIF;NCC;NISS;DataNascimento".split(';')
parametros = ''
atributos_init = ''
print('# sets')
for a in atributos:
    m = a[0:1].lower()+a[1:] # inicial_minuscula
    M = a[0:1].capitalize()+a[1:] # inicial_minuscula
    set = f'''def set{M}(self, {m}):
    self.{m} = {m}
    '''
    print (set)

print('# gets')
for a in atributos:
    m = a[0:1].lower()+a[1:] # inicial_minuscula
    M = a[0:1].capitalize()+a[1:] # inicial_minuscula
    get = f'''def get{M}(self):
    return self.{m}
    '''
    print (get)
    parametros += f'{m}, '
    atributos_init += f'\tself.{m} = {m}\n'

print('# construtor')
x= f'''def __init__(self, {parametros.rstrip(', ')}):
{atributos_init}'''
print (x)

x='''def Ficha(self):
    temp = vars(self)
    print('-----------------')
    for item in temp:
        c = 25 - len(item)
        print("%s%s : %s" % (item.capitalize(), '.' * c, temp[item]))'''
print (x)





dictionary = {"Name":"Bob", "Age":18, "Occupation":"Student"}
object_name = namedtuple("ObjectName", dictionary.keys())(*dictionary.values())

print(object_name)
# OUTPUT
# ObjectName(Name='Bob', Age=18, Occupation='Student')
print(object_name.Name)
# OUTPUT
# Bob
print(object_name.Age)
# OUTPUT
18
print(object_name.Occupation)
# OUTPUT
# Student
