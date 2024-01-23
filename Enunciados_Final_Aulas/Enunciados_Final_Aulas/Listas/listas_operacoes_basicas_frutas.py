frutas = ['Banana', "Maça", "Morango", "Laranjas"]
frutas.append('Pêra')
print(frutas)
# Resultado
# ['Banana', 'Maça', 'Morango', 'Laranjas', 'Pêra']

# adicionar lista
frutas.extend(['Babaco', 'Pitanga'])
print(frutas)
# ['Banana', 'Maça', 'Morango', 'Laranjas', 'Pêra', 'Babaco', 'Pitanga']


frutas = ('Banana', "Maça", "Morango", "Laranjas")
print(type(frutas))
print(frutas)
# Resultado
# <class 'tuple'>
# ['Banana', 'Maça', 'Morango', 'Laranjas', 'Pêra']


# por índice
frutas = ['Banana', 'Maça', 'Morango', 'Laranjas', 'Pêra', 'Babaco', 'Pitanga']
frutas.pop(4)
print(frutas)

# por nome
frutas = ['Banana', 'Maça', 'Morango', 'Laranjas', 'Pêra', 'Babaco', 'Pitanga']
frutas.remove('Pêra')
print(frutas)
# Resultado

# Ordenação. Criação de uma nova lista
frutas = ['Banana', 'Maça', 'Morango', 'Laranjas', 'Pêra', 'Babaco', 'Pitanga']
frutas_ordenadas = sorted(frutas)
print(frutas_ordenadas)
# Resultado
# ['Babaco', 'Banana', 'Laranjas', 'Maça', 'Morango', 'Pitanga', 'Pêra']

# Ordenação da lista (on site)
frutas = ['Banana', 'Maça', 'Morango', 'Laranjas', 'Pêra', 'Babaco', 'Pitanga']
frutas.sort()
print(frutas)
# Resultado
# ['Babaco', 'Banana', 'Laranjas', 'Maça', 'Morango', 'Pitanga', 'Pêra']

# Ordenação da lista (on site) por ordem descendente
frutas = ['Banana', 'Maça', 'Morango', 'Laranjas', 'Pêra', 'Babaco', 'Pitanga']
frutas.sort(reverse=True)
print(frutas)
# Resultado
# ['Pêra', 'Pitanga', 'Morango', 'Maça', 'Laranjas', 'Banana', 'Babaco']


# Ordenação da lista em função do tamanho do nome das frutas
frutas = ['Banana', 'Maça', 'Morango', 'Laranjas', 'Pêra', 'Babaco', 'Pitanga']
frutas.sort(key=lambda e: len(e))
print(frutas)
# Resultado
# ['Maça', 'Pêra', 'Banana', 'Babaco', 'Morango', 'Pitanga', 'Laranjas']

# Ordenação da lista em função do tamanho do nome das frutas + nome
frutas = ['Banana', 'Maça', 'Pitanga', 'Morango', 'Laranjas', 'Pêra', 'Babaco']
frutas.sort(key=lambda e: str(len(e)) + e)
print(frutas)
# Resultado
# ['Maça', 'Pêra', 'Babaco', 'Banana', 'Morango', 'Pitanga', 'Laranjas']

# Juntar listas
codigos = [1, 2, 3, 4, 5, 6, 7]
frutas = ['Banana', 'Maça', 'Morango', 'Laranjas', 'Pêra', 'Babaco', 'Pitanga']
lista_zip = zip(codigos, frutas)
print("lista_zip: não é iterável", lista_zip)
lista = list(lista_zip)
print("Lista", lista)

# Juntar listas
codigos = [1, 2, 3, 4, 5]
frutas = ['Banana', 'Maça', 'Morango', 'Laranjas', 'Pêra', 'Babaco', 'Pitanga']
lista_zip = zip(codigos, frutas)
print("lista_zip: não é iterável", lista_zip)
lista = list(lista_zip)
print("Lista", lista)

print("zip, range")
for item in zip(range(1, len(frutas) + 1), frutas, strict=True):
    print(item)
