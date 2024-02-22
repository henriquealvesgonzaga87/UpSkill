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
        Resultado, pos = pc.PesquisaEmListaDic(dados["Resultados"], pos+1, {"Data": Data})
        if Resultado != None:
            print(pos, Resultado)
            op = input("Continuar pesquisa (s/n)")
            if op == 'n':
                break
        else:
            print(f'A data {Data} não foi encontrada')
            return PesquisaData()

    Menus.Menus.Pausa('Pesquisa Data')

