from Classe_Python_MySQL_Estrutura_Dados import *

bd = Classe_Python_MySQL_Estrutura_Dados(servidor='localhost',
                                         utilizador='root',
                                         password='root',
                                         base_dados='sakila')


def AtualizarFoto(bd, id, nome_ficheiro_foto):
    def LerFotoParaBinaryData(nome_ficheiro_foto):
        # Convert digital data to binary format
        with open(nome_ficheiro_foto, 'rb') as file:  # rb - binário
            binaryData = file.read()
        return binaryData

    # try:
    foto_bin = LerFotoParaBinaryData(nome_ficheiro_foto)
    cur = bd.mydb.cursor()
    sql = f'UPDATE staff set picture=%s where staff_id=%s'
    result = cur.execute(sql, (foto_bin, id))
    bd.mydb.commit()
    print('Foto inserida na BD')
    return result
    # except Exception as error:
    print('Falha a inserir foto:', error)


# return None

r = AtualizarFoto(bd, 2, 'JonStephens.png')
