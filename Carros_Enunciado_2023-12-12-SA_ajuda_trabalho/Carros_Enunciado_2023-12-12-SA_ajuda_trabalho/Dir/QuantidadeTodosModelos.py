lista = [('Toyota', 270), ('Seat', 817), ('Renault', 786), ('Porche', 574), ('Peugeot', 542), ('Opel', 538)]
for i, v in enumerate(lista):
	if v[0] == 'Toyota':
		lista[i] = list([v, 'modelo'])
print(lista)