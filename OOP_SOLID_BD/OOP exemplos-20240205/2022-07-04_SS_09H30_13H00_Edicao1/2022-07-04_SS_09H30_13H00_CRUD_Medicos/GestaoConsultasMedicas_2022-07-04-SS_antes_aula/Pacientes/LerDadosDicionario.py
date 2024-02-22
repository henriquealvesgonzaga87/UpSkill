def LerDadosDicionario(nome_ficheiro):
	import csv, os
	dicionario = []
	f = open(nome_ficheiro, 'r', newline='', encoding='utf-8')
	reader = csv.DictReader(f, delimiter=';')
	fieldnames = reader.fieldnames
	print(fieldnames)
	for row in reader:
		print(row["Número"], row["Nome"])
	f.close()
