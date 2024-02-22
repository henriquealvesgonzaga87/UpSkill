import re

def ValidaNome(nome):
    if re.search("^[A-Z][a-z]{2,8}( [A-Z][a-z]{2,8}){1,4}$", nome):  # No match
        return True
    return False

def LerNome(legenda):
    while True:
        nome = input(legenda)
        if ValidaNome(nome):
            return nome
        else:
            print("Nome inválido.")

def LerNome2(legenda):
    while True:
        nome = input(legenda)
        if nome == '':
            return None
        if ValidaNome(nome):
            return nome
        else:
            print("Nome inválido.")

def ValidaNomeApelido(nome):
    if re.search("^[A-Z][a-z]{2,8} [A-Z][a-z]{2,8}$", nome):  # No match
        return True
    return False

