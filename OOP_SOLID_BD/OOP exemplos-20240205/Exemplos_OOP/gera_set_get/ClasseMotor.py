# from ClasseMotor import *
# Criar objecto com base em dicionário
# motor = Motor(r['marca'], r['potencia'], r['cilindra'], r['Preço'])
# Criar objecto usando construtor
# motor = Motor('marca', 'potencia', 'cilindra', 'Preço')
class Motor:
	# sets
	def setMarca(self, marca):
		if marca != '':
			self.marca = marca
			return True
		else:
			return False

	def setPotencia(self, potencia):
		if potencia != '':
			self.potencia = potencia
			return True
		else:
			return False

	def setCilindra(self, cilindra):
		if cilindra != '':
			self.cilindra = cilindra
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
	def getPotencia(self):
		return self.potencia
	def getCilindra(self):
		return self.cilindra
	def getPreco(self):
		return self.preco

	# construtor
	def __init__(self, marca, potencia, cilindra, preco):
		self.marca = marca
		self.potencia = potencia
		self.cilindra = cilindra
		self.preco = preco

	def __str__(self):
		return str(self.__dict__)

	def Ficha(self):
		temp = vars(self)
		print('-----------------')
		print('Objeto da classe: Motor')
		print(f'Objeto da classe: {self.__class__.__name__}')
		print(f'Objeto da classe: {self.__class__.__base__}')
		print(f'Objeto da classe: {self.__class__.__bases__}')
		for item in temp:
			c = 25 - len(item)
			print("%s%s : %s" % (item.capitalize(), '.' * c, temp[item]))

	def FichaDicionario(self):
		print('-----------------')
		print('Objeto da classe: Motor')
		print(f'Objeto da classe: {self.__class__.__name__}')
		for k, v in self.__dict__.items():
			c = 25 - len(k)
			print("%s%s : %s" % (k.capitalize(), '.' * c, v))

# motor = Motor('marca', 'potencia', 'cilindra', 'Preço')
# motor.Ficha()
