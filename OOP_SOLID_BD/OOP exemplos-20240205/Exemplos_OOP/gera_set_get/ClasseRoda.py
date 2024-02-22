# from ClasseRoda import *
# Criar objecto com base em dicionário
# roda = Roda(r['Jante'], r['Pneu'], r['Preço'])
# Criar objecto usando construtor
# roda = Roda('Jante', 'Pneu', 'Preço')
class Roda:
	# sets
	def setJante(self, jante):
		if jante != '':
			self.jante = jante
			return True
		else:
			return False

	def setPneu(self, pneu):
		if pneu != '':
			self.pneu = pneu
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
	def getJante(self):
		return self.jante
	def getPneu(self):
		return self.pneu
	def getPreco(self):
		return self.preco

	# construtor
	def __init__(self, jante, pneu, preco):
		self.jante = jante
		self.pneu = pneu
		self.preco = preco

	def __str__(self):
		return str(self.__dict__)

	def Ficha(self):
		temp = vars(self)
		print('-----------------')
		print('Objeto da classe: Roda')
		print(f'Objeto da classe: {self.__class__.__name__}')
		print(f'Objeto da classe: {self.__class__.__base__}')
		print(f'Objeto da classe: {self.__class__.__bases__}')
		for item in temp:
			c = 25 - len(item)
			print("%s%s : %s" % (item.capitalize(), '.' * c, temp[item]))

	def FichaDicionario(self):
		print('-----------------')
		print('Objeto da classe: Roda')
		print(f'Objeto da classe: {self.__class__.__name__}')
		for k, v in self.__dict__.items():
			c = 25 - len(k)
			print("%s%s : %s" % (k.capitalize(), '.' * c, v))

# roda = Roda('Jante', 'Pneu', 'Preço')
# roda.Ficha()
