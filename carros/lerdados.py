import csv

# lista = []
# with open('carros.txt', 'rt', newline='', encoding='utf -8') as f:
#     reader = csv.reader(f, delimiter=';')
#     for r in reader:
#         lista.append(r)
# # for linha in lista:
# #     print(linha)
# for i, v in enumerate(lista):
#     print(f"{v[0]} : {v[1]} - {v[2]} - {v[3]} - {v[4]} - {v[5]}")


def lerdados(nome_arquivo):
    lista = []
    with open(nome_arquivo, 'rt', newline='', encoding='utf -8') as f:
        reader = csv.reader(f, delimiter=';')
        reader.__next__()  # ignora o cabeçalho, salta a linha
        for r in reader:
            lista.append(r)
    return lista


carros = lerdados('carros.txt')
