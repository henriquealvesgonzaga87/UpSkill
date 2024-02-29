from models.models import Cliente, TipoProduto, MarcaProduto, Produto, Venda
# fazer um menu para realizar um CRUD chamando as funções do db
# quais queries fazer além do CRUD?
# listar vendas por cliente
# listar vendas por tipo de produtos + lucro por produto
cliente = Cliente()
tipo_produto = TipoProduto()
marca_produto = MarcaProduto()
produto = Produto()
venda = Venda()


def menu_principal():
    while True:
        print("""1 - Menu Clientes
2 - Menu Produtos
3 - Menu Vendas
0 - Sair do programa""")
        opcao_menu = int(input(": "))
        if opcao_menu == 0:
            print("Até breve!")
            exit()
        elif opcao_menu == 1:
            menu_cliente()
        elif opcao_menu == 2:
            menu_produtos()
        elif opcao_menu == 3:
            menu_vendas()
        else:
            print("Opção invalida")


def menu_cliente():
    while True:
        print("""1 - Adicionar cliente
2 - listar clientes
3 - filtra cliente por nome
4 - filtra cliente por sobrenome
5 - filtra por NIF
6 - atualizar cliente
7 - deletar cliente
0 - retornar ao menu principal
e - para sair do programa""")
        opcao = input(": ").lower().strip()
        if opcao == 'e':
            print("até breve")
            exit()
        if int(opcao) == 0:
            menu_principal()
            break
        elif int(opcao) == 1:
            cliente.adicionar()
        elif int(opcao) == 2:
            cliente.lista_clientes()
        elif int(opcao) == 3:
            cliente.filtra_por_nome()
        elif int(opcao) == 4:
            cliente.filtra_por_sobrenome()
        elif int(opcao) == 5:
            cliente.filtra_por_nif()
        elif int(opcao) == 6:
            cliente.atualizar_cliente()
        elif int(opcao) == 7:
            cliente.deletar_cliente()
        else:
            print("Opção invalida")



def menu_produtos():
    while True:
        print("""1 - menu tipos produtos
2 - menu marcas
3 - menu mercadoria
0 - retornar ao menu principal
e - sair do programa""")
        opcao = input(": ")
        if opcao == 'e':
            print("até breve")
            exit()
        if int(opcao) == 0:
            menu_principal()
            break
        elif int(opcao) == 1:
            menu_tipo_produtos()
        elif int(opcao) == 2:
            menu_marca()
        elif int(opcao) == 3:
            menu_mercadoria()
        else:
            print("Opção invalida")


def menu_tipo_produtos():
    while True:
        print("""1 - adicionar tipo de produto
2 - listar todos tipos de produtos
3 - atualizar tipo de produtos
4 - deletar tipo de produto por nome
5 - deletar tipo de produto por id
0 - retornar ao menu anterior
99 - retornar ao menu principal
e - sair do programa""")
        opcao = input(": ")
        if opcao == 'e':
            print("até breve")
            exit()
        if int(opcao) == 0:
            menu_produtos()
            break
        if int(opcao) == 99:
            menu_principal()
            break
        elif int(opcao) == 1:
            tipo_produto.adicionar()
        elif int(opcao) == 2:
            tipo_produto.listar_todos_tipos_produtos()
        elif int(opcao) == 3:
            tipo_produto.atualizar_tipo_produto()
        elif int(opcao) == 4:
            tipo_produto.deletar_por_nome()
        elif int(opcao) == 5:
            tipo_produto.deletar_por_id()
        else:
            print("Opção invalida")


def menu_marca():
    while True:
        print("""1 - adicionar marca
2 - listar marcas
3 - atualizar marca por nome
4 - atualizar marca por ID
5 - deletar marca por nome
6 - deletar marca por ID
0 - retornar ao menu anterior
99 - retornar ao menu principal
e - sair do programa""")
        opcao = input(": ")
        if opcao == 'e':
            print("até breve")
            exit()
        if int(opcao) == 0:
            menu_produtos()
            break
        if int(opcao) == 99:
            menu_principal()
            break
        elif int(opcao) == 1:
            marca_produto.adicionar()
        elif int(opcao) == 2:
            marca_produto.listar()
        elif int(opcao) == 3:
            marca_produto.atualizar_por_nome()
        elif int(opcao) == 4:
            marca_produto.atualizar_por_id()
        elif int(opcao) == 5:
            marca_produto.deletar_por_nome()
        elif int(opcao) == 6:
            marca_produto.deletar_por_id()
        else:
            print("Opção invalida")


def menu_mercadoria():
    while True:
        print("""1 - adicionar produto
2 - consultar todos produtos
3 - consultar produtos por nome
4 - consultar produto por ID
5 - atualizar produto
6 - deletar produto
0 - retornar ao menu anterior
99 - retornar ao menu principal
e - sair do programa""")
        opcao = input(": ")
        if opcao == 'e':
            print("até breve")
            exit()
        if int(opcao) == 0:
            menu_produtos()
            break
        if int(opcao) == 99:
            menu_principal()
            break
        elif int(opcao) == 1:
            produto.adicionar()
        elif int(opcao) == 2:
            produto.consultar_todos_produtos()
        elif int(opcao) == 3:
            produto.consultar_por_nome()
        elif int(opcao) == 4:
            produto.consultar_por_id()
        elif int(opcao) == 5:
            produto.atualizar()
        elif int(opcao) == 6:
            produto.deletar()
        else:
            print("Opção Inválida")


def menu_vendas():
    while True:
        print("""1 - adicionar venda
2 - listar vendas
3 - pesquisar vendas por cliente
4 - pesquisar vendas por produtos
5 - atualizar venda
6 - deletar venda
7 - emitir recibo
0 - retornar ao menu anterior
99 - retornar ao menu principal
e - sair do programa""")
        opcao = input(": ")
        if opcao == 'e':
            print("até breve")
            exit()
        if int(opcao) == 0:
            menu_produtos()
            break
        if int(opcao) == 99:
            menu_principal()
            break
        elif int(opcao) == 1:
            venda.adicionar()
        elif int(opcao) == 2:
            venda.listar_todas_vendas()
        elif int(opcao) == 3:
            venda.listar_venda_por_cliente()
        elif int(opcao) == 4:
            venda.listar_venda_por_produto()
        elif int(opcao) == 5:
            venda.atualizar_venda()
        elif int(opcao) == 6:
            venda.deletar_venda()
        elif int(opcao) == 7:
            venda.recibo()
        else:
            print("Opção inválida!")


menu_principal()
