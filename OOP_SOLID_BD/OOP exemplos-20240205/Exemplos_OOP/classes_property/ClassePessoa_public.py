# from ClassePessoa import *
# Criar objecto com base em dicionário
# pessoa = Pessoa(r['Nome'], r['Email'], r['Telefone'])
# Criar objecto usando construtor
# pessoa = Pessoa('Nome', 'Email', 'Telefone')
class Pessoa:
	# sets
	def setNome(self, nome):
		if nome != '':
			self.nome = nome
			return True
		else:
			return False

	def ValidaEMail(email):
		import re
		if re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):  # No match
			return True
		return False

	def setEmail(self, email):
		if self.ValidaEMail(email):
			self.email = email
			return True
		else:
			return False

	def setTelefone(self, telefone):
		if telefone != '':
			self.telefone = telefone
			return True
		else:
			return False

	# gets
	def getNome(self):
		return self.nome
	def getEmail(self):
		return self.email
	def getTelefone(self):
		return self.telefone

	# construtor
	def __init__(self, nome, email, telefone):
		self.nome = nome
		self.email = email
		self.telefone = telefone

	def __str__(self):
		return str(self.__dict__)

	def Ficha(self):
		temp = vars(self)
		print('-----------------')
		print('Objeto da classe: Pessoa')
		print(f'Objeto da classe: {self.__class__.__name__}')
		print(f'Objeto da classe: {self.__class__.__base__}')
		print(f'Objeto da classe: {self.__class__.__bases__}')
		for item in temp:
			c = 25 - len(item)
			print("%s%s : %s" % (item.capitalize(), '.' * c, temp[item]))

	def FichaDicionario(self):
		print('-----------------')
		print('Objeto da classe: Pessoa')
		print(f'Objeto da classe: {self.__class__.__name__}')
		for k, v in self.__dict__.items():
			c = 25 - len(k)
			print("%s%s : %s" % (k.capitalize(), '.' * c, v))


pessoa = Pessoa('Nome', '', 'Telefone') # permite telefone ''
pessoa.Ficha()
