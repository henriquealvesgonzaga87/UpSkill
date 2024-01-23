from LerFicheiroCSV import *


cab, lista = LerFicheiroCSV("emdata_0CB815FC6454_1702200182-1702203782.csv", delimitador=',')
print(cab)
for m in lista:
    print(m)

