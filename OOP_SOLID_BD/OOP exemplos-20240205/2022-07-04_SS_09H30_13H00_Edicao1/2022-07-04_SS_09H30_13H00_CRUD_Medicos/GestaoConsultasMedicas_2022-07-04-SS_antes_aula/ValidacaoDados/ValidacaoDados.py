import re
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


def EValidoTelemovel(x):
    if re.search("^(91|92|93|96)[0-9]{7}$", x):  # No match
        return True
    return False

def LerTelemovel(legenda):
    while True:
        x = input(legenda)
        if EValidoTelemovel(x):
            return x
        else:
            print("%s inválido" % legenda.replace("?", ''))
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
    if re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-z]+$", email):  # No match
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


