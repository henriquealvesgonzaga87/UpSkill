number_string = 340020.8
# This portion is responsible for grouping the number
number_commas_only = "{:,}".format(number_string)
print(number_commas_only)

# To ensure we have two decimal places
number_two_decimal = "{:.2f}".format(number_string)
print(number_two_decimal)

# Both combined along with the currency symbol(in this case $)
currency_string = "{:,.2f}€".format(number_string)
print(currency_string)

# 340,020.8
# 340020.80
# 340,020.80€

# The string class contains further methods, which can be used for formatting purposes as well:
# ljust, rjust, center and zfill.
print('\nS.center(width[, fillchar]) -> str')
x = '12345678901234567890'
s = "Python"
print(x)
print(s.center(10),  '.', sep='')
#12345678901234567890
#  Python

y = s.center(10, "*")
print (y)
# **Python**

print('\nS.ljust(width[, fillchar]) -> str')
s = "UPSkills"
y = s.ljust(15)
print(x)
print(y, '.', sep='')

y = s.ljust(15, '_')
print(x)
print(y, '.', sep='')

print('\nS.rjust(width[, fillchar]) -> str')
y = s.rjust(15)
print(x)
print(y, '.', sep='')

y = s.rjust(15, '_')
print(x)
print(y, '.', sep='')

print('\nS.zfill(width) -> str')
s = "4567"
y = s.zfill(15)
print(x)
print(y, '.', sep='')

# Replicar texto:
pontos = '.' * 10
print(x)
print(pontos)

#12345678901234567890
#..........

print(x)
print(f"{'':.<10}")
#12345678901234567890
#..........

p = 10
car = '_'
print(f"{'':{car}<{p}}")
#12345678901234567890
#..........

# dicas para trabalho
tirs = 12.25
virs = 123.45
sb = 1350.25
ss = round(sb * 0.11, 2)
largura = 25
tamanho = 10
print(3 * x)
print(f"Salário bruto".ljust(largura, '.') + ":", f"{sb:{tamanho},.2f}€")
print(f"IRS ({tirs:.2f}%)".ljust(largura, '.') + ":", f"{virs:{tamanho},.2f}€")
print(f"SS (11%)".ljust(largura, '.') + ":", f"{ss:{tamanho},.2f}€")
# Salário bruto............:   1,350.25€
# IRS (12.25%).............:     123.45€
# SS (11%).................:     148.53€

largura = 20
tamanho = 8
print(3 * x)
print(f"Salário bruto".ljust(largura, '.') + ":", f"{sb:{tamanho},.2f}€")
print(f"IRS ({tirs:.2f}%)".ljust(largura, '.') + ":", f"{virs:{tamanho},.2f}€")
print(f"SS (11%)".ljust(largura, '.') + ":", f"{ss:{tamanho},.2f}€")

# 123456789012345678901234567890123456789012345678901234567890
# Salário bruto.......: 1,350.25€
# IRS (12.25%)........:   123.45€
# SS (11%)............:   148.53€
