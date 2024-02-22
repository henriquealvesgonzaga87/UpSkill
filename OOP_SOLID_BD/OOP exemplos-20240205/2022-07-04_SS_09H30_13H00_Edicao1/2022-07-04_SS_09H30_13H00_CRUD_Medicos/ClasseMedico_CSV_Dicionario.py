import csv, os, shutil, datetime


class CMedico:
    def __init__(self, nome_ficheiro):
        self.medicos = {}
        self.nome_ficheiro = nome_ficheiro
    # TODO: iterator
    # class csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)¶
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

    #for row in reader: print(row["Número"], row["Nome"])

    def GravarDicionarioCSV(self, nome_ficheiro=None):
        if nome_ficheiro is None:
            nome_ficheiro = self.nome_ficheiro
        with open(nome_ficheiro, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Nome', 'Especialidade', 'Instituição','Cédula Número','Número Ordem','Data Nascimento']
            writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
            writer.writeheader()
            for r in self.medicos.values():
                writer.writerow(r)
                # print(r)
                # {'Nome': 'Vânia Carina Dias de Oliveira', 'Especialidade': 'Cirurgia Pediátrica', 'Instituição': 'Centro Hospitalar Universitário de Lisboa Norte, E. P. E.', 'Cédula Número': '70004', 'Número Ordem': '948'}

    def Display(self):
        temp = vars(self)
        for item in temp:
            print("%-25s : %s" % (item, temp[item]))

    def ToString(self):
        return self.__dict__.copy()

    def PrintDict(self, dict):
        print('-----------------')
        for k, v in dict.items():
            print("%-15s : %s" % (k, v))

    def ListarMedicos(self):
        for k, v in self.medicos.items():
            print(k, v)

    def ListarMedicosFicha(self):
        for k, v in self.medicos.items():
            self.PrintDict(v)

    def Eliminar(self):
        print("-- E L I M I N A R -- ")
        nome_eliminar = input("Nome?")
        n = 0  # número de
        for k, v in self.medicos.items():
            if v['Nome'].find(nome_eliminar) >= 0:
                self.PrintDict(v)
                op = input("Eliminar  (0-Abortar, 1-Eliminar 2-Continuar pesquisa)?")
                if op == '0':
                    break
                elif op == '1':
                    # Using pop() to remove a dict. pair
                    # removes Mani
                    medico_eliminado = self.medicos.pop(v['Cédula Número'])
                    print("Médico eliminado:")
                    self.PrintDict(medico_eliminado)
                    # https://pythonguides.com/python-copy-file/
                    nome_ficheiro_copia = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_Eliminar_") + self.nome_ficheiro
                    self.CopiaFicheiro(nome_ficheiro_copia)
                    self.GravarDicionarioCSV(self.nome_ficheiro)
                    break

    def Alterar(self):
        print("-- A L T E R A R -- ")
        nome = input("Nome?")
        n = 0  # número de
        for k, v in self.medicos.items():
            if v['Nome'].find(nome) >= 0:
                self.PrintDict(v)
                op = input("Alterar  (0-Abortar, 1-Alterar 2-Continuar pesquisa)?")
                if op == '0':
                    break
                elif op == '1':
                    nome = input("Novo nome?")
                    v['Nome'] = nome
                    # ... restantes dados
                    self.medicos[v['Cédula Número']] = v
                    print("Médico alterado:")
                    self.PrintDict(v)
                    nome_ficheiro_copia = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_Alterar_") + self.nome_ficheiro
                    self.CopiaFicheiro(nome_ficheiro_copia)
                    self.GravarDicionarioCSV(self.nome_ficheiro)
                    break

    def CopiaFicheiro(self, destino):
        shutil.copyfile(self.nome_ficheiro, destino)


medicos = CMedico("medicos.csv")
# medicos.LerCSVDicionario("medicos.csv")
medicos.LerCSVDicionario()
# medicos.GravarDicionarioCSV("medicos_gravado.csv")
#  {'Nome': 'Abel António Rocha Branco', 'Especialidade': 'Medicina Interna', 'Instituição': 'Hospital Distrital de Santarém, E.P.E.', 'Cédula Número': '63531', 'Número Ordem': '1900', '':''}
# medicos.ListarMedicos()
# medicos.ListarMedicosFicha()

# medicos.Eliminar()
medicos.Alterar()


# https://nortemedico.pt/srnom/medicos-e-especialidades/regulamentos/listagem-das-especialidades-medicas

# listas PDF
# 2021 https://www.iasaude.pt/attachments/article/8407/Lista%20de%20M%C3%A9dicos%20Convencionados%20atualizada%20em%2012%20de%20agosto%20de%202021.pdf
# 2018: 45 páginas: https://www.acss.min-saude.pt/wp-content/uploads/2016/09/Lista-Provisoria-Colocados-IM-2018-FE.pdf
# 2021: 42 páginas: https://www.acss.min-saude.pt/wp-content/uploads/2016/09/Lista-provisoria-colocados_Formacao-especializada_IM-2021-FE.pdf

# dados para gráficos
# https://www.pordata.pt/Portugal/M%C3%A9dicos+n%C3%A3o+especialistas+e+especialistas+por+especialidade-147
