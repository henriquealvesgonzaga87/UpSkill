import os
def GetListOfFiles(path, ext):
    import glob
    dir_path = fr'{path}\**\*.{ext}'   # ** - subdiretórios
    lista = []
    for file in glob.glob(dir_path, recursive=True):
        lista.append(os.path.basename(file))
    return lista

files = GetListOfFiles(os.getcwd(), 'py')
print(files)
x = "\\subsection{#}"
lst = "\\lstinputlisting[firstline=1,lastline=500,style=python,numbers=left, label={lst:&}, caption={>.}]{#}"
for filename in files:
    y = x.replace("#", filename.rstrip('.py')).replace('_',' ').replace('SobreposicaoIntervalos', 'Sobreposição de Intervalos')
    y2 = filename.rstrip('.py').replace('_','')
    f = f"13_BD\Especialidadess/{filename}"
    f = lst.replace("#", f).replace("&",y2).replace('>',y2)
    print("%-------------")
    print(y)
    print()
    print(f)
    print()

