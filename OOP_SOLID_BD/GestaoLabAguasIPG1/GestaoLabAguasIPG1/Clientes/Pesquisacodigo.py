# Pesquisa nome
import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c
import Menus.Menus
import ValidationData.validators_pt as vdpt
import ValidationData.ValidacaoDados as vd
import Clientes.PesquisaCliente as pc


def Pesquisacódigo():
    print('Clientes: Pesquisa IDTipoDeCliente')
    dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

    # Put the code here to implement the functionality

    codigo = vd.LerCod2("IDTipoDeCliente (Enter para voltar)")
    if codigo is None:
        return

    pos = -1
    while True:
        Cliente, pos = pc.PesquisaEmListaDic(dados["Clientes"], pos + 1, {"IDTipoCliente": codigo})
        if Cliente != None:
            print(pos, Cliente)
            op = input("Continuar pesquisa (s/n)")
            if op == 'n' or op == 'N':
                break
        else:
            print(f'Não foi encontrado nenhum Cliente com {codigo}')
            return Pesquisacódigo()

    Menus.Menus.Pausa('Pesquisa Cliente')

