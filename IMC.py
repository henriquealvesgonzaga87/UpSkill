# calcular índice de massa corporal (IMC)
# saiba se tem o peso ideal
# IMC = p/a**2

altura = float(input("digite a sua altura (m): "))
while altura <= 0:
    altura = float(input("digite a sua altura (m): "))

peso = float(input("Digite o seu peso (Kg): "))
while peso <= 0:
    peso = float(input("Digite o seu peso (Kg): "))

IMC = peso / altura ** 2

print(f"IMC: {IMC:.2f}")
