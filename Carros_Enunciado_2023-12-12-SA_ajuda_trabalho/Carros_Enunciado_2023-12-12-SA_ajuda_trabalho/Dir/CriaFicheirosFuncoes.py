f = open ("../Programa_Carros.py", "rt", encoding='utf-8')
linhas = f.readlines()
f.close()
import os
for x in linhas:
    if x.startswith("def"):
        fic = x.split('(')[0].split(" ")[1]
        # def ListaMarcaQuantidade(carros, marca):
        # 0 - def ListaMarcaQuantidade
        #     0-def 1-ListaMarcaQuantidade
        # 1 - (carros, marca):
        if os.path.exists(fic):
            os.remove(fic)
        fic = fic + '.py'
        print(x, fic)
        f = open(fic, "wt", encoding='utf-8')
        print(x, file=f, end='')
        print("\tpass", file=f)
        f.close()
