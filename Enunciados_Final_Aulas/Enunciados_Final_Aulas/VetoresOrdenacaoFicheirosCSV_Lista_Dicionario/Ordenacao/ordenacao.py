# In Python, use the sorted function or the list sort method.


L = {'car': 'Ford', 'year': 2005, 'year': 2006}
print(L)
L['maria'] = {'car': 'Fiat', 'year': 2005}
print()

cars = [
  {'maria': {'car': 'Ford', 'year': 2005}},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
#exit()



L = ["Mario", "Carla", "Anabela", "Maria", "Nuno"]
L.sort()            # Modifies list L in-place
print (L)
exit()

L2 = sorted(L)      # Creates L2. L is not modified!
print(L2)

#These functions can sort by different criteria.
L = ["Mario", "Carla", "anabela", "Maria", "nuno"]

print(sorted(L))                    # lexicographic sort
                                    #-> ['Carla', 'Maria', 'Mario', 'anabela', 'nuno']
print(sorted(L, key=len))           # sort by length
                                    #-> ['nuno', 'Mario', 'Carla', 'Maria', 'anabela']
print(sorted(L, key=str.upper))     # case-insensitive
                                    #-> ['anabela', 'Carla', 'Maria', 'Mario', 'nuno']

# The optional key argument receives a function to sort the elements by.
# The key function is applied to each element and the results are compared to establish the order.
# To reverse the order, use the reverse=True argument.
print(sorted(L, reverse=True))

 # Lists of tuples can be sorted, too.
dates = [(1910, 10, 5, 'Republic'),
         (1974, 4, 25, 'Liberty'),
         (1640, 12, 1, 'Independence')]
print(sorted(dates))                        # "lexicographic" order

# Tuples are compared like strings: left-to-right.
# For a different order, use the key argument.

sorted(dates, key=lambda e: e[3])           #by name
sorted(dates, key=lambda t: (t[1], t[2]) )     #by month,day

#We're using lambda expressions here!

def LerJogadoresParaLista():
    f = open("JOGADORES.CSV", "rt", encoding="utf-8")
    jogadores = f.readline()    # lê linha cabeçalho
    jogadores = f.readlines()
    lista = []
    for x in jogadores:
        x = x.rstrip('\n')
        v = x.split(";")
        numero, nome, eMail, contacto, dataInsercao = x.split(";")
        lista.append((numero, nome, eMail, contacto, dataInsercao))
        # lista.append([numero, nome, eMail, contacto, dataInsercao])
    return lista

#[('1704920', 'Alexandre Rossa Soares Da Rocha', '', '9368', '2020-11-23 19:38:29'),
# ('1702119', 'Alexandre Terras Simões', 'ats05062000@hotmail.com', '9639', '2020-11-23 19:38:33'),
# ...
# ]

def PrintTop(lista, top):
    t = 0
    print("=" * 20)
    print("Top: %d" % top)
    print("{:<8}{:<45}{:35}{:10}{:20}".format("Número", "Nome", "E-Mail", "Contacto", "Data Inserção"))
    for x in lista:
        numero, nome, eMail, contacto, dataInsercao = x
        print("{:<8}{:<45}{:35}{:10}{:20}".format(numero, nome, eMail, contacto, dataInsercao))
        t = t + 1
        if t == top-1:
            break

    n = len(lista)
    if (t < n-1):
        numero, nome, eMail, contacto, dataInsercao = lista[n-1]
        print("...")
        print("{:<8}{:<45}{:35}{:10}{:20}".format(numero, nome, eMail, contacto, dataInsercao))

L = LerJogadoresParaLista()
top = 50
PrintTop (L, top)

PrintTop (sorted(L), top)
# PrintTop(sorted(L, key=len), top)              # sort by length

PrintTop(sorted(L, key=lambda t: t[1]), top)  # sort by name
PrintTop(sorted(L, key=lambda t: t[1], reverse=True), top)  # sort by name DESC
PrintTop(sorted(L, key=lambda t: (t[3][:2], t[1])), top)  # sort by ...





def contarJogadoresPorDominioDeEmail():
    # objectivo: Permite criar/escrever uma lista com duas colunas: dominio de Email e quantidade
    #   de utilizadores com conta de email nesse dominio. A lista é ordenada por dominio.
    # Variaveis
    #    Auxiliares
    #        jogadores [n] (Texto T100) - Lista de jogadores
    #        dominios [n] (Texto T20) - Lista de nomes de dominios de email (ex:gmail.com)
    #        qt [n] (Inteiro T4) - Lista com a quantidade de utilizadores com um determinado dominio
    #        tab [n] (Texto T20, Inteiro T4) - Lista composta pelos listas: dominios e qt.
    #    Saída
    #      tab2 [n] (Texto T20, Inteiro T4) - Lista composta pelos listas: dominios e qt ordenada por domínio.
    # Autor:
    ...
    import os
    path = os.getcwd()
    f = open(path.replace(nomeFicheiroJogadores, "rt", encoding="utf-8")
    jogadores = f.readline()  # lê linha cabeçalho
    jogadores = f.readlines()
    n = 0  # número de jogadores
    dominios = []
    qt = []
    n=0
    for x in jogadores:
        x = x.rstrip('\n')
        v = x.split(";")  # vetor com 5 elementos
        numero, nome, eMail, contacto, dataInsercao = x.split(";")
        v = eMail.split("@")
        if len(v) >= 2:
            dominio = v[1].lower()
            if dominio not in dominios:
                dominios.append(dominio)
                qt.append(1)
                n= n + 1
            else:
                i = dominios.index(dominio)
                qt[i] = qt[i] + 1
    print("{:<20}{:4}".format("Domínio", "Quantidade"))
    for i in range(len(dominios)):
        print("{:<20}{:4}".format(dominios[i], qt[i]))

    print("Ordenado por qt")
    print(dominios, qt)
    tab = []
    print("{:<20}{:4}".format("Domínio", "Quantidade"))
    for i in range(len(dominios)):
         tab.append((dominios[i], qt[i]))
    print(tab)
    tab2 = sorted(tab, key=lambda e: e[1], reverse=False)  # por qt
    for i in range(len(tab2)):
        print("{:<20}{:4}".format(tab2[i][0], tab2[i][1]))

    print("Ordenado por domínio")
    tab2 = sorted(tab, key=lambda e: e[0], reverse=False)  # por domínio
    print("{:<20}{:4}".format("Domínio", "Quantidade"))
    for i in range(len(tab2)):
        print("{:<20}{:4}".format(tab2[i][0], tab2[i][1]))

    print("Ordenado por qt + domínio")
    tab2 = sorted(tab, key=lambda e: "%03d" % e[1]+e[0], reverse=False)  # por domínio
    tab2 = sorted(tab, key=lambda e: (e[1], e[0]), reverse=False)  # por domínio
    print("{:<20}{:4}".format("Domínio", "Quantidade"))
    for i in range(len(tab2)):
        print("{:<20}{:4}".format(tab2[i][0], tab2[i][1]))
