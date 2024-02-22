import re
def EValidoTelemovel(x):
    if re.search(r"^(91|92|93|96)\d{7}$", x):  # No match
        return True
    return False

def EValidoTelefone(x):
    if re.search(r"^2\d{8}$", x):  # No match
        return True
    return False

def LerTelemovel(x):
    while True:
        Telemovel = input(x)
        if EValidoTelemovel(Telemovel):
            return Telemovel
        else:
            print("%s inválido" % x)
    return None

def LerTelefone(x):
    while True:
        Telefone = input(x)
        if EValidoTelefone(Telefone):
            return Telefone
        else:
            print("%s inválido" % x)

def LerTelemovel2(x):
    Telemovel = input(x)
    if Telemovel == '':
        return None
    else:
        while True:
            if EValidoTelemovel(Telemovel):
                return Telemovel
            else:
                print("%s inválido" % x)

def EValidoNome(nome):
    if re.search("^[A-Z][a-z]{1,10}( [A-Z][a-z]{1,10}){0,5}", nome):  # No match
        return True
    return False

def EValidoCod(cod):
    cod1 = int(cod)
    if cod1 >= 1:  # No match
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

def LerNome2(legenda):
    while True:
        nome = input(legenda)
        if nome == '':
            return None
        if EValidoNome(nome):
            return nome
        else:
            print("%s inválido" % legenda)

def LerCod2(legenda):
    while True:
        cod = input(legenda)
        if cod == '':
            return None
        if EValidoCod(cod):
            return cod
        else:
            print("%s inválido" % legenda)

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

def LerEMail2(legenda):
    while True:
        e = input(legenda)
        if e== '':
            return None
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
        if msg == '':
            return None
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

def Lercodigopostal(codigop):
    padrao = re.compile(r'^\d{4}-\d{3}$')

    if padrao.match(codigop):
        return True
    else:
        return False

def LerNumero(msg, min, max, tipo):
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


def LerData(data):
    from datetime import date, datetime
    while True:
        data_hoje = str(date.today())
        if data == '':
            return None

        try:
            data = str(datetime.strptime(data, '%Y-%m-%d').date())

        except ValueError:
            return LerData(input("Digite a data novamente:"))

        if data >= data_hoje:
            break
        else:
            data = str(input("Introduza uma data atual ou futura(enter para voltar): "))

    return data

def Lerdataa(msg):
    from datetime import datetime
    while True:
        data = int(input(msg))
        data_atual = datetime.now().date()
        if data >= data_atual:
            return msg
        else:
            print("Data fora do intervalo %s")

    # from datetime import datetime
# data_min = datetime.strptime("2018-01-01", '%Y-%m-%d')
# data_max = datetime.strptime("2018-12-31", '%Y-%m-%d')
# data_fundacao = LerData("Data fundação?", data_min, data_max)
#
# agora = datetime.now()
# print (agora)
# print ("Data: ", agora.strftime ("%Y-%m-%d"))
# print ("Hora: ", agora.strftime ("%X"))


