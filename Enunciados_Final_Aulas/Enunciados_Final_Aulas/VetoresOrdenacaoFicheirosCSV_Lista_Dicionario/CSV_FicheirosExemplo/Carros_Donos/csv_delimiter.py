def SavePresencasCSV(presencas, out_dir, base_filename):
    import csv, os
    file_name = os.path.join(out_dir, base_filename)
    with open(file_name, 'w', newline='',  encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL, quotechar='|')
        writer.writerows(presencas)

def ReadPresencasCSV(out_dir, base_filename):
    import csv, os
    presencas = []
    file_name = os.path.join(out_dir, base_filename)
    with open(file_name, 'r', newline='',  encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';', quotechar='|')
        for r in reader:
            presencas.append(tuple(r))
    return presencas

presencas = [(1,'Ana','Presente'),(2,'Beta','Faltou')]
print(presencas)
SavePresencasCSV(presencas, "", 'presencas.csv')
p = ReadPresencasCSV("", 'presencas.csv')
print(p)
p = ReadPresencasCSV("", 'carros.txt')
print(p)
p = ReadPresencasCSV("", 'donos.txt')
print(p)

