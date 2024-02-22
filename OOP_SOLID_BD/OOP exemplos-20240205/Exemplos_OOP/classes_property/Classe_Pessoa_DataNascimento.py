from datetime import datetime, timedelta, date
import locale
locale.setlocale(locale.LC_ALL, '')

class Pessoa:
    """ Documentação:
        Várias linhas
    """
    # construtor
    def __init__(self, nome, dataNascimento, email, telemovel):
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.email = email
        self.telemovel = telemovel
    # def __init__(self):
    #     self.nome = "Nome Apelido"
    #     self.dataNascimento = datetime.now()
    #     self.email = 'email@ipg.pt'
    #     self.telemovel = 96123457
    # gets
    def getNome(self):
        return self.nome
    def getNome(self):
        return self.dataNascimento
    def getNome(self):
        return self.email
    def getNome(self):
        return self.telemovel
    # sets
    def setNome(self, nome):
        if nome != '':
            self.nome = nome
    def setDataNascimento(self, dataNascimento):
        agora = datetime.datetime.date()
        if dataNascimento <= agora:
            self.dataNascimento = dataNascimento
    def setEMail(self, email):
        if email != '':
            self.email = email
    def setTelemovel(self, telemovel):
        self.telemovel = telemovel

    # funcionalidades
    def ToString(self):
        return self.__dict__.copy()

    def Ficha(self):
        temp = vars(self)
        print('-----------------')
        for item in temp:
            c = 25 - len(item)
            print("%s%s : %s" % (item.capitalize(), '.' * c, temp[item]))

    def Display(self):
        print('-----------------')
        for k, v in self.__dict__.items():
            print("%-25s : %s" % (k, v))

    def getIniciais(self):
        return ''.join([x[0] for x in self.nome.split()])

    def getPrimeiroNome(self):
        return self.nome.split()[0]

    def getApelido(self):
        return self.nome.split()[-1]

    def getIdade (self):
        hoje = datetime.now()
        return hoje - self.dataNascimento
    def getIdadeDias(self):
        hoje = datetime.now()
        return (hoje - self.dataNascimento).days

    def getIdadeMeses(self):
        hoje = datetime.now()
        return (hoje - self.dataNascimento).days/30

    def getIdadeAnos(self):
        hoje = datetime.now()
        return (hoje - self.dataNascimento).days/365.25

    def getIdadeAnosData(self, data):
        return (data - self.dataNascimento).days/365.25

    # from datetime import datetime
    # print(datetime.min, datetime.max)
    # 0001-01-01 00:00:00 9999-12-31 23:59:59.999999
    def getIdadeAnosCalendario(self):
        hoje = datetime.now()
        return "TODO: SA 05-07-2022"
        # datetime.strptime(f'{anos}-{meses}-{dias}', "%Y-%m-%d")

    def getIdadeAnosMesesDias(self):
        hoje = datetime.now()
        # hoje.year, hoje.month, hoje.day
        return "TODO: SA 05-07-2022"

    def Falar(self, texto):
        pass

    def Info(self):
        print ("Employee.__doc__:", Pessoa.__doc__)
        print ("Employee.__name__:", Pessoa.__name__)
        print ("Employee.__module__:", Pessoa.__module__)
        print ("Employee.__bases__:", Pessoa.__bases__)
        print ("Employee.__dict__:", Pessoa.__dict__)


    def PlayTexto(self, texto):
        import gtts
        from playsound import playsound  # pip install playsound==1.2.2
        nomef = f"{datetime.now().strftime('%Y-%m-%d_%H_%M_%S')}.mp3"
        tts = gtts.gTTS(texto,  lang="pt")
        tts.save(nomef)
        playsound(nomef)


    def ApresentacaoOral(self):
        import gtts
        from playsound import playsound  # pip install playsound==1.2.2
        import time
        # time.sleep(3)
        print('-----------------')
        nomef = f"{self.email}.mp3"
        f = open(nomef, "wb")
        for atributo, valor in self.__dict__.items():
            texto = "%-25s : %s" % (atributo, valor)
            # make request to google to get synthesis
            print(texto)
            tts = gtts.gTTS(texto,  lang="pt")
            tts.write_to_fp(f)
        f.close()
        playsound(nomef)



