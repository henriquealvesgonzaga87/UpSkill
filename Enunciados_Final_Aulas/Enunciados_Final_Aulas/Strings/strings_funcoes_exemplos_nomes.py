str = '-'.join('hello')
print(str)
list1 = ['U', 'P', 's', 'k', 'i', 'l', 'l']
print('i)', ''.join(list1))

nome = 'Miguel Paulo de Assunção Silva'
nome_lista = nome.split(' ')
nome_de_lista = ' '.join(nome_lista)
print('ii) Juntar elementos de um vetor:', nome_de_lista)
print('\t', nome)
print('\t', nome_lista)




v = [[1, 'Lígia Isabel Mendes Belo'], [2, 'Sandra Alexandra Gomes Araújo'], [3, 'Inês Marisa Fonseca Couto'],
     [4, 'Bruno Saraiva de Castro'], [5, 'Guilherme Miguel Pontes de Melo'], [6, 'Henrique Nogueira Pereira'],
     [7, 'João José Alves Gonzaga'], [8, 'João Filipe da Silva Matos'], [9, 'Miguel Paulo de Assunção Silva'],
     [10, 'João Ângelo Dias Augusto'], [11, 'Julien Pedro Gonçalves Rodrigues'],
     [12, 'Patrick Alexandre Pereira Batista'], [13, 'Pedro José Tomé Monteiro'], [14, 'Rodrigo Miguel Guerra Paraíso'],
     [15, 'Ana Augusto Soares Ferreira']]
v = v[:]
print(v)

bcode = '\n\\begin{lstlisting}[frame=lines,style=python,numbers=none,caption={Código Python.}, label={}]'
b = '\n\\begin{lstlisting}[frame=lines,style=python,numbers=none,caption={Resultado}, label={}]'
e = '\\end{lstlisting}\n\n'

print(bcode)
print(e)
print(b)
# Imprimindo uma string.
s = "Olá, mundo!"
print('1)', s)

# Tipo de uma string.
print('2)', type(s))

# É do tipo de uma string?
print('3)', isinstance(s, str))

# Tamanho de uma string.
print('4)', len(s))
print(e)

print(b)
print(e)
print(b)
# Concatenação
print('5)', "Meu Portugal " + "português")

# Substitui uma substring por alguma outra coisa.
s1 = s.replace("mundo", "meu lar")
print('6)', s1)

# A string s começa com "Olá"?
print('7)', s.startswith("Olá"))

# A string s termina com "mundo"?
print('8)', s.endswith("mundo"))

# Quantas ocorrências da palavra "abacate" a string s1 possui?
print(s1.count("lar"))
print(e)

print('# Substrings em Python (Slicing) ' + ('-' * 20))
t = '''
# Substrings em Python (Slicing)
# Além das operações vistas acima, podemos acessar caracteres específicos de uma string em Python
# usando a notação []. Neste esquema de acesso a caracteres de uma string,o primeiro caracter está no índice 0, o segundo no índice 1, e assim por diante, conforme ilustrado no exemplo abaixo.
'''
print(t)

t = '''O nome completo é composto pelos nomes próprios e pelos apelidos
 O nome pode conter no máximo seis vocábulos simples ou compostos, em regra, até dois nomes próprios e quatro apelidos.'''
print(t)

print(b)
print(e)
print(b)
pos = '0123456789012345678901234567890123456789'
nome = "RODOLFO PINHEIRO QUEIROS ARANTES"

print('0:', nome[0])
print('1:', nome[1])
print('2:', nome[2])
print("Posições.....:", pos)
print("Original.....:", nome)

# Podemos também acessar os elementos em ordem reversa usando índices negativos. Neste esquema, o último caracter de uma string está no índice −1
# , o penúltimo no índice −2, e assim por diante, como mostrado no exemplo abaixo.

print('-1', nome[-1])
print('-2', nome[-2])
print('-3', nome[-3])
print(e)

t = '''Podemos também acessar fatias ou "slices" de uma string ou lista em Python. Esta notação é muito concisa e poderosa, então é importante que você a entenda bem.

 Segundo essa notação, uma fatia de uma string, ou seja, uma substring, pode ser acessada se fornecermos os índices do começo e do final da fatia que desejamos analisar, como mostrado abaixo:
'''
print(t)
print(b)
print(e)
print(b)
print('nome[1:3]', nome[1:3])

t = '''Note que, como mencionamos anteriormente, os índices de uma string começam do 0 e não do 1.

 Além disso, perceba que o índice do final da fatia não é incluído nela. No exemplo acima, o [1:3] nos retornou dois caracteres e não três. Foram retornados o caracter no índice 1 e o caracter no índice 2, mas não o caracter no índice 3.

 Se omitirmos o índice de ínicio da fatia ou o de final (ou ambos), o ínicio e o final da string serão considerados, respectivamente. Veja os exemplos:
'''
print(t)

print(b)
print(e)
print(b)
print('nome[:7]', nome[:7])
#
print('nome[9:]', nome[9:])
#
# # Retorna toda a string
print('nome[:]', nome[:])
# Retorn os caracteres 1 e 2
print('nome[1:3]', nome[1:3])
print(e)

t = '''É possível ainda especificar um parâmetro que indica quantos caracteres devem ser processados de cada vez. Por exemplo, se quisermos imprimir somente os caracteres nos índices pares ou ímpares de uma string, podemos fazer assim:
'''
print(t)

print(b)
print(e)
print(b)
print('nome[::2]', nome[::2])  # Imprime os caracteres nos índices pares
print('nome[1::2]', nome[1::2])  # Imprime os caracteres nos índices ímpares
print(e)

t = '''Um outro exemplo útil do uso da técnica de slicing para manipulação de strings é inverter uma palavra ou frase usando somente operações de slicing:
'''
print(t)
print(b)
print(e)
print(b)
print('nome[::-1]', nome[::-1])
print(e)

t = '''No exemplo acima, usamos um terceiro parâmetro do recurso de slicing para indicar que retornamos toda a frase (os ::) e logo em seguida dizemos que faremos isso de trás para frente (por meio do −1 no final). Mais especificamente, o −1
indica que estamos saltando um caracter de cada vez, começando de trás para frente (o que é feito por meio do sinal de menos).
 Então, para resumir, a sintaxe de slicing de strings é a seguinte [início:fim:salto], onde:

 início é o primeiro índice a ser considerado (o primeiro caracter da string é considerado caso este valor seja omitido);

 fim - 1 é o último índice a ser considerado (o último caracter da string é considerado caso este valor seja omitido); e

 salto indica quantos caracteres devem ser saltados em cada etapa (o valor 1
  é considerado por padrão, e um sinal de menos deve ser usado para percorrer a string em ordem reversa).
'''
print(t)

print(b)
print(e)
print(b)
print('# Nomes-Strings ' + ('-' * 20))
print("Posições.....:", pos)
print(".capitalize():", nome.capitalize())
print(".title().....:", nome.title())
print(".upper().....:", nome.upper())
print(".lower().....:", nome.lower())
import string

print(".capwords()..:", string.capwords(nome))
# print(string.__all__)  # listas todas as funções da classe string
print(e)

t = '''str.split(sep=None, maxsplit=-1)
 Retorna uma lista de palavras na string, usando sep como a string delimitadora. Se maxsplit é fornecido, no máximo maxsplit cortes são feitos (portando, a lista terá no máximo maxsplit+1 elementos). Se maxsplit não foi especificado ou -1 foi informado, então não existe limite no número de cortes (todos os cortes possíveis são realizados).
'''
print(t)

print(b)
print(e)
print(b)
nome_lista = nome.split(' ')
print(nome_lista)
primeironome = nome_lista[0]  # primeiro
ultimonome = nome_lista[-1]  # último, -2 penúltimo
print('primeironome..:', primeironome)  #
print('ultimonome....:', ultimonome)

print("primeiro nome (nome próprio) e restantes nomes: nome.split(' ', 1)")
nome_lista = nome.split(' ', 1)
print('a)', nome_lista)

print("nomes + apelido: nome.rsplit(' ', 1)")
nome_lista = nome.rsplit(' ', 1)
print('b)', nome_lista)

print("Dois nomes próprios + apelidos: nome.split(' ', 2)")
nome_lista = nome.split(' ', 2)
print('c)', nome_lista)
print(e)

t = '''str.startswith(prefix[, start[, end]])
 Retorne True se a String começar com o prefixo, caso contrário, retorna False. prefixo também pode ser uma tupla de prefixos a serem procurados. Com start opcional, a String de teste começa nessa posição. Com fim opcional, interrompe a comparação de String nessa posição.
'''
print(t)
print(b)
print(e)
print(b)
print(pos)
#     0123456789012345678901234567890123456789
s1 = 'RODOLFO PINHEIRO QUEIROS ARANTES'
s2 = 'BRUNO AMADO ARANTES QUEIROS'
print("Pesquisa de texto em strings")
print("Começa por:")

print('1)', s1.startswith('RODOLFO'))
print('2)', s1.startswith('RODOLFO', 9))
print('3)', s1.startswith('PINHEIRO', 9))
print('4)', s2.startswith('ARANTES', 11, 18))
print('5)', s1.startswith(('RODOLFO', 'BRUNO')))
print('6)', s2.startswith(('RODOLFO', 'BRUNO')))
print(e)

print(b)
print(e)
print(b)
print(pos)
#     0123456789012345678901234567890123456789
s1 = 'RODOLFO PINHEIRO QUEIROS ARANTES'
s2 = 'BRUNO AMADO ARANTES QUEIROS'
print("Pesquisa de texto em strings")
print("Termina por:")

print('1)', s1.endswith('ARANTES'))
print('2)', s1.endswith('RODOLFO', 9))
print('3)', s1.endswith('PINHEIRO', 9))
print('4)', s2.endswith('QUEIROS', 11, 18))
print('5)', s1.endswith(('ARANTES', 'QUEIROS')))
print('6)', s2.endswith(('ARANTES', 'QUEIROS')))
print(e)

t = '''\\section{Contém}\n
 str.find(sub[, start[, end]])\n
 Retorna o índice mais baixo na string onde a substring sub é encontrado dentro da fatia s[start:end]. Argumentos opcionais como start e end são interpretados como na notação de fatiamento. Retorna -1 se sub não for localizado.

 Nota O método find() deve ser usado apenas se precisarmos conhecer a posição de sub. Para verificar se sub é ou não uma substring, use o operador in:
 'Py' in 'Python'
 True
'''
print(t)

print(b)
print(e)
print(b)
#    0123456789012345678901234567890123456789
m = 'Pedro José Tomé Monteiro'
print(f"1) {m.find('Tomé')}")
print(f"2) {'Tomé' in m}")
print(f"3) {m.find('Maria')}")
print(f"1) {m.find('Tomé', 15)}")
print(f"1) {m.find('Tomé', 11)}")
print(f"1) {m.find('José', 5, 12)}")
print(e)

print('''\\section{Subtituir texto}''')

print(b)
print(e)
print(b)
h = 'Henrique Nogueira Pereira'
m1 = 'Lígia Isabel Mendes Belo'
m2 = 'Ana Augusto Soares Ferreira'

print('h + m1: adcionar apelido de f a m1 (não esquercer o espaço)')
m1h = m1 + ' ' + h.rsplit(' ', 1)[-1]
print(f'i) .{m1h}.')
print(f'\t.{m1}.')
print(f'\t.{h}.')

print('h + m2: subtituir apelido de f por apelido de m2')
m2h = m2.replace(m2.rsplit(' ', 1)[-1], h.rsplit(' ', 1)[-1])
print(f'ii) .{m2h}.')
print(f'\t.{m2}.')
print(f'\t.{h}.')
print(e)

print('''\\section{Remover no ínicio}''')
t = '''str.removepreffix(suffix, /)
 Se a string terminar com a string suffix e a suffix não estiver vazia, retorna string[:-len(suffix)]. Caso contrário, retorna uma cópia da string original:
'''
print(t)

print(b)
print(e)
print(b)
m = 'João Filipe da Silva Matos'
m1 = m.removeprefix(m.split(' ', 1)[0] + ' ')
print(f'i) .{m1}.')
print(f'\t.{m}.')
print(e)

print('Remover no meio')
t = '''Se a string terminar com a string suffix e a suffix não estiver vazia, retorna string[:-len(suffix)]. Caso contrário, retorna uma cópia da string original:
'''
print(t)

print(b)
print(e)
print(b)
m = 'João Filipe da Silva Matos'
m1 = m.replace(' da', '')
print(f'i) .{m1}.')
print(f'\t.{m}.')
print(e)

print('Remover no fim')
t = '''str.removesuffix(suffix, /)
# Se a string terminar com a string suffix e a suffix não estiver vazia, retorna string[:-len(suffix)]. Caso contrário, retorna uma cópia da string original:
'''
print(t)

print(b)
m = 'Patrick Alexandre Pereira Batista'
m1 = m.removesuffix(' ' + m.rsplit(' ', 1)[-1])
print(f'i) .{m1}.')
print(f'\t.{m}.')
print(e)

print('Pesquisa')

t = '''juntar elementos de strings e vetores
 '<sepadador>'.join(<string | lista>)
 str.join(iterable)
 Retorna a string que é a concatenação das strings no iterável.
 Uma TypeError será levantada se existirem quaisquer
 valores que não sejam strings no iterável, incluindo objetos bytes.
 O separador entre elementos é a string que está fornecendo este método.'''
print(t)

print(b)
print(e)
print(b)
str = '-'.join('hello')
print(str)
list1 = ['U', 'P', 's', 'k', 'i', 'l', 'l']
print('i)', ''.join(list1))

nome = 'Miguel Paulo de Assunção Silva'
nome_lista = nome.split(' ')
nome_de_lista = ' '.join(nome_lista)
print('ii) Juntar elementos de um vetor:', nome_de_lista)
print('\t', nome)
print('\t', nome_lista)
print(t)
