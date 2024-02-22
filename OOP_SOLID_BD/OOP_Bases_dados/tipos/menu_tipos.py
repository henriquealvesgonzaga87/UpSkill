from perguntas_capitais.programa_professor.LerGravarCSV import GravarListaEmFicheiroCSV
# Tipo: sumos, águas, vinhos, sandes
# inserir, alterar, eliminar, consultar (por nome, código, preço, consumo: [hora, dia, dia da semana])
# produtos

def insert_item():
    pass


tipos = dict()

while True:
    print("Tipos de produtos:")
    print("1 - Inserir")
    print("2 - Alterar")
    print("3 - Eliminar")
    print("4 - Listar todos")
    print("0 - Terminar")
    op = int(input("Digite a sua opção: "))
    if op == 0:
        break
    if op == 1:
        chaves = list(tipos.keys())
        if not chaves:
            chave_primaria = 1
        else:
            chave_primaria = max(chaves) + 1
        tipo_produto = input("Informe o tipo de produto: ")
        if tipo_produto in tipos.values():
            print("Produuto já registrado")
        else:
            tipos[chave_primaria] = tipo_produto

print(tipos)
GravarListaEmFicheiroCSV(tipos, 'tipos_produtos', delimitador=';')
