from CRUD_MicrosoftSQLServer_Classe import *

o = CRUDMaisProdutosSQLServer()
o.CopiaBaseDados()
exit()
print(o.Versao())
o.ExecutaComandoSQL('drop table products')
print(o.CriaTabela())

o.InserirDefault()
o.Inserir(100, 'Prod 100', 100)
o.AtualizaPreco(100, 55.25)
o.ListarDadosFormatoTabular()

# inserir
fn = 'ficheiros_dados/ipg.png'
bn = 'ficheiros_dados/empresas.txt'
bn = 'ficheiros_dados/lista.xlsx'
o.Inserir_Foto_Biografia(100, fn, bn)

# ler da BD

# foto e biografia: bytes (binário)
# grava com o nome original
foto, nome_foto, biografia, nome_biografia = o.Ler_Foto_Biografia_GravaFicheiro(100)
o.VerFoto(foto)


# gravar com nomes diferentes e mesma extensão
nome_ficheiro_foto = 'ipg2'              # .png sem extensão
nome_ficheiro_biografia = 'empresas2'    # .txt sem extensão
foto, nome_foto, biografia, nome_biografia = o.Ler_Foto_Biografia_GravaFicheiro(100,
                    nome_ficheiro_foto=nome_ficheiro_foto,
                    nomeFicheiroBio=nome_ficheiro_biografia)
o.VerBiografia(nome_biografia)
# exit()

o.CopiaBaseDados()
# -----------
tabelas = o.getNomesTabelas()
for t in tabelas:
    print(t)
tabela = 'TipoPrato'

campos = o.getCamposTabela(tabela)
for c in campos:
    print(c)

campos_detalhe = o.getEstruturaTabela(tabela)
for c in campos_detalhe:
    print(c)

# r = o.getDadosTabelaLista(tabela)
# for t in tabelas:
#     print(t, o.getCamposTabela(t))
