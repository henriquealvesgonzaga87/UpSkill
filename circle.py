import math as m

number = float(input("Informe o raio do circulo: "))
while number <= 0:
    number = float(input("Informe o raio do circulo: "))

area = m.pi * number ** 2
diametro = number * 2
circunferencia = 2 * m.pi * number

print(f"A area é: {area:.2f}")
print(f"O diametro é: {diametro:.2f}")
print(f"A circunferência é: {circunferencia:.2f}")
