#Leitura de ficheiro de texto sem conjsidrar a sua estrutura/formato

f = open('hipermercado.txt', 'rt', encoding='utf-8')
linhas = f.readlines()  # lista em que cada elemento contém uma linha do ficheiro
f.close()
print(linhas)
for p in linhas:
    print(p)

# Cada linha do ficheiro é um elemento to tipo string da lista. A string inclui o caractere de controlo de fim de linha \code{\\n}
# ['1;Ketchup;Mercearia Salgado;1.59;23%\n', '2;Atum;Mercearia Salgado;3.38;6%\n', '3;Cogumelos;Mercearia Salgado;1.98;23%\n', '4;Bolachas Cacau;Mercearia Doce;1.39;23%\n', '5;Cerelac;Mercearia Doce;5.65;6%\n', '6;Heineken 12*25CL;Bebidas;8.99;23%\n', '7;Gel Dove;Higiene e Beleza;5.99;23%\n', '8;Lenços de Bolso;Limpeza do Lar;1.59;23%\n', '9;Jardineira;Congelados;1.99;6%\n', '10;Leite 6x1L;Lacticinios;4.92;6%\n', '11;Natas;Lacticinios;0.79;6%\n', '12;Ovos;Lacticinios;0.94;6%\n', '13;Espadarte Posta;Peixaria;6.49;6%\n', '14;Queijo Limiano;Charcutaria;3.89;6%\n', '15;Laranjas;Frutas e Legumes;1.449;6%\n', '16;Ameixa Seca;Frutas e Legumes;2.00;6%\n', '17;Tabuleiro;Casa;7.00;23%\n', '18;Pensar Python;Cultura;17.0;6%\n', '19;Limpa Vidros;Bricolage;3.69;23%\n', '20;Oregaos;Mercearia Salgado;1.42;6%\n', '21;Bolachas Belvita;Mercearia Doce;2.39;23%\n', '22;Pedras Salgadas;Bebidas;2.46;13%\n', '23;Skip 40D;Limpeza do Lar;12.99;23%\n', '24;Pão Aveia;Padaria;1.99;6%\n', '25;Iogurte Grego;Lacticinios;2.59;6%']
# 1;Ketchup;Mercearia Salgado;1.59;23%
#
# 2;Atum;Mercearia Salgado;3.38;6%
#
# 3;Cogumelos;Mercearia Salgado;1.98;23%
#
# 4;Bolachas Cacau;Mercearia Doce;1.39;23%
#
# 5;Cerelac;Mercearia Doce;5.65;6%
#
# 6;Heineken 12*25CL;Bebidas;8.99;23%
# ...

#Cada linha do ficheiro é uma string.


import csv
lista = []
with open('hipermercado.txt', 'rt', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    for r in reader:
        lista.append(r)
for p in lista:
    print(p)
#
# ['1', 'Ketchup', 'Mercearia Salgado', '1.59', '23%']
# ['2', 'Atum', 'Mercearia Salgado', '3.38', '6%']
# ['3', 'Cogumelos', 'Mercearia Salgado', '1.98', '23%']
# ['4', 'Bolachas Cacau', 'Mercearia Doce', '1.39', '23%']
# ['5', 'Cerelac', 'Mercearia Doce', '5.65', '6%']
# ['6', 'Heineken 12*25CL', 'Bebidas', '8.99', '23%']
# ['7', 'Gel Dove', 'Higiene e Beleza', '5.99', '23%']
# ...








