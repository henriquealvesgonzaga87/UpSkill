# class <nome>:
#    <attr> = <value>
#
#    def method(self, ...):
#        # method's code


class Pessoa:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def get_first_nome(self):
        return self.nome.split()[0]

    def get_last_nome(self):
        return self.nome.split()[-1]

    def update_salario(self, new_salario):
        self.salario = new_salario

    def compute_salario_after_tax(self, irs=0.18, ss=0.12):
        return self.salario - (self.salario * irs) - (self.salario * ss)

person1 = Pessoa("João Cardoso Martins", 35, 1500)
person2 = Pessoa("Ana Costa Silva", 27, 2000)

print(person1.get_last_nome(), person1.compute_salario_after_tax())
print(person2.get_last_nome(), person2.compute_salario_after_tax())

print(person1.__dict__)
print(person1.__class__)

# Martins 1050.0
# Silva 1400.0
# {'nome': 'João CArdoso Martins', 'idade': 35, 'salario': 1500}
# <class '__main__.Pessoa'>
