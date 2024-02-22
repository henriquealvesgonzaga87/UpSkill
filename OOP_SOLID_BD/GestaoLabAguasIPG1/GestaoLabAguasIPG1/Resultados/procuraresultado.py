import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c
import Menus.Menus
import ValidationData.validators_pt as vdpt
import ValidationData.ValidacaoDados as vd
import Clientes.PesquisaCliente as pc

def procuraresultado():
    dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

    codA = vd.LerCod2("Código da Analise (enter para continuar)")

    if codA is None:
        return

    pos = -1
    while True:
        pr, pos = pc.PesquisaEmListaDic(dados["Resultados"], pos + 1, {"Código": codA})
        if pr != None:
            print(pr["Resultado"])
            op = input("Continuar pesquisa (s/n)")
            if op == 'n':
                break
        else:
            print(f'Não existe nenhuma Analise com o código {codA}')
            return procuraresultado()
        break

    Menus.Menus.Pausa('Pesquisa IDCliente')