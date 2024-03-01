import re

def regex_nome(nome):
    while True:
        regex = r"^([A-Za-záàâãéèêíìóòôõúùç]{2,}\s+){0,}([A-Za-záàâãéèêíìóòôõúùç]{2,})$"
        if re.match(regex, nome):
            return True
        else:
            return False
        


def regex_nif(nif):
    regex = r"^([1-2]|5|6|8|9)\d{8}$"
    if re.match(regex, str(nif)):
        return True
    else:
        return False
