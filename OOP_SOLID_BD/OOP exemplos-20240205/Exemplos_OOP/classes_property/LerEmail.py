import re

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
        if e == '':
            return None
        if ValidaEMail(e):
            return e
        else:
            print("%s inválido" % legenda)
    return e
