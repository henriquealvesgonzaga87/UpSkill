from LerFicheiroCSV import *


cab, lista = LerFicheiroCSV("LEIAlunos.txt", delimitador=',')
print(cab)
nomes_unicos = []
for m in lista:
    n = m[0].split(' ')[0].capitalize()
    print(n)
    if n not in nomes_unicos:
        nomes_unicos.append(n)

lista = sorted(nomes_unicos[::2])
print(lista)
for n in lista:
    print(f"'{n}',")