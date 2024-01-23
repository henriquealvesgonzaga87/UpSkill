import csv
def LerDados(nome_ficheiro):
    lista = []
    with open(nome_ficheiro, 'rt', newline='') as f:
        reader = csv.reader(f, delimiter=';')
        reader.__next__()
        for r in reader:
            lista.append(r)
    return lista
def QuantidadeCarrosPorMarca(lista, marca_contar):
    qt = 0  # x = ['44-JH-69', 'Mitsubishi', 'Colt', '1995', '9670417', '2']
    for x in lista:
        marca = x[1]
        if marca == marca_contar:
            qt = qt + 1
    return qt
carros = LerDados('carros.txt')       # len(  )
marca = 'BMW'
qt = QuantidadeCarrosPorMarca(carros, marca)    # 1322
print(f"Quantidade de carros da marca {marca}: {qt} ({qt / len(carros)*100:.2f}%)")
def ListadeMarcas(lista):
    marcas = []
    for x in lista:
        marca = x[1]
        if marca not in marcas:
            marcas.append(marca)
    return marcas

def Listade(lista, coluna):
    r = []
    for x in lista:
        if x[coluna] not in r:
            r.append(x[coluna])
    return r

print(Listade(carros, 3))
exit()


def QuantidadeCarrosPorMarcaTodos(lista):
    r = []
    marcas = ListadeMarcas(lista)
    for m in marcas:
        qt = QuantidadeCarrosPorMarca(lista, m)
        r.append([m, qt])
    return r
print(QuantidadeCarrosPorMarcaTodos(carros))

# lista_marcas = ListadeMarcas(carros)
# lista_marcas_ordenada = sorted(lista_marcas)
# print(lista_marcas_ordenada, len(lista_marcas))

import QuantidaDeCarros
# Quantos carros existem?

qt = QuantidaDeCarros(carros)
print(qt)

f = open("estatisticas.txt", "wt", encoding='UTF-8')
print(qt, file=f)
f.close()
exit()


# Quantidade de carros por pessoa (IDUtente)
def QuantidadeCarrosPorUtente(carros, IDUtente):
    pass

# Lista pessoas (IDUtente) com um dado número de carros?
def ListaPessoasQuantidadeCarros(carros, numero_carros):
    pass

# Marca com mais carros
def MarcaComMaisCarros(carros):
    pass

# Marca com mais carros
def MarcaComMenosCarros(carros):
    pass

# Modelo com mais carros
def ModeloComMaisCarros(carros):
    pass

# Ano com mais carros
def AnoComMaisCarros(carros):
    pass

# Quantidade:
   # carros por um dado ano  
def QuantidadeCarrosDadoAno(carros, ano):
    # lista carros por ano
    pass
def QuantidadeCarrosTodosAnos(carros):
    pass

# Matricula: Listar carros. Todos os dados
#   Começadas por: 88   def MatriculaComecadaPor()
def ListaCarrosMatriculaComecadaPor(carros, texto):
    #   Terminadas por: 89
    pass
def ListaCarrosMatriculaTerminadasPor(carros, texto):
    #  Contem:  HE
    pass
def ListaCarrosMatriculaContem(carros, texto):
    pass

# Modelos:
#   Quantidade
def QuantidadePorModelo(carros, modelo):
    #   Lista ordenada com modelo + qt
    pass
def QuantidadeTodosModelos(carros, modelo):
    pass

#Lista com marca + quantidade ordenada.
def ListaMarcaQuantidade(carros, marca):
    pass
#Lista com marca + modelo + quantidade ordenada
def ListaMarcaModeloQuantidade(carros, marca, modelo):
    pass
