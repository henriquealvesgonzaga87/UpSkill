# from ClassePneu import *
# Criar objecto com base em dicionário
# pneu = Pneu(r['Largura'], r['Altura'], r['Diâmetro'], r['Carregamento'], r['Preço'])
# Criar objecto usando construtor
# pneu = Pneu('Largura', 'Altura', 'Diâmetro', 'Carregamento', 'Preço')
class Pneu:
	# sets
	def setLargura(self, largura):
		if largura != '':
			self.largura = largura
			return True
		else:
			return False

	def setAltura(self, altura):
		if altura != '':
			self.altura = altura
			return True
		else:
			return False

	def setDiametro(self, diametro):
		if diametro != '':
			self.diametro = diametro
			return True
		else:
			return False

	def setCarregamento(self, carregamento):
		if carregamento != '':
			self.carregamento = carregamento
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
	def getLargura(self):
		return self.largura
	def getAltura(self):
		return self.altura
	def getDiametro(self):
		return self.diametro
	def getCarregamento(self):
		return self.carregamento
	def getPreco(self):
		return self.preco

	# construtor
	def __init__(self, largura, altura, diametro, carregamento, preco):
		self.largura = largura
		self.altura = altura
		self.diametro = diametro
		self.carregamento = carregamento
		self.preco = preco

	def __str__(self):
		return str(self.__dict__)

	def Ficha(self):
		temp = vars(self)
		print('-----------------')
		print('Objeto da classe: Pneu')
		print(f'Objeto da classe: {self.__class__.__name__}')
		print(f'Objeto da classe: {self.__class__.__base__}')
		print(f'Objeto da classe: {self.__class__.__bases__}')
		for item in temp:
			c = 25 - len(item)
			print("%s%s : %s" % (item.capitalize(), '.' * c, temp[item]))

	def FichaDicionario(self):
		print('-----------------')
		print('Objeto da classe: Pneu')
		print(f'Objeto da classe: {self.__class__.__name__}')
		for k, v in self.__dict__.items():
			c = 25 - len(k)
			print("%s%s : %s" % (k.capitalize(), '.' * c, v))

# pneu = Pneu('Largura', 'Altura', 'Diâmetro', 'Carregamento', 'Preço')
# pneu.Ficha()
