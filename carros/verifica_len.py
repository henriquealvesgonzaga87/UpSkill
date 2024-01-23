def verifica_len(txt):
	texto = str(input(txt)).upper()
	while len(texto) != 2:
		print("O valor de caracteres deve ser 2")
		texto = str(input(txt))
