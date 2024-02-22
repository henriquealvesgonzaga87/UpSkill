from Classe_Python_MySQL_Estrutura_Dados import *

bd = Classe_Python_MySQL_Estrutura_Dados(servidor='localhost',
                                         utilizador='root',
                                         password='root',
                                         base_dados='sakila')


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:  # wb - binário
        file.write(data)


def VerFoto(fotoEmBinario):
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import io
    fp = io.BytesIO(fotoEmBinario)
    img = mpimg.imread(fp)  # , format='jpeg'
    plt.imshow(img)
    plt.show()


staff_id = 1
nome_ficheiro = f'{staff_id}.png'
# ScalarData: Ler um campo de um registo
foto = bd.getScalarData(f'select picture from staff where staff_id={staff_id};')
# grava em disco
write_file(foto, nome_ficheiro)
# mostra
VerFoto(foto)
