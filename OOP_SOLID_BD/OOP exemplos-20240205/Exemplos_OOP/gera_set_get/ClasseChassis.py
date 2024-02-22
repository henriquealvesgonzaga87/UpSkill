# from ClasseChassis import *
# Criar objecto com base em dicionário
# chassis = Chassis(r['Marca'], r['Modelo'], r['Comprimento'], r['Largura'])
# Criar objecto usando construtor
# chassis = Chassis('Marca', 'Modelo', 'Comprimento', 'Largura')
class Chassis:
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

	def setComprimento(self, comprimento):
		if comprimento != '':
			self.comprimento = comprimento
			return True
		else:
			return False

	def setLargura(self, largura):
		if largura != '':
			self.largura = largura
			return True
		else:
			return False

	# gets
	def getMarca(self):
		return self.marca
	def getModelo(self):
		return self.modelo
	def getComprimento(self):
		return self.comprimento
	def getLargura(self):
		return self.largura

	# construtor
	def __init__(self, marca, modelo, comprimento, largura):
		self.marca = marca
		self.modelo = modelo
		self.comprimento = comprimento
		self.largura = largura

	def __str__(self):
		return str(self.__dict__)

	def Ficha(self):
		temp = vars(self)
		print('-----------------')
		print('Objeto da classe: Chassis')
		print(f'Objeto da classe: {self.__class__.__name__}')
		print(f'Objeto da classe: {self.__class__.__base__}')
		print(f'Objeto da classe: {self.__class__.__bases__}')
		for item in temp:
			c = 25 - len(item)
			print("%s%s : %s" % (item.capitalize(), '.' * c, temp[item]))

	def FichaDicionario(self):
		print('-----------------')
		print('Objeto da classe: Chassis')
		print(f'Objeto da classe: {self.__class__.__name__}')
		for k, v in self.__dict__.items():
			c = 25 - len(k)
			print("%s%s : %s" % (k.capitalize(), '.' * c, v))

# chassis = Chassis('Marca', 'Modelo', 'Comprimento', 'Largura')
# chassis.Ficha()
