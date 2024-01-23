# Vejamos alguns exemplos básicos de operações envolvendo listas.

# Cria uma lista sem nenhum elemento.
# A expressão lista_vazia = list() possui o mesmo efeito.
lista_vazia = []
print("Lista vazia: ", lista_vazia)
print("Tipo de uma lista: ", type(lista_vazia))

lista_inteiros = [1, 2, 3, 4]
print("Lista de inteiros: ", lista_inteiros)

lista_tipos_diferentes = ["George", "Orwell", 1984]
print("Lista de elementos com tipos diferentes: ", lista_tipos_diferentes)

lista = [(15, 'Ana Marisa Fonseca Couto'), (1, 'Bruno Isabel Mendes Belo'), (2, 'Guilherme Miguel Pontes de Melo'), (3, 'Henrique Nogueira Pereira'), (4, 'Inês José Alves Gonzaga'), (10, 'João Alexandra Gomes Araújo'), (5, 'João Saraiva de Castro'), (11, 'João Ângelo Dias Augusto'), (8, 'Julien Pedro Gonçalves Rodrigues'), (6, 'Lígia Filipe da Silva Matos'), (7, 'Miguel Paulo de Assunção Silva'), (9, 'Patrick Alexandre Pereira Batista'), (12, 'Pedro José Tomé Monteiro'), (13, 'Rodrigo Miguel Guerra Paraíso'), (14, 'Sandra Augusto Soares Ferreira')]

nums = lista[:][:1]
nomes = lista[:]
print("nums nomes")
print(nums)
print(nomes)

# ordenação por todas as colunas
lista2=sorted(lista)
print(lista2)

#ordenação 1 coluna
lista2=sorted(lista, key=lambda x: x[0])
print(lista)

#ordenação 2 coluna
lista2=sorted(lista, key=lambda x: x[1])
print(lista)

#ordenação tamanho do nome (2º coluna)
lista=sorted(lista, key=lambda x: len(x[1]))
print(lista)



exit()
lista = [
    (1, 'Ana Isabel Mendes Belo'),
    (2, 'Bruno Miguel Pontes de Melo'),
    (3, 'Guilherme Nogueira Pereira'),
    (4, 'Henrique José Alves Gonzaga'),
    (5, 'Inês Saraiva de Castro'),
    (6, 'João Filipe da Silva Matos'),
    (10, 'Lígia Alexandra Gomes Araújo'),
    (7, 'João Paulo de Assunção Silva'),
    (11, 'Miguel Ângelo Dias Augusto'),
    (8, 'João Pedro Gonçalves Rodrigues'),
    (9, 'Julien Alexandre Pereira Batista'),
    (12, 'Patrick José Tomé Monteiro'),
    (13, 'Pedro Miguel Guerra Paraíso'),
    (14, 'Rodrigo Augusto Soares Ferreira'),
    (15, 'Sandra Marisa Fonseca Couto')]

n = len(lista)
lista2 = []
for i in range(n):
    r1 = lista[i % n]
    r2 = lista[(i + 1) % n]
    nomes1 = r1[1].split(' ')
    nomes2 = r2[1].split(' ')
    nome = nomes2[0:1] + nomes1[1:]  # lista
    nome = ' '.join(nome)  # string
    lista2.append((lista[i][0], nome))




