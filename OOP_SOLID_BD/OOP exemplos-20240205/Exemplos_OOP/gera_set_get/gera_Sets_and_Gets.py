from collections import namedtuple
import sys

classes = []
classe = 'Carro'; atributos = "Marca;Modelo;Portas;Cilindrada;Potencia;Co2;Cor;Versao;Ano;Mes;Preço"
classes.append((classe, atributos))

classe = 'CarroUsado'; atributos = "Matricula;Estado;NumeroDeRegistos;Preço"
classes.append((classe, atributos))

classe = 'Motor'; atributos = "marca;potencia;cilindra;Preço"
classes.append((classe, atributos))

classe = 'Roda'; atributos = "Jante;Pneu;Preço"
classes.append((classe, atributos))

classe = 'Jante'; atributos = "Largura;TamanhoDaRoda;NúmeroDeOrifícios;Cor;Preço"
classes.append((classe, atributos))

classe = 'Pneu'; atributos = "Largura;Altura;Diâmetro;Carregamento;Preço"
classes.append((classe, atributos))

# Então cá vai. O chassis pode ser definido como a base do veículo e sobre o qual são instalados
# os elementos que o formam: o motor, a caixa de velocidades, a coluna de direção,
# o depósito de combustível e a carroçaria.
# Por seu lado, esta última é a zona visível do veículos e é composta pelo capô,
# pelas portas, pelos painéis e ainda pelo habitáculo.

classe = 'Chassis'; atributos = "Marca;Modelo;Comprimento;Largura"
classes.append((classe, atributos))

classe = 'Carrocaria'; atributos = "Modelo;capô;portas;painéis;habitáculo"
classes.append((classe, atributos))
# composta pelo capô, pelas portas, pelos painéis e ainda pelo habitáculo.

classe = 'Carro2'; atributos = "Marca;Modelo;Rodas;Motor;Chassis;Carrocaria;Preço"
classes.append((classe, atributos))

antes = sys.stdout
imports = ''
for d in classes:
    classe = d[0]
    atributos = d[1]

    imports += f'from Classe{classe} import *\n'

    f = open(f'Classe{classe}.py', "wt", encoding='utf-8')
    sys.stdout = f

    print (f'# from Classe{classe} import *')

    atributos = atributos.split(';')
    print("# Criar objecto com base em dicionário")
    x=''
    for a in atributos:
        x += f"r['{a}'], "
    print(f"# {classe.lower()} = {classe}({x.rstrip(', ')})")

    print("# Criar objecto usando construtor")
    x=''
    for a in atributos:
        x += f"'{a}', "
    criar_objeto = f"{classe.lower()} = {classe}({x.rstrip(', ')})"
    imprimir_ficha = f'{classe.lower()}.Ficha()'
    print("#", criar_objeto)

    de = "âãàáéêóôõíç"
    pa = "aaaaeeoooic"
    atributos = d[1]
    lista = zip(de, pa)
    for a in lista:
        atributos = atributos.replace(a[0], a[1])

    atributos = atributos.split(';')
    print(f'class {classe}:')
    parametros = ''
    atributos_init = ''
    print('\t# sets')
    for a in atributos:
        m = a[0:1].lower()+a[1:] # inicial_minuscula
        M = a[0:1].capitalize()+a[1:] # inicial_minuscula
        set = f'''\tdef set{M}(self, {m}):
\t\tif {m} != '':
\t\t\tself.{m} = {m}
\t\t\treturn True
\t\telse:
\t\t\treturn False'''
        print (set)
        print()

    print('\t# gets')
    for a in atributos:
        m = a[0:1].lower()+a[1:] # inicial_minuscula
        M = a[0:1].capitalize()+a[1:] # inicial_minuscula
        get = f'''\tdef get{M}(self):
\t\treturn self.{m}'''
        print (get)
        parametros += f'{m}, '
        atributos_init += f'\t\tself.{m} = {m}\n'

    print()
    print('\t# construtor')
    x= f'''\tdef __init__(self, {parametros.rstrip(', ')}):
{atributos_init}'''
    print (x)

    print("\tdef __str__(self):")
    print("\t\treturn str(self.__dict__)\n")

    nome_classe = "print(f'Objeto da classe: {self.__class__.__name__}')"
    base = "print(f'Objeto da classe: {self.__class__.__base__}')"
    bases = "print(f'Objeto da classe: {self.__class__.__bases__}')"
    x=f'''\tdef Ficha(self):
\t\ttemp = vars(self)
\t\tprint('-----------------')
\t\tprint('Objeto da classe: {classe}')
\t\t{nome_classe}
\t\t{base}
\t\t{bases}
\t\tfor item in temp:
\t\t\tc = 25 - len(item)
\t\t\tprint("%s%s : %s" % (item.capitalize(), '.' * c, temp[item]))'''
    print (x)
    print()

    x=f'''\tdef FichaDicionario(self):
\t\tprint('-----------------')
\t\tprint('Objeto da classe: {classe}')
\t\t{nome_classe}
\t\tfor k, v in self.__dict__.items():
\t\t\tc = 25 - len(k)
\t\t\tprint("%s%s : %s" % (k.capitalize(), '.' * c, v))'''
    print (x)
    print()
    print("#", criar_objeto)
    print("#", imprimir_ficha)

    f.close()
sys.stdout = antes
print (imports)
