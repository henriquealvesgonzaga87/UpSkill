# from ClassePessoa import *
# Criar objecto com base em dicionário
# pessoa = Pessoa(r['Nome'], r['Email'], r['Telefone'])
# Criar objecto usando construtor
# pessoa = Pessoa('Nome', 'Email', 'Telefone')

class Label:
    def __init__(self, text, font):
        self._text = text
        self._font = font

    def get_text(self):
        return self._text

    def set_text(self, value):
        self._text = value

    def get_font(self):
        return self._font

    def set_font(self, value):
        self._font = value
    def __str__(self):
        return str(self.__dict__)

l = Label('t','10')
print(l)
l._font = 50
print(l._font)


from datetime import date

class Employee:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value != '':
            self._name = value.upper()

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value# date.fromisoformat(value)

john = Employee(".", "2001-02-07")

print(john.name)
print(john.birth_date)

john.name = ""
print(john.name)



class Pessoa:
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

# pessoa = Pessoa('Nome', 'Email', 'Telefone')
# pessoa.Ficha()
