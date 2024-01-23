fic_txt = 'dados.txt'
fic_bin = 'dados.bin'

f = open(fic_txt, 'wt', encoding='ascii')
for x in range(0, 1023+1):
    print(x, file=f)
f.close()

f = open(fic_bin, 'wb')
for x in range(0, 1023+1):
    f.write(x.to_bytes(2))
    # file.write((i).to_bytes(24, byteorder='big', signed=False))
f.close()

import os
from datetime import datetime

print(os.path.getsize(fic_txt))
print(os.path.getmtime(fic_txt))
print(os.path.getctime(fic_txt))

# os.path.getsize() returns the size of the file
# os.path.getmtime() returns the file last modified date
# os.path.getctime() returns the file creation date (equals to last modified date in Unix systems like macOS)

def PropriedadesFicehrio(fic):
    print(fic)
    # timestamp is number of seconds since 1970-01-01
    # 1702312270.2769284
    # convert the timestamp to a datetime object in the local timezone
    data_criacao = datetime.fromtimestamp(os.path.getmtime(fic))
    # print the datetime object and its type
    print("Data criação =", data_criacao)
    print("Tipo =", type(data_criacao))
    data_alteracao = datetime.fromtimestamp(os.path.getmtime(fic))
    print("Data alteração = ", data_alteracao)

PropriedadesFicehrio(fic_txt)
PropriedadesFicehrio(fic_bin)

# Open the binary file
file = open(fic_bin, "rb")
# Reading the first three bytes from the binary file
bytes = file.read(2)
# Printing data by iterating with while loop
while bytes:
    inteiro = int.from_bytes(bytes)
    print(inteiro)
    bytes = file.read(2)
# Close the binary file
file.close()

#os.system(fic_txt)

