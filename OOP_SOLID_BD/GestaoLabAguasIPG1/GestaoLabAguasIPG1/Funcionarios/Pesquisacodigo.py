# Pesquisa nome
import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c
import Menus.Menus
import ValidationData.validators_pt as vdpt
import ValidationData.ValidacaoDados as vd
import Clientes.PesquisaCliente as pc


def Pesquisacódigo():
    print('Funcionarios: Pesquisa Departamento')
    dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

    # Put the code here to implement the functionality

    codigo = vd.LerCod2("Departamento (Enter para voltar)")
    if codigo is None:
        return

    pos = -1
    while True:
        pes, pos = pc.PesquisaEmListaDic(dados["Funcionários"], pos + 1, {"IDDepartamento": codigo})
        if pes != None:
            print(pos, pes)
            op = input("Continuar pesquisa (s/n)")
            if op == 'n' or op == 'N':
                break
        else:
            print(f'Não foi encontrado nenhum Funcionario com {codigo}')
            return Pesquisacódigo()

    Menus.Menus.Pausa('Pesquisa Cliente')

