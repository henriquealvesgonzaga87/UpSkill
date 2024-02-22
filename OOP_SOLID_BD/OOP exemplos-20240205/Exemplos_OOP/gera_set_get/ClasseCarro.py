# from ClasseCarro import *
# Criar objecto com base em dicionário
# carro = Carro(r['Marca'], r['Modelo'], r['Portas'], r['Cilindrada'], r['Potencia'], r['Co2'], r['Cor'], r['Versao'], r['Ano'], r['Mes'], r['Preço'])
# Criar objecto usando construtor
# carro = Carro('Marca', 'Modelo', 'Portas', 'Cilindrada', 'Potencia', 'Co2', 'Cor', 'Versao', 'Ano', 'Mes', 'Preço')
class Carro:
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

	def setPreco(self, preco):
		if preco != '':
			self.preco = preco
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
	def getPreco(self):
		return self.preco

	# construtor
	def __init__(self, marca, modelo, portas, cilindrada, potencia, co2, cor, versao, ano, mes, preco):
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
		self.preco = preco

	def __str__(self):
		return str(self.__dict__)

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
		for k, v in self.__dict__.items():
			c = 25 - len(k)
			print("%s%s : %s" % (k.capitalize(), '.' * c, v))

# carro = Carro('Marca', 'Modelo', 'Portas', 'Cilindrada', 'Potencia', 'Co2', 'Cor', 'Versao', 'Ano', 'Mes', 'Preço')
# carro.Ficha()
