# Pesquisa nome
import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c
import Menus.Menus
import ValidationData.validators_pt as vdpt
import ValidationData.ValidacaoDados as vd
import Clientes.PesquisaCliente as pc

def PesquisaTipoAnalise():
    print('Resultados: Pesquisa Tipo Analise')
    dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

    # Put the code here to implement the functionality

    cod = vd.LerCod2("Introduza o código do tipo de analise: (enter para continuar)")

    if cod is None:
        return

    pos = -1
    while True:
        Ctp, pos = pc.PesquisaEmListaDic(dados["Resultados"], pos+1, {"CódigoTipoAnalise": cod})
        if Ctp != None:
            print(pos, Ctp)
            op = input("Continuar pesquisa (s/n)")
            if op == 'n':
                break
        else:
            print(f'O IDTipoAnalise {cod} não foi encontrado')
            return PesquisaTipoAnalise()

    Menus.Menus.Pausa('Pesquisa TipoAnalise')

