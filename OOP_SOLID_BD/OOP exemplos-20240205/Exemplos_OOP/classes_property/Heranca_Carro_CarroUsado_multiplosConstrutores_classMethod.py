from typing import Any


class Carro:
    # Marca;Modelo;Portas;Cilindrada;Potencia;Co2;Cor;Versao;Ano;Mes
     # construtor
    # sets

    def setMarca(self, marca):
        if marca != '':
            self.marca = marca
            return True
        else:
            return False

    def setModelo(self, modelo):
        if modelo != '':
            self.modelo = modelo
            return True
        else:
            return False

    def setPortas(self, portas):
        if portas != '':
            self.portas = portas
            return True
        else:
            return False

    def setCilindrada(self, cilindrada):
        if cilindrada != '':
            self.cilindrada = cilindrada
            return True
        else:
            return False

    def setPotencia(self, potencia):
        if potencia != '':
            self.potencia = potencia
            return True
        else:
            return False

    def setCo2(self, co2):
        if co2 != '':
            self.co2 = co2
            return True
        else:
            return False

    def setCor(self, cor):
        if cor != '':
            self.cor = cor
            return True
        else:
            return False

    def setVersao(self, versao):
        if versao != '':
            self.versao = versao
            return True
        else:
            return False

    def setAno(self, ano):
        if ano != '':
            self.ano = ano
            return True
        else:
            return False

    def setMes(self, mes):
        if mes != '':
            self.mes = mes
            return True
        else:
            return False

    # gets
    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

    def getPortas(self):
        return self.portas

    def getCilindrada(self):
        return self.cilindrada

    def getPotencia(self):
        return self.potencia

    def getCo2(self):
        return self.co2

    def getCor(self):
        return self.cor

    def getVersao(self):
        return self.versao

    def getAno(self):
        return self.ano

    def getMes(self):
        return self.mes

    # construtor
    def __init__(self, marca, modelo, portas, cilindrada, potencia, co2, cor, versao, ano, mes):
        self.marca = marca
        self.modelo = modelo
        self.portas = portas
        self.cilindrada = cilindrada
        self.potencia = potencia
        self.co2 = co2
        self.cor = cor
        self.versao = versao
        self.ano = ano
        self.mes = mes

        # construtor
    def __init__(self, marca, modelo='', portas='', cilindrada='', potencia='', co2='', cor='', versao='', ano='', mes=''):
        self.marca = marca
        self.modelo = modelo
        self.portas = portas
        self.cilindrada = cilindrada
        self.potencia = potencia
        self.co2 = co2
        self.cor = cor
        self.versao = versao
        self.ano = ano
        self.mes = mes

    # método de classe. Poder ser chamado sem se criar um objecto:
    # exemplo: datetime.datetime.now(). Foi chamado o médoto now() da classe datetime
    # Permite criar objetos parcialmente preenchidos.
    # A powerful technique for providing multiple constructors in Python is to use @classmethod.
    # This decorator allows you to turn a regular method into a class method.
    @classmethod
    def from_marca_modelo(cls, marca, modelo):
        return cls(marca, modelo, portas='', cilindrada='', potencia='', co2='', cor='', versao='', ano='', mes='')

    def Ficha(self):
        temp = vars(self)
        print('-----------------')
        print('Objeto da classe: Carro')
        print(f'Objeto da classe: {self.__class__.__name__}')
        print(f'Objeto da classe: {self.__class__.__base__}')
        print(f'Objeto da classe: {self.__class__.__bases__}')
        for item in temp:
            c = 25 - len(item)
            print("%s%s : %s" % (item.capitalize(), '.' * c, temp[item]))

    def FichaDicionario(self):
        print('-----------------')
        print('Objeto da classe: Carro')
        print(f'Objeto da classe: {self.__class__.__name__}')
        print(f'Objeto da classe: {self.__class__.__base__}')
        print(f'Objeto da classe: {self.__class__.__bases__}')
        for k, v in self.__dict__.items():
            c = 25 - len(k)
            print("%s%s : %s" % (k.capitalize(), '.' * c, v))


class CarroUsado (Carro):  # CarroUsado extends Carro
    # Matricula;Estado;NumeroDeRegistos

    #  CarroUsado(String Marca, String Modelo, int portas, int cilindrada, int potencia, int Co2, String cor, String versao) {
    #     super(Marca, Modelo, portas, cilindrada, potencia, Co2, cor, versao);
    #
    #
    # public CarroUsado(String Marca, String Modelo, int portas, int cilindrada, int potencia, int Co2, String cor, String versao,int ano, String matricula, String estado) {
    #     super(Marca, Modelo, portas, cilindrada, potencia, Co2, cor, versao);
    #     this.ano = ano;
    #     this.matricula = matricula;
    #     this.estado = estado;
    #
    # construtor
    def __init__(self, marca, modelo, portas, cilindrada, potencia, co2, cor, versao, ano, mes,
                 matricula, estado, numeroDeRegistos):
        ##########################################################################################
        super().__init__(marca, modelo, portas, cilindrada, potencia, co2, cor, versao, ano, mes)
        ##########################################################################################
        self.matricula = matricula
        self.estado = estado
        self.numeroDeRegistos = numeroDeRegistos

    # sets
    def setMatricula(self, matricula):
        if matricula != '':
            self.matricula = matricula
            return True
        else:
            return False

    def setEstado(self, estado):
        if estado != '':
            self.estado = estado
            return True
        else:
            return False

    def setNumeroDeRegistos(self, numeroDeRegistos):
        if numeroDeRegistos != '':
            self.numeroDeRegistos = numeroDeRegistos
            return True
        else:
            return False

    # gets
    def getMatricula(self):
        return self.matricula

    def getEstado(self):
        return self.estado

    def getNumeroDeRegistos(self):
        return self.numeroDeRegistos

    # def Ficha(self):
    #     temp = vars(self)
    #     print('-----------------')
    #     print('Objeto da classe: CarroUsado')
    #     print(f'Objeto da classe: {self.__class__.__name__}')
    #     print(f'Objeto da classe: {self.__class__.__base__}')
    #     print(f'Objeto da classe: {self.__class__.__bases__}')
    #     for item in temp:
    #         c = 25 - len(item)
    #         print("%s%s : %s" % (item.capitalize(), '.' * c, temp[item]))
    #
    # def FichaDicionario(self):
    #     print('-----------------')
    #     print('Objeto da classe: CarroUsado')
    #     print(f'Objeto da classe: {self.__class__.__name__}')
    #     print(f'Objeto da classe: {self.__class__.__base__}')
    #     print(f'Objeto da classe: {self.__class__.__bases__}')
    #     for k, v in self.__dict__.items():
    #         c = 25 - len(k)
    #         print("%s%s : %s" % (k.capitalize(), '.' * c, v))


carro = Carro('Marca', 'Modelo', 'Portas', 'Cilindrada', 'Potencia', 'Co2', 'Cor', 'Versao', 'Ano', 'Mes')
carro.Ficha()

carroUsado = CarroUsado('Marca', 'Modelo', 'Portas', 'Cilindrada', 'Potencia', 'Co2', 'Cor', 'Versao', 'Ano', 'Mes','Matricula', 'Estado', 'NumeroDeRegistos')
carroUsado.Ficha()

carro2 = Carro.from_marca_modelo('Skoda','Octavia')
carro2.Ficha()

carro3 = Carro('BMW')
carro3.Ficha()
carro3 = Carro('BMW', potencia=320)
carro3.Ficha()



# carroUsado = CarroUsado('Matricula', 'Estado', 'NumeroDeRegistos')

print('dir(object)', dir(object))
