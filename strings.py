def gerar_string(n1, n2):
    s = '.' * n1
    u = s + 'X' * (n2 - n1)
    v = u + '.' * (23 - n2 + 1)
    x = f"{n1:02}:{n2:02} " + v
    return x


print(gerar_string(1, 4))
print(gerar_string(2, 5))
print(gerar_string(10, 14))


def gera_horas(h1, h2):
    pass


def escreve_horas(h1, h2):
    pass


def sobreposicao_intervalos(i1, i2):
    x1, x2 = i1
    y1, y2 = i2
    return max(x1, y1) < min(x2, y2)


print(sobreposicao_intervalos((10, 12), (11, 13)))
