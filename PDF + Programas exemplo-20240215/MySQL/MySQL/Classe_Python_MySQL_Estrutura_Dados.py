import pymysql


class Classe_Python_MySQL_Estrutura_Dados:
    def __init__(self, servidor='localhost', porta=3307, utilizador='root', password='root', base_dados='basedadoslabaguas'):
        self.mydb = pymysql.connect(
            host=servidor,
            port=porta,
            user=utilizador,
            password=password,
            database=base_dados
        )
        self.bd_nome = base_dados
    def ListDataTable(self, table, where=''):
        cur = self.mydb.cursor()
        cur.execute("SELECT * FROM " + table + " %s" % where)
        rows = cur.fetchall()
        titulos = [x[0] for x in cur.description]
        print(titulos)
        for row in rows:
            print(row)

    def ListDataSQL(self, sql):
        print('Consulta ' + '-' * 20 + sql)
        cur = self.mydb.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        titulos = [x[0] for x in cur.description]
        print(titulos)
        for row in rows:
            print(row)

    def getScalarData(self, sql):
        cur = self.mydb.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        campo = rows[0][0]
        return campo

    def TableStrucure(self, table):
        print('Tabela ' + '-' * 20 + table)
        cur = self.mydb.cursor()
        cur.execute('desc ' + table + ';')
        data = cur.fetchall()
        titulos = [x[0] for x in cur.description]
        print(titulos)
        for d in data:
            #print(d[0], d[1], d[2])
            print(d)

    def ListTables(self):
        print("List of tables " + '-' * 20)
        cur2 = self.mydb.cursor()
        res = cur2.execute(
            f"SELECT table_name FROM INFORMATION_SCHEMA.TABLES  WHERE TABLE_SCHEMA = '{self.bd_nome}' and TABLE_TYPE = 'BASE TABLE';")
        data = cur2.fetchall()
        for name in data:
            print("Table ", name)

    def ListTablesAndStructure(self):
        print("List of tables " + '-' * 20)
        cur2 = self.mydb.cursor()
        res = cur2.execute(
            f"SELECT table_name FROM INFORMATION_SCHEMA.TABLES  WHERE TABLE_SCHEMA = '{self.bd_nome}' and TABLE_TYPE = 'BASE TABLE';")
        data = cur2.fetchall()
        for name in data:
            print("Table ", name)
            self.TableStrucure(name[0])

    def ListTablesData(self):
        print("List of tables " + '-' * 20)
        cur2 = self.mydb.cursor()
        res = cur2.execute(
            f"SELECT table_name FROM INFORMATION_SCHEMA.TABLES  WHERE TABLE_SCHEMA = '{self.bd_nome}' and TABLE_TYPE = 'BASE TABLE';")
        data = cur2.fetchall()
        for name in data:
            print("TABLE " + '-' * 20, name)
            self.ListDataTable(name[0], "where 1=1")

# bd = Classe_Python_MySQL_Estrutura_Dados()
# bd.ListTablesAndStructure()
