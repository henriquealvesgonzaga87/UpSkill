# from ClasseCarrocaria import *
# Criar objecto com base em dicionário
# carrocaria = Carrocaria(r['Modelo'], r['capô'], r['portas'], r['painéis'], r['habitáculo'])
# Criar objecto usando construtor
# carrocaria = Carrocaria('Modelo', 'capô', 'portas', 'painéis', 'habitáculo')
class Carrocaria:
	# sets
	def setModelo(self, modelo):
		if modelo != '':
			self.modelo = modelo
			return True
		else:
			return False

	def setCapo(self, capo):
		if capo != '':
			self.capo = capo
			return True
		else:
			return False

	def setPortas(self, portas):
		if portas != '':
			self.portas = portas
			return True
		else:
			return False

	def setPaineis(self, paineis):
		if paineis != '':
			self.paineis = paineis
			return True
		else:
			return False

	def setHabitaculo(self, habitaculo):
		if habitaculo != '':
			self.habitaculo = habitaculo
			return True
		else:
			return False

	# gets
	def getModelo(self):
		return self.modelo
	def getCapo(self):
		return self.capo
	def getPortas(self):
		return self.portas
	def getPaineis(self):
		return self.paineis
	def getHabitaculo(self):
		return self.habitaculo

	# construtor
	def __init__(self, modelo, capo, portas, paineis, habitaculo):
		self.modelo = modelo
		self.capo = capo
		self.portas = portas
		self.paineis = paineis
		self.habitaculo = habitaculo

	def __str__(self):
		return str(self.__dict__)

	def Ficha(self):
		temp = vars(self)
		print('-----------------')
		print('Objeto da classe: Carrocaria')
		print(f'Objeto da classe: {self.__class__.__name__}')
		print(f'Objeto da classe: {self.__class__.__base__}')
		print(f'Objeto da classe: {self.__class__.__bases__}')
		for item in temp:
			c = 25 - len(item)
			print("%s%s : %s" % (item.capitalize(), '.' * c, temp[item]))

	def FichaDicionario(self):
		print('-----------------')
		print('Objeto da classe: Carrocaria')
		print(f'Objeto da classe: {self.__class__.__name__}')
		for k, v in self.__dict__.items():
			c = 25 - len(k)
			print("%s%s : %s" % (k.capitalize(), '.' * c, v))

# carrocaria = Carrocaria('Modelo', 'capô', 'portas', 'painéis', 'habitáculo')
# carrocaria.Ficha()
