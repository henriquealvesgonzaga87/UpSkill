f = open("carros_funcoes.py", "rt", encoding="utf-8")
linhas = f.readlines()
f.close()
for x in linhas:
    if x.startswith("def"):
        fic = x.split('(')[0].split(" ")[1] + '.py'
        print(x, fic)
        f = open(fic, 'wt', encoding='utf-8')
        print(x, file=f)
        print("\tpass", file=f)
