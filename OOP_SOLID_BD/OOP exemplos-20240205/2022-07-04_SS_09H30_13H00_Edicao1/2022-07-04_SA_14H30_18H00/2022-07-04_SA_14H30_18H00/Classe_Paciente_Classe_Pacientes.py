import csv, os
from datetime import datetime


class Paciente:
    # construtor
    # Número;Nome;ViaVerde;EMail;Telemovel;NIF;NCC;NISS;DataNascimento
    # sets
    def setNumero(self, numero):
        self.numero = numero

    def setNome(self, nome):
        self.nome = nome

    def setViaVerde(self, viaVerde):
        self.viaVerde = viaVerde

    def setEMail(self, eMail):
        self.eMail = eMail

    def setTelemovel(self, telemovel):
        self.telemovel = telemovel

    def setNIF(self, nIF):
        self.nIF = nIF

    def setNCC(self, nCC):
        self.nCC = nCC

    def setNISS(self, nISS):
        self.nISS = nISS

    def setDataNascimento(self, dataNascimento):
        self.dataNascimento = dataNascimento

    # gets
    def getNumero(self):
        return self.numero

    def getNome(self):
        return self.nome

    def getViaVerde(self):
        return self.viaVerde

    def getEMail(self):
        return self.eMail

    def getTelemovel(self):
        return self.telemovel

    def getNIF(self):
        return self.nIF

    def getNCC(self):
        return self.nCC

    def getNISS(self):
        return self.nISS

    def getDataNascimento(self):
        return self.dataNascimento

    # construtor
    def __init__(self, numero, nome, viaVerde, eMail, telemovel, nIF, nCC, nISS, dataNascimento):
        self.numero = numero
        self.nome = nome
        self.viaVerde = viaVerde
        self.eMail = eMail
        self.telemovel = telemovel
        self.nIF = nIF
        self.nCC = nCC
        self.nISS = nISS
        self.dataNascimento = dataNascimento
    def ToString(self):
        return self.__dict__.copy()

    def Ficha(self):
        temp = vars(self)
        print('-----------------')
        for item in temp:
            c = 25 - len(item)
            print("%s%s : %s" % (item.capitalize(), '.' * c, temp[item]))

d = datetime.strptime('1994-08-02', "%Y-%m-%d")
p = Paciente('3','Rita Ferro Clementino Rego Arantes Carvalheira Rosado','19954-561',
             'ritarfcracr@hotmail.com','961086556', '258192642', '25257606','30156949375', d)
p.Ficha()


class Pacientes:
    def __init__(self, nome_ficheiro):
        self.pacientes = []     # lista de objectos da class Medico
        self.nome_ficheiro = nome_ficheiro

    def LerCSVDicionario(self, nome_ficheiro=None):
        self.pacientes = []
        if nome_ficheiro is None:
            nome_ficheiro = self.nome_ficheiro
        with open(nome_ficheiro, 'r', newline='') as f:   #encoding='utf-8'
            reader = csv.DictReader(f, delimiter=';')
            for r in reader:
                # Criar objecto com base em dicionário
                d = datetime.strptime(r['DataNascimento'], "%Y-%m-%d")
                p = Paciente(r['Número'], r['Nome'], r['ViaVerde'], r['EMail'], r['Telemovel'],
                             r['NIF'], r['NCC'], r['NISS'], d)
                self.pacientes.append(p)  # load all records - list of objects
        return self.pacientes

    def ListarPacientesFicha(self):
        for p in self.pacientes:
            p.Ficha()

    def ListarPacientesTabela(self):
        for p in self.pacientes:
            print(p.ToString())


    # com lista
    def ListaPacientesPorDominioDeEmail(self):
        dominios = []
        qt = []
        for p in self.pacientes:
            dominio = p.getEMail().split("@")[1]
            if dominio not in dominios:
                dominios.append(dominio)
                qt.append(1)
            else:
                i = dominios.index(dominio)
                qt[i] = qt[i] + 1
        lista = zip(dominios, qt)
        # ordenado por quantidade
        lista = sorted(lista, key=lambda x: x[1], reverse=True)  # por domínio
        total = 0
        print ("Pacientes por domínio de E-Mail:")
        for x in lista:
            c = 25 - len(x[0])
            print(x[0],' ' *c, "%6d" % x[1])
            total += x[1]
            c = 25 - len('Total')
        print('Total', ' ' * c, "%6d" % total)
        return lista

    # con dicionario
    def ListaPacientesPorAnoNascimento(self):
        anos = {}
        for p in self.pacientes:
            ano = p.dataNascimento.year
            if ano in anos.keys():
                anos[ano] += 1
            else:
                anos[ano] = 1
        # ordenado por quantidade
        lista = sorted(anos.items(), key=lambda x: x[1]) # quantidade
        lista = sorted(anos.items(), key=lambda x: x[0]) # ano
        total = 0
        print ("Pacientes por domínio de E-Mail:")
        for x in lista:
            c = 25 - len(str(x[0]))
            print(x[0],' ' *c, "%6d" % x[1])
            total += x[1]
            c = 25 - len('Total')
        print('Total', ' ' * c, "%6d" % total)
        return lista

    def GraficoDominioDeEmail(self, lista):
        import matplotlib.pyplot as plt
        X = []
        Y = []
        for x in lista:
            # X.append(str(x[0])+'\n'+str((x[1])))
            X.append(x[0])
            Y.append(x[1])

        # defining labels
        activities = X
        # portion covered by each label
        slices = Y
        # color for each label
        colors = ['r', 'y', 'g', 'b']

        # plotting the pie chart
        plt.pie(slices, labels = activities, colors=colors,
                startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
                radius = 1.2, autopct = '%1.2f%%',  textprops={'fontsize': 14})

        # plotting legend
        # plt.legend(loc='lower center')
        plt.title('Pacientes por operadora de E-Mail', fontsize=20)
        plt.savefig("GraficoDominioDeEmail.png", format='png', transparent=True)
        # showing the plot
        plt.show()


    def GraficoIdades(self, lista):
        # https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
        import matplotlib.pyplot as plt
        X = []
        Y = []
        for x in lista:
            X.append(x[0])
            Y.append(x[1])
        # x-coordinates of left sides of bars
        left = [i for i in range(1, len(lista)+1)]
        # labels for bars
        tick_label = X # ['one', 'two', 'three', 'four', 'five']
        # plotting a bar chart
        plt.bar(left, Y, tick_label = tick_label,
                width = 0.8, color = ['blue', 'green'])
        # x-axis label
        plt.xlabel('Idade')
        # frequency label
        plt.ylabel('Número de pacientes')
        # plot title
        plt.title('Histograma por Idades')
        plt.yticks(fontsize=14)
        plt.xticks(fontsize=8, rotation=45)

        plt.savefig("Histograma.png", format='png', transparent=True)
        # function to show the plot
        plt.show()


pacientes = Pacientes("pacientes.csv")
pacientes.LerCSVDicionario()
# pacientes.ListarPacientesFicha()
# pacientes.ListarPacientesTabela()
lista = pacientes.ListaPacientesPorDominioDeEmail()
pacientes.GraficoDominioDeEmail(lista)

lista = pacientes.ListaPacientesPorAnoNascimento()
pacientes.GraficoIdades(lista)



