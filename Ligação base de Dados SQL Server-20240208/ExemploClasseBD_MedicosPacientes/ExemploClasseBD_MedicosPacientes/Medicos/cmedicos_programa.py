from cmedicos import *

i = CMedicos()
print(i.CriaTabela())

i.ImportFromCSV('medicos.csv')
