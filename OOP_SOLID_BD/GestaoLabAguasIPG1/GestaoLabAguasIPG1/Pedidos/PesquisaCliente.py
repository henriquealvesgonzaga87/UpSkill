# Pesquisa nome
import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c
import Menus.Menus
import ValidationData.validators_pt as vdpt
import ValidationData.ValidacaoDados as vd
import Clientes.PesquisaCliente as pc

def PesquisaCliente():
    print('Pesquisas: Pesquisa ID Cliente')
    dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

    # Put the code here to implement the functionality

    idcliente = vd.LerCod2("ID Cliente (enter para continuar)")

    if idcliente is None:
        return

    pos = -1
    while True:
        id, pos = pc.PesquisaEmListaDic(dados["Pedidos"], pos+1, {"CódigoCliente": idcliente})
        if id != None:
            print(pos, id)
            op = input("Continuar pesquisa (s/n)")
            if op == 'n':
                break
        else:
            print(f'O IDCliente {idcliente} não foi encontrado com pedidos')
            return PesquisaCliente()

    Menus.Menus.Pausa('Pesquisa IDCliente')

