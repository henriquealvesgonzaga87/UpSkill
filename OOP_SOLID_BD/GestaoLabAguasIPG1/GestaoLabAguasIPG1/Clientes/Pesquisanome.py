# Pesquisa nome
import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c
import Menus.Menus
import ValidationData.validators_pt as vdpt
import ValidationData.ValidacaoDados as vd
import Clientes.PesquisaCliente as pc

def Pesquisanome():
    print('Clientes: Pesquisa nome')
    dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

    # Put the code here to implement the functionality

    Nome = vd.LerNome2("Nome (enter para continuar)")

    if Nome is None:
        return

    pos = -1
    while True:
        Cliente, pos = pc.PesquisaEmListaDic(dados["Clientes"], pos+1, {"Nome": Nome})
        if Cliente != None:
            print(pos, Cliente)
            op = input("Continuar pesquisa (s/n)")
            if op == 'n':
                break
        else:
            print(f'O nome {Nome} não foi encontrado')
            return Pesquisanome()

    Menus.Menus.Pausa('Pesquisa nome')

