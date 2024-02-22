# Pesquisa nome
import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c
import Menus.Menus
import ValidationData.validators_pt as vdpt
import ValidationData.ValidacaoDados as vd
import Clientes.PesquisaCliente as pc


def PesquisaTipoCliente():
    print('Clientes: Pesquisa IDTipoDeCliente')
    dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

    # Put the code here to implement the functionality

    codtipoa = vd.LerCod2("IDTipoDeCliente (Enter para voltar)")
    if codtipoa is None:
        return

    pos = -1
    while True:
        TipoA, pos = pc.PesquisaEmListaDic(dados["Pedidos"], pos + 1, {"IDTipoCliente": codtipoa})
        if TipoA != None:
            print(pos, TipoA)
            op = input("Continuar pesquisa (s/n)")
            if op == 'n' or op == 'N':
                break
        else:
            print(f'Não foi encontrado nenhum IDTipoDeCliente com {codtipoa}')
            return PesquisaTipoCliente()

    Menus.Menus.Pausa('Pesquisa IDTipoDeCliente')

