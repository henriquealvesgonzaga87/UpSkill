# from ClasseCarroUsado import *
# Criar objecto com base em dicionário
# carrousado = CarroUsado(r['Matricula'], r['Estado'], r['NumeroDeRegistos'], r['Preço'])
# Criar objecto usando construtor
# carrousado = CarroUsado('Matricula', 'Estado', 'NumeroDeRegistos', 'Preço')
class CarroUsado:
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

	def setPreco(self, preco):
		if preco != '':
			self.preco = preco
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
	def getPreco(self):
		return self.preco

	# construtor
	def __init__(self, matricula, estado, numeroDeRegistos, preco):
		self.matricula = matricula
		self.estado = estado
		self.numeroDeRegistos = numeroDeRegistos
		self.preco = preco

	def __str__(self):
		return str(self.__dict__)

	def Ficha(self):
		temp = vars(self)
		print('-----------------')
		print('Objeto da classe: CarroUsado')
		print(f'Objeto da classe: {self.__class__.__name__}')
		print(f'Objeto da classe: {self.__class__.__base__}')
		print(f'Objeto da classe: {self.__class__.__bases__}')
		for item in temp:
			c = 25 - len(item)
			print("%s%s : %s" % (item.capitalize(), '.' * c, temp[item]))

	def FichaDicionario(self):
		print('-----------------')
		print('Objeto da classe: CarroUsado')
		print(f'Objeto da classe: {self.__class__.__name__}')
		for k, v in self.__dict__.items():
			c = 25 - len(k)
			print("%s%s : %s" % (k.capitalize(), '.' * c, v))

# carrousado = CarroUsado('Matricula', 'Estado', 'NumeroDeRegistos', 'Preço')
# carrousado.Ficha()
