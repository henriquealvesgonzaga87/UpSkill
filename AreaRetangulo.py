# entrada de dados (input)
c = 0
while c <= 0 or c > 99.99:
    c = float(input("Comprimento do retângulo (m): "))

l = 0
while l <= 0 or l >= c:
    l = float(input("Largura do retângulo (m): "))

# processamento

area = l * c

print(f"Á área do retângulo é {area:.2f} m2")
