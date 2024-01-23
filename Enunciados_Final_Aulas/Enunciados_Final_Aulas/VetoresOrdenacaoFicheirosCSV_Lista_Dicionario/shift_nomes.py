dados = [
	(1, 'Ana Isabel Mendes Belo'),
	(2, 'Bruno Miguel Pontes de Melo'),
	(3, 'Guilherme Nogueira Pereira'),
	(4, 'Henrique José Alves Gonzaga'),
	(5, 'Inês Saraiva de Castro'),
	(6, 'João Filipe da Silva Matos'),
	(10, 'Lígia Alexandra Gomes Araújo'),
	(7, 'João Paulo de Assunção Silva'),
	(11, 'Miguel Ângelo Dias Augusto'),
	(8, 'João Pedro Gonçalves Rodrigues'),
	(9, 'Julien Alexandre Pereira Batista'),
	(12, 'Patrick José Tomé Monteiro'),
	(13, 'Pedro Miguel Guerra Paraíso'),
	(14, 'Rodrigo Augusto Soares Ferreira'),
	(15, 'Sandra Marisa Fonseca Couto')
]
# generate random floating point values
from random import seed
import random

# # seed random number generator
# seed(1)
# # generate random numbers between 0-1
# for _ in range(10):
# 	value = random()
# 	print(value)
seed(13)
n = len(dados)
print("{:8s}".format("Número"), end='')
print("{:40s}".format("Nome"), end='')
print("{:>15s}".format("Venc.Base"), end='')
print("{:>15s}".format("N.Vendas"))

f = open("Vencimentos_Maio2022.txt", "wt", encoding='utf-8')
print("{:8s}".format("Número"), end='', file=f)
print("{:40s}".format("Nome"), end='', file=f)
print("{:>15s}".format("Venc.Base"), end='', file=f)
print("{:>13s}".format("N.Vendas"), end='', file=f)
print("{:>13s}".format("Comissão"), end='', file=f)
print("{:>13s}".format("V.Ilíquido"), end='', file=f)
print("{:>13s}".format("Desc.SS"), end='', file=f)
print("{:>13s}".format("Desc.IRS"), end='', file=f)
print("{:>13s}".format("T.Descontos"), end='', file=f)
print("{:>13s}".format("Receber"), file=f)

f2 = open("Dados_Vencimentos_Maio2022.txt", "wt", encoding='utf-8')
print("Número", "Nome", "Venc.Base", "N.Vendas", sep=';', file=f2)
TaxaIRS = 5
SS = 21
tComissao = 0
tQt = 0
tVIRS = 0
tVSS = 0
tTotalDescontos = 0
tliquido = 0
tvIliquido = 0
nomes = []
for i in range(n):
	r1 = dados[i % n]
	r2 = dados[(i + 1) % n]
	nomes1 = r1[1].split(' ')
	nomes2 = r2[1].split(' ')
	nome = nomes2[0:1] + nomes1[1:]  # lista
	nome = ' '.join(nome)  # string
	vb = random.randint(74000, 250000) / 100.0
	qt = random.randint(2, 50)
	# print(i+1, ' '.join(nome), vb, qt)
	print("{:>4d}{:}".format(i + 1, ' ' * 4), end='')
	print("{:40s}".format(nome), end='')
	print("{:15.2f}".format(vb), end='')
	print("{:13d}".format(qt))

	print(i + 1, nome, vb, qt, sep=';', file=f2)

	nomes.append([i+1, nome])

	print("{:>4d}{:}".format(i + 1, ' ' * 4), end='', file=f)
	print("{:40s}".format(nome), end='', file=f)
	print("{:15.2f}".format(vb), end='', file=f)
	print("{:13d}".format(qt), end='', file=f)
	VSS = vb * SS / 100.0
	if (qt <= 5):
		comissao = 10
	if (qt <= 10):
		comissao = 12
	if (qt <= 15):
		comissao = 14
	else:
		comissao = 15
	comissao = qt * comissao
	vIliquido = vb + comissao
	VIRS = round(vIliquido * TaxaIRS / 100, 2)
	VSS = round(vb * SS / 100.0)
	totalDescontos = VIRS + VSS
	liquido = vIliquido - totalDescontos

	tQt = tQt + qt
	tComissao = tComissao + comissao
	tVIRS = tVIRS + VIRS
	tVSS = tVSS + VSS
	tTotalDescontos = tTotalDescontos + totalDescontos
	tliquido = tliquido + liquido
	tvIliquido = tvIliquido + vIliquido

	print("{:13.2f}".format(comissao), end='', file=f)
	print("{:13.2f}".format(vIliquido), end='', file=f)
	print("{:13.2f}".format(VSS), end='', file=f)
	print("{:13.2f}".format(VIRS), end='', file=f)
	print("{:13.2f}".format(totalDescontos), end='', file=f)
	print("{:13.2f}".format(liquido), file=f)

print("{:63s}".format(''), end='', file=f)
print("{:13d}".format(tQt), end='', file=f)
print("{:13.2f}".format(tComissao), end='', file=f)
print("{:13.2f}".format(tvIliquido), end='', file=f)
print("{:13.2f}".format(tVSS), end='', file=f)
print("{:13.2f}".format(tVIRS), end='', file=f)
print("{:13.2f}".format(tTotalDescontos), end='', file=f)
print("{:13.2f}".format(tliquido), file=f)
f.close()

print(dados)
print(nomes)

# Quantidade Comissão (€)
#     0-5      10.00
#     6-10     12.00
#     11-15    14.00
#     15+      15.00

# https://www.programiz.com/python-programming/methods/string/join
# Python String join()
# In this tutorial, we will learn about the Python String join() method with the help of examples.
#
# The join() string method returns a string by joining all the elements of an iterable (list, string, tuple), separated by a string separator.
#
# Example
# text = ['Python', 'is', 'a', 'fun', 'programming', 'language']
#
# # join elements of text with space
# print(' '.join(text))
#
# # Output: Python is a fun programming language
# Run Code
# Syntax of String join()
# The syntax of the join() method is:
#
# string.join(iterable)


