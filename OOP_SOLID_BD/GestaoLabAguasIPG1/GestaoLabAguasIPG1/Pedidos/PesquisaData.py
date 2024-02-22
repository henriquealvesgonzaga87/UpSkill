# Pesquisa nome
import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c
import Menus.Menus
import ValidationData.validators_pt as vdpt
import ValidationData.ValidacaoDados as vd
import Clientes.PesquisaCliente as pc

def PesquisaData():
    print('Pesquisa: Pesquisa Data')
    dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

    Data= vd.LerData("Data (enter para continuar)")

    if Data is None:
        return

    pos = -1
    while True:
        Pedido, pos = pc.PesquisaEmListaDic(dados["Pedidos"], pos+1, {"Data": Data})
        if Pedido != None:
            print(pos, Pedido)
            op = input("Continuar pesquisa (s/n)")
            if op == 'n':
                break
        else:
            print(f'A data {Data} não foi encontrada')
            return PesquisaData()

    Menus.Menus.Pausa('Pesquisa Data')

