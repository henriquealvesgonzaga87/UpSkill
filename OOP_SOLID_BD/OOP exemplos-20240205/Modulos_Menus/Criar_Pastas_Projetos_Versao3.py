import os
# v3 (2023-11-02): add: LerGravarDados/LerGravarDados.py

projecto  = "FootballChampionshipManagement" # project
titulo = "Football Championship Management" # title
listaModulos = ["Clubs", "Players", "Games","Configuration","ValidationData","LerGravarDados","Menus"] # listModules
opcoesBasicas = ['Insert','Change','Delete','List all','Search name','Search code'] # basicOptions

if not os.path.exists(projecto):
    os.mkdir(projecto)

def GeraMenu(titulo, opcoes, no):
    imp = "import Menus.Menus\n"
    opcoesLista = ""
    ifs = "if op == 0:\n\t\tbreak\n"
    i = 0
    for x in opcoes:
        i = i + 1
        x = x.replace(" ", "")
        imp1 = "{0:s}.Menu{0:s}".format(x)
        if x == 'Menus':
            imp1 = "{0:s}.{0:s}".format(x)

        if x not in ['Configuration','ValidationData','LerGravarDados','Menus']:
            imp = imp + "import %s\n" % imp1
            opcoesLista = opcoesLista + f"'{x}',"
            ifs = ifs + f"\telif op == {i}:\n\t\t{imp1}.Menu()\n"
    opcoesLista = opcoesLista.rstrip(',')
    opcoesLista = f'[{opcoesLista}]'
    return f"""
{imp}
while True:
\top = Menus.Menus.Menu("{titulo}",{opcoesLista}, {no})
\t{ifs}"""

def GeraMenuModulos(titulo, opcoes, no):
    imp = "import Menus.Menus\nimport  Configuration.Configuracao\nimport LerGravarDados.LerGravarDados as ld\nimport ValidationData.ValidacaoDados as vd\nimport ValidationData.validators_pt as vd2\n"

    opcoesLista = ""
    ifs = "\tif op == 0:\n\t\t\tbreak\n"
    i = 0
    for x in opcoes:
        i = i + 1
        x = x.replace(" ", "")
        imp1 = "{0:s}".format(x)
        imp = imp + "from %s.%s import *\n" % (m, imp1)
        if x not in ['xConfiguracao','xValidacaoDados', 'xLerGravarDados', 'xMenus']:
            opcoesLista = opcoesLista + f"'{x}',"
            ifs = ifs + f"\t\telif op == {i}:\n\t\t\t{imp1}()\n"
    opcoesLista = opcoesLista.rstrip(',')
    opcoesLista = f'[{opcoesLista}]'
    return f"""
{imp}
def Menu():
\twhile True:
\t\top = Menus.Menus.Menu("{titulo}",{opcoesLista}, {no})
\t{ifs}"""

f = open(f'{projecto}/__init__.py', "wt"); f.close()
f = open(f'{projecto}/MenuPrincipal.py', "wt", encoding='utf-8');
print(GeraMenu(titulo, listaModulos, len(listaModulos)-4), file=f)
f.close()
# modulos
x = f'{projecto}/Configuration'
if not os.path.exists(x):
    os.mkdir(x)
fc = open(f'{projecto}/Configuration/Configuracao.py', "wt", encoding='utf-8')
x='''from datetime import datetime, timedelta, date
import locale
locale.setlocale(locale.LC_ALL, '')
'''
print(x, file=fc)

for m in listaModulos:
    x = f'{projecto}/{m}'
    if not os.path.exists(x):
        os.mkdir(x)
    f = open(f'{x}/__init__.py', "wt")
    f.close()
    if m not in ['Configuration','ValidationData','LerGravarDados','Menus']:
        f = open(f'{x}/Menu{m}.py', "wt", encoding='utf-8')
        print(f'# {m}', file=f)
        print(GeraMenuModulos(m, opcoesBasicas, len(opcoesBasicas)), file=f)
        f.close()
        for sm in opcoesBasicas:
            f = open(f'{x}/{sm.replace(" ","")}.py', "wt", encoding='utf-8')
            print(f'# {sm}', file=f)
            print(f'import Menus.Menus', file=f)
            y=f"""def {sm.replace(" ","")}():
\tprint('TODO: Implement the function!')
\tMenus.Menus.Pausa('{sm}')
\t# Put the code here to implement the functionality
"""
            print(y, file=f)
            f.close()
        # config
        nomeFicheiro = f"nomeFicheiro{m} = '{m}/{m}.CSV'"
        print(nomeFicheiro, file=fc)

fc.close()

x="""
import json

def GravarJSON(filename_out , dados):
    f = open(filename_out , 'w', encoding='utf8')
    print(dados)
    json.dump(dados , f, ensure_ascii=False , indent = 4) # to file
    f.close()
        # -------------
def LerJoson(filename_in):
    try:
        f = open(filename_in , encoding="utf8")
    except:
        return {"Clubs":[],'Players': [],'Games':[]}
        # Mudar de acordo com a estrutura de dados JSON
    dados = json.load(f)

    return dados
"""

f = open(f'{projecto}/LerGravarDados/LerGravarDados.py', "wt", encoding='utf-8')
print(x, file=f)
f.close()



x="""
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    NORMAL = '\033[00m'

def print2(cor, prt):
    print(f"{cor}{prt}{bcolors.NORMAL}")
    
def Menu(Titulo, Opcoes, np):
    print2(bcolors.OKBLUE, "* " * 5 + Titulo + " *" * 5)
    print()
    for i in range(np):
        print(i + 1, "-", Opcoes[i])
    print("0 - Terminar")
    while True:
        try:
            op = int(input("Opção?"))
        except ValueError:
            print ("Não digitou um número inteiro!")
            continue
        if op >= 0 and op <= np:
            break
        else:
            print ("O valor deve estar entre %d e %d" % (0, np))

    return op

def Pausa(msg=''):
    input(msg + " Prima a tecla Enter para continuar ...")


def Pausa1(msg=''):
    import keyboard
    # Check if b was pressed
    #if keyboard.is_pressed('b'):
	#   print('b Key was pressed')
    print(msg + " Prima qq tecla para continuar ...", end='')
    while True:
        if keyboard.read_key():
            print()
            break
"""

f = open(f'{projecto}/Menus/Menus.py', "wt", encoding='utf-8')
print(x, file=f)
f.close()

# --------------------
x="""import re
def EValidoNome(nome):
    if re.search("^[A-Z][a-z]{1,10}( [A-Z][a-z]{1,10}){0,5}", nome):  # No match
        return True
    return False

def LerNome(legenda):
    while True:
        nome = input(legenda)
        if EValidoNome(nome):
            return nome
        else:
            print("%s inválido" % legenda)
    return None
# -------------------
def EValidoNomePessoa(nome):
    if re.search("^[A-Z][a-z]{1,10} [A-Z][a-z]{1,10}", nome):  # No match
        return True
    return False
def LerNomePessoa(legenda):
    while True:
        nome = input(legenda)
        if EValidoNomePessoa(nome):
            return nome
        else:
            print("%s inválido" % legenda)
    return None

def ValidaEMail(email):
    if re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):  # No match
        return True
    return False

def ValidaEMail2(email):
    if re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):  # No match
        return True
    return False

def LerEMail(legenda):
    while True:
        e = input(legenda)
        if ValidaEMail(e):
            return e
        else:
            print("%s inválido" % legenda)
    return e

def ValidaNome(nome):
    import re
    regex = r"[A-Z][a-z]{2,8}( [a-z]{2,3}){0,1}( [A-Z][a-z]{2,8}){1,4}"
    matches = re.finditer(regex, nome, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        return True
    else:
        return False

def ValidaSigla(sigla):
    import re
    regex = r"[A-Z]{3,5}"
    matches = re.finditer(regex, sigla, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        return True
    else:
        return False


def LerNumeroInteiro0(msg, min, max):
    while True:
        n = int(input(msg))
        if n >= min and n <= max:
            break
        else:
            print ("O valor deve estar entre %d e %d" % (min, max))
    return n

def LerNumeroInteiro1(msg, min, max):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print ("Não digitou um número inteiro!")
            continue
        if n >= min and n <= max:
            break
        else:
            print ("O valor deve estar entre %d e %d" % (min, max))
    return n
# ns = LerNumeroInteiro1("Número sócio?", 0, 100)

def LerNumero(msg, min, max, tipo="inteiro"):
    # tipo in ["inteiro", "real"]
    while True:
        try:
            if tipo=="inteiro":
                n = int(input(msg))
            else:
                n = float(input(msg))
        except ValueError:
            print ("Não digitou um número inteiro!")
            continue
        if n >= min and n <= max:
            break
        else:
            print ("O valor deve estar entre %d e %d" % (min, max))
    return n
# ni = LerNumero("Número sócio?", 0, 100)
# print(type(ni))
# ni = LerNumero("Número sócio?", 0, 100, "inteiro")
# print(type(ni))
# nr = LerNumero("Número sócio?", 0, 100, "real")
# print(type(nr))
# exit();


def LerData(msg, min=None, max=None):
    from datetime import datetime
    while True:
        data_texto = input(msg)
        try:
            data = datetime.strptime(data_texto, '%Y-%m-%d')
        except ValueError:
            print("Data inválida")
            continue
        c=0
        if min == None:
            c = 1
        elif data >= min:
            c = 1
        if max == None:
            c = c + 1
        elif data <= max:
            c = c + 1
        if c != 2:
            print("Data fora do intervalo %s e %s"
                  % (min.strftime ("%Y-%m-%d"),
                     max.strftime ("%Y-%m-%d")))
        else:
            break                     
    return data
# from datetime import datetime
# data_min = datetime.strptime("2018-01-01", '%Y-%m-%d')
# data_max = datetime.strptime("2018-12-31", '%Y-%m-%d')
# data_fundacao = LerData("Data fundação?", data_min, data_max)
#
# agora = datetime.now()
# print (agora)
# print ("Data: ", agora.strftime ("%Y-%m-%d"))
# print ("Hora: ", agora.strftime ("%X"))

"""
f = open(f'{projecto}/ValidationData/ValidacaoDados.py', "wt", encoding='utf-8')
print(x, file=f)
f.close()

x='''

"""Funções para validar números de bilhete de identidade,
     contribuinte, identificação bancária, segurança social,
     cartão de crédito e ISBN.
     Segundo contribuição de _kk_, B.Baixo, Jorge Buescu,
     Michael Gilleland (Merriam Park Software), Filipe Polido,
     Jeremy Bradbury e Hugo Pires (DRI/DRO, IIESS).
     Estas rotinas são do dominio público (sem copyright).

     versão 0.17, 2009/Nov.10
     ORIGINAL: http://maracujah.net/files/software/nif.py
"""

#-------------------------------------------------------------
# Changes:
#   Nome das funções locais passam a iniciar-se por apenas um
#     underscore ('_')
#   O primeiro dígito de um NIF pode ser 8 (João Correia)
#   Correção de bug na função controlCreditCard()
#   controlCreditCard() simplificada
#   Adicionada função para somar produto de membros de duas
#     lista, _sumLists(), e outras beneficiações
#   Adicionada função para validar nmero de segurança social:
#     controlNISS()
#   Adicionada função para validar IBAN (apenas Portugal),
#     segundo sugestão e contribuição de Paula Vaz
#   Alterada a função controlNIB() conforme código em
#     http://download-uk.oracle.com/appsnet/115finpor.pdf
#     contribuição de Pedro Graca segundo sugestão de
#     Francisco Pereira
#   Adicionada função para validar ISBN: controlISBN()
#   Adicionada função _toIntList() para converter string
#     lista de inteiros
#   Funcoes verificam validade de cada dígito. Controlada a
#     validade do primeiro dígito do NIF, contribuição de
#     Nuno Anes
#   Corrigida a função controlCreditCard() segundo
#     sugestão de Pedro Graca.
#   Adicionada função para validar número de cartão de
#     crédito: controlCredtiCard()
#   Função controlNBI() corrigida por António Manuel Dias
#     apos sugestão de Pedro Graca
#-------------------------------------------------------------


import string

# tamanhos dos nums do BI, contribuinte, NISS, NIB e ISBN
(LEN_NBI, LEN_NIF, LEN_NISS, LEN_NIB, LEN_ISBN) = (9, 9, 11, 21, 10)
# tamanho mínimo e máximo de num cartão de crédito
(MINLEN_CC, MAXLEN_CC) = (7, 19)


def _toIntList(numstr, acceptX=0):
    """
    Converte string passada para lista de inteiros,
    eliminando todos os caracteres inválidos.
    Recebe string com nmero a converter.
    Segundo parÃ¢metro indica se 'X' e 'x' devem ser
    convertidos para '10' ou não.
    """
    res = []

    # converter todos os dígitos
    for i in numstr:
        if i in string.digits:
            res.append(int(i))

    # converter dígito de controlo no ISBN
    if acceptX and (numstr[-1] in 'Xx'):
        res.append(10)
    return res


def _valN(num):
    """
    Algoritmo para verificar validade de NBI e NIF.
    Recebe string com número a validar.
    """

    # converter num (string) para lista de inteiros
    num = _toIntList(num)

    # computar soma de controlo
    sum = 0
    for pos, dig in enumerate(num[:-1]):
        sum += dig * (9 - pos)

    # verificar soma de controlo
    return (sum % 11 and (11 - sum % 11) % 10) == num[-1]


def _sumLists(a, b):
    """
    Devolve soma dos produtos, membro a membro, das listas.
    Recebe duas listas de tamanho igual.
    """
    val = 0
    for i in map(lambda a, b: a * b, a, b):
        val += i
    return val


def controlNBI(nbi, control):
    """
    Verifica validade do número do bilhete de identidade.
    Recebe string com número BI e string com dígito de controlo.
    """

    # juntar NBI e dígito de controlo
    # adicionar zero Ã  esquerda de nbi se for de comprimento 7
    nbi = str(nbi) + str(control)
    nbi = '0' * (len(nbi) == 8) + nbi

    # verificar tamanho do número
    if len(nbi) != LEN_NBI:
        return False

    # verificar validade
    return _valN(nbi)


def controlNIF(nif):
    """
    Verifica validade de número de contribuinte.
    Recebe string com NIF.
    """

    # verificar tamanho do número passado
    if len(nif) != LEN_NIF:
        return False

    # verificar validade do carácter inicial do NIF
    if nif[0] not in "125689":
        return False

    # verificar validade
    return _valN(nif)


def controlNISS(niss):
    """
    Verifica validade de número de segurança social.
    Recebe string com NISS.
    """
    table = (29, 23, 19, 17, 13, 11, 7, 5, 3, 2)

    # verificar tamanho do número passado
    if len(niss) != LEN_NISS:
        return False

    # verificar validade do carácter inicial do NISS
    if niss[0] not in "12":
        return False

    # converter número para lista de inteiros
    niss = _toIntList(niss)

    # verificar soma de controlo
    return niss[-1] == 9 - _sumLists(table, niss[:-1]) % 10


def controlNIB(nib):
    """
    Verifica validade de número de identificação bancária.
    Recebe string com NIB.
    """
    table = (73, 17, 89, 38, 62, 45, 53, 15, 50,
             5, 49, 34, 81, 76, 27, 90, 9, 30, 3)

    # converter para lista de inteiros
    nib = _toIntList(nib)

    # verificar tamanho do número passado
    if len(nib) != LEN_NIB:
        return False

    # ultimos dois dígitos são o valor de verificação
    return nib[-2] * 10 + nib[-1] == 98 - _sumLists(table, nib[:-2]) % 97


def controlIBAN(iban):
    """
    Verifica validade de número de identificação bancária
    internacional (apenas Portugal).
    Recebe string com IBAN.
    """

    # verificar código IBAN para Portugal
    if iban[:4] == 'PT50':
        return controlNIB(iban[5:])
    else:
        raise ValueError("Código IBAN não suportado: %s" % iban[:4])


def controlCreditCard(ncc):
    """
    Verifica a validade de número de cartão de crédito.
    Recebe string com número do cartão de crédito.
    """

    # converter número para lista de inteiros e inverter lista
    ncc = _toIntList(ncc)
    ncc.reverse()

    # verificar tamanho do número
    if MINLEN_CC > len(ncc) or len(ncc) > MAXLEN_CC:
        return False

    # computar soma de controlo
    sum = 0
    alt = False

    for i in ncc:
        if alt:
            i *= 2
            if i > 9:
                i -= 9
        sum += i
        alt = not alt

    # verificar soma de controlo
    return not (sum % 10)


def controlISBN(isbn):
    "Verifica a validade de ISBN."
    # converter para lista de inteiros
    isbn = _toIntList(isbn, 1)

    # verificar tamanho do número
    if len(isbn) != LEN_ISBN:
        return False

    # computar soma de controlo
    sum = 0
    for pos, dig in enumerate(isbn[:-1]):
        sum += ((pos + 1) * dig)

    # verificar soma de controlo
    return sum % 11 == isbn[-1]


#################################################################
# Rotina de teste
#

if __name__ == "__main__":

    print ()
    print("Testar BI 10039784-0:", controlNBI("10039784", "0"))

    print("Testar BI 6617084-2:", controlNBI("6617084", "2"))

    print("Testar contribuinte 204716624:", controlNIF("204716624"))

    print("Testar segurança social 11234567892:", controlNISS("11234567892"))

    print("Testar NIB 0018.0000.40359330001.87:",
          controlNIB("0018.0000.40359330001.87"))

    print("Testar IBAN PT50.0018.0000.40359330001.87:",
          controlIBAN("PT50.0018.0000.40359330001.87"))

    print("Testar cartão de crédito 1234 5678 9999 9993:",
          controlCreditCard("1234 5678 9999 9993"))

    print("Testar ISBN 972-662-792-3:", controlISBN("972-662-792-3"))

    print("Testar ISBN 0-471-54891-X:", controlISBN("0-471-54891-X"))

    print()
'''

f = open(f'{projecto}/ValidationData/validators_pt.py', "wt", encoding='utf-8')
print(x, file=f)
f.close()

import seedir as sd
sd.seedir(os.path.join(os.getcwd(),f'{projecto}'), style='emoji')
