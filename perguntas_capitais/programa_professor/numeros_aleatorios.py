from random import randint, sample

N = 10
k = 4
numeros = list(range(1, N + 1))
escolhidos = []
while True:
    pessoa_escolhida = randint(1, N)
    if pessoa_escolhida not in escolhidos:
        escolhidos.append(pessoa_escolhida)
    if len(escolhidos) == k:
        break
print(escolhidos)
print(sample(numeros, k))
