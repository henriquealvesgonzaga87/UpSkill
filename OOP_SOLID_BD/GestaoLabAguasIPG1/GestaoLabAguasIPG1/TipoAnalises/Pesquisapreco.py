# Pesquisa nome
import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c
import Menus.Menus
import ValidationData.validators_pt as vdpt
import ValidationData.ValidacaoDados as vd
import Clientes.PesquisaCliente as pc


def Pesquisapreco():
    print('PesquisaPreço')
    dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

    # Put the code here to implement the functionality

    preco = vd.LerNumero("Preço (Enter para voltar)", 0, 10000, "naointeiro")
    if preco is None:
        return

    pos = -1
    while True:
        Analise, pos = pc.PesquisaEmListaDic(dados["TipoAnalises"], pos + 1, {"Preço": preco})
        if Analise != None:
            print(pos, Analise)
            op = input("Continuar pesquisa (s/n)")
            if op == 'n' or op == 'N':
                break
        else:
            print(f'Não foi encontrado nenhum IDTipoDeCliente com {preco}')
            return Pesquisapreco()

    Menus.Menus.Pausa('Pesquisa IDTipoDeCliente')

