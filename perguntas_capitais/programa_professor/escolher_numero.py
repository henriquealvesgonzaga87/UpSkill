from random import randint, shuffle
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 N = 10
# 2, 5, 7, 1                    k = 4
N = 10
k = 4
numeros = list(range(1, N + 1))
escolhidos = []
resposta = 1
escolhidos.append(resposta)
for i in range(len(numeros)):
    aleatorio = randint(1, len(numeros))
    if aleatorio not in escolhidos:
        escolhidos.append(aleatorio)
    if len(escolhidos) == 4:
        break
shuffle(escolhidos)
print(escolhidos)
