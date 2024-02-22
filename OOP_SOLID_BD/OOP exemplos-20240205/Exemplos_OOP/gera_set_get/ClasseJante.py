# from ClasseJante import *
# Criar objecto com base em dicionário
# jante = Jante(r['Largura'], r['TamanhoDaRoda'], r['NúmeroDeOrifícios'], r['Cor'], r['Preço'])
# Criar objecto usando construtor
# jante = Jante('Largura', 'TamanhoDaRoda', 'NúmeroDeOrifícios', 'Cor', 'Preço')
class Jante:
	# sets
	def setLargura(self, largura):
		if largura != '':
			self.largura = largura
			return True
		else:
			return False

	def setTamanhoDaRoda(self, tamanhoDaRoda):
		if tamanhoDaRoda != '':
			self.tamanhoDaRoda = tamanhoDaRoda
			return True
		else:
			return False

	def setNúmeroDeOrificios(self, númeroDeOrificios):
		if númeroDeOrificios != '':
			self.númeroDeOrificios = númeroDeOrificios
			return True
		else:
			return False

	def setCor(self, cor):
		if cor != '':
			self.cor = cor
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
	def getTamanhoDaRoda(self):
		return self.tamanhoDaRoda
	def getNúmeroDeOrificios(self):
		return self.númeroDeOrificios
	def getCor(self):
		return self.cor
	def getPreco(self):
		return self.preco

	# construtor
	def __init__(self, largura, tamanhoDaRoda, númeroDeOrificios, cor, preco):
		self.largura = largura
		self.tamanhoDaRoda = tamanhoDaRoda
		self.númeroDeOrificios = númeroDeOrificios
		self.cor = cor
		self.preco = preco

	def __str__(self):
		return str(self.__dict__)

	def Ficha(self):
		temp = vars(self)
		print('-----------------')
		print('Objeto da classe: Jante')
		print(f'Objeto da classe: {self.__class__.__name__}')
		print(f'Objeto da classe: {self.__class__.__base__}')
		print(f'Objeto da classe: {self.__class__.__bases__}')
		for item in temp:
			c = 25 - len(item)
			print("%s%s : %s" % (item.capitalize(), '.' * c, temp[item]))

	def FichaDicionario(self):
		print('-----------------')
		print('Objeto da classe: Jante')
		print(f'Objeto da classe: {self.__class__.__name__}')
		for k, v in self.__dict__.items():
			c = 25 - len(k)
			print("%s%s : %s" % (k.capitalize(), '.' * c, v))

# jante = Jante('Largura', 'TamanhoDaRoda', 'NúmeroDeOrifícios', 'Cor', 'Preço')
# jante.Ficha()
