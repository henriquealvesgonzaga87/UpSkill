import pymysql

mydb = pymysql.connect(
    host="localhost",
    port=3307,
    user="root",
    password="root",
    database="BaseDadosLabAguas"
)


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM tipocliente")
myresult = mycursor.fetchall()

# data
print('Registos:', mycursor.rowcount)
for x in myresult:
    print(x)


# Registos: 12
# (1, 'Empresa')
# (2, 'Particular')
# (3, 'Municipios')
# (4, 'Juntas de Freguesia')
# (5, 'Restauração')
# (6, 'Saúde')
# (7, 'Alojamentos')
# (8, 'Colectividades')
# (9, 'Serviços')
# (10, 'Comércio')
# (11, 'Ensino')
# (12, 'Indústria')


mycursor.execute('describe tipocliente')
data = mycursor.fetchall()
for d in data:
    print(d[0], d[1], d[2])
# IDTipoCliente int NO
# Nome varchar(50) NO


# insert
sql = "insert into tipocliente (IDTipoCliente,TipoCliente)values(%s, %s)"
val = (50, 'Admin')
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
# 1 record inserted.

# data
mycursor.execute("SELECT * FROM tipocliente")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
# (1, 'Empresa')
# (2, 'Particular')
# (3, 'Municipios')
# (4, 'Juntas de Freguesia')
# (5, 'Restauração')
# (6, 'Saúde')
# (7, 'Alojamentos')
# (8, 'Colectividades')
# (9, 'Serviços')
# (10, 'Comércio')
# (11, 'Ensino')
# (12, 'Indústria')
# (50, 'Admin')
