import csv
def LerCSVDicionario(self, nome_ficheiro=None):
    self.medicos = {}
    if nome_ficheiro is None:
        nome_ficheiro = self.nome_ficheiro
    with open(nome_ficheiro, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        for r in reader:
            self.medicos[r['Cédula Número']] = r  # load all records - dict of dicts
        # self.medicos = [r for r in reader]      # load all records - list of dicts
    return self.medicos

    # for row in reader: print(row["Número"], row["Nome"])


def GravarDicionarioCSV(self, nome_ficheiro=None):
    if nome_ficheiro is None:
        nome_ficheiro = self.nome_ficheiro
    with open(nome_ficheiro, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Nome', 'Especialidade', 'Instituição', 'Cédula Número', 'Número Ordem', 'Data Nascimento']
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        for r in self.medicos.values():
            writer.writerow(r)
            # print(r)
            # {'Nome': 'Vânia Carina Dias de Oliveira', 'Especialidade': 'Cirurgia Pediátrica', 'Instituição': 'Centro Hospitalar Universitário de Lisboa Norte, E. P. E.', 'Cédula Número': '70004', 'Número Ordem': '948'}


medicos = LerCSVDicionario("medicos.csv")