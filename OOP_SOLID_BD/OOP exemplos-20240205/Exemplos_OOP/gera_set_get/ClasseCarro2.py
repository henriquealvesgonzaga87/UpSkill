# from ClasseCarro2 import *
# Criar objecto com base em dicionário
# carro2 = Carro2(r['Marca'], r['Modelo'], r['Rodas'], r['Motor'], r['Chassis'], r['Carrocaria'], r['Preço'])
# Criar objecto usando construtor
# carro2 = Carro2('Marca', 'Modelo', 'Rodas', 'Motor', 'Chassis', 'Carrocaria', 'Preço')
class Carro2:
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

	def setRodas(self, rodas):
		if rodas != '':
			self.rodas = rodas
			return True
		else:
			return False

	def setMotor(self, motor):
		if motor != '':
			self.motor = motor
			return True
		else:
			return False

	def setChassis(self, chassis):
		if chassis != '':
			self.chassis = chassis
			return True
		else:
			return False

	def setCarrocaria(self, carrocaria):
		if carrocaria != '':
			self.carrocaria = carrocaria
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
	def getRodas(self):
		return self.rodas
	def getMotor(self):
		return self.motor
	def getChassis(self):
		return self.chassis
	def getCarrocaria(self):
		return self.carrocaria
	def getPreco(self):
		return self.preco

	# construtor
	def __init__(self, marca, modelo, rodas, motor, chassis, carrocaria, preco):
		self.marca = marca
		self.modelo = modelo
		self.rodas = rodas
		self.motor = motor
		self.chassis = chassis
		self.carrocaria = carrocaria
		self.preco = preco

	def __str__(self):
		return str(self.__dict__)

	def Ficha(self):
		temp = vars(self)
		print('-----------------')
		print('Objeto da classe: Carro2')
		print(f'Objeto da classe: {self.__class__.__name__}')
		print(f'Objeto da classe: {self.__class__.__base__}')
		print(f'Objeto da classe: {self.__class__.__bases__}')
		for item in temp:
			c = 25 - len(item)
			print("%s%s : %s" % (item.capitalize(), '.' * c, temp[item]))

	def FichaDicionario(self):
		print('-----------------')
		print('Objeto da classe: Carro2')
		print(f'Objeto da classe: {self.__class__.__name__}')
		for k, v in self.__dict__.items():
			c = 25 - len(k)
			print("%s%s : %s" % (k.capitalize(), '.' * c, v))

# carro2 = Carro2('Marca', 'Modelo', 'Rodas', 'Motor', 'Chassis', 'Carrocaria', 'Preço')
# carro2.Ficha()
