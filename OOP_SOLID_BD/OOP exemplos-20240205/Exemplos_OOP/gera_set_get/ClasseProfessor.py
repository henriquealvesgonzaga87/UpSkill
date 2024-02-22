# from ClasseProfessor import *
# Criar objecto com base em dicionário
# professor = Professor(r['Nome'], r['Email'], r['Telefone'], r['Escola'], r['Departamento'])
# Criar objecto usando construtor
# professor = Professor('Nome', 'Email', 'Telefone', 'Escola', 'Departamento')
class Professor:
	# sets
	def setNome(self, nome):
		if nome != '':
			self.nome = nome
			return True
		else:
			return False

	def setEmail(self, email):
		if email != '':
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

	def setEscola(self, escola):
		if escola != '':
			self.escola = escola
			return True
		else:
			return False

	def setDepartamento(self, departamento):
		if departamento != '':
			self.departamento = departamento
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
	def getEscola(self):
		return self.escola
	def getDepartamento(self):
		return self.departamento

	# construtor
	def __init__(self, nome, email, telefone, escola, departamento):
		self.nome = nome
		self.email = email
		self.telefone = telefone
		self.escola = escola
		self.departamento = departamento

	def __str__(self):
		return str(self.__dict__)

	def Ficha(self):
		temp = vars(self)
		print('-----------------')
		print('Objeto da classe: Professor')
		print(f'Objeto da classe: {self.__class__.__name__}')
		print(f'Objeto da classe: {self.__class__.__base__}')
		print(f'Objeto da classe: {self.__class__.__bases__}')
		for item in temp:
			c = 25 - len(item)
			print("%s%s : %s" % (item.capitalize(), '.' * c, temp[item]))

	def FichaDicionario(self):
		print('-----------------')
		print('Objeto da classe: Professor')
		print(f'Objeto da classe: {self.__class__.__name__}')
		for k, v in self.__dict__.items():
			c = 25 - len(k)
			print("%s%s : %s" % (k.capitalize(), '.' * c, v))

# professor = Professor('Nome', 'Email', 'Telefone', 'Escola', 'Departamento')
# professor.Ficha()
