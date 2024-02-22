import pyodbc

class CRUDMaisProdutosSQLServer:
    def __init__(self, server='VOD16', database='UpSkillsEmentas'):
        # server= 'VOD2\QTS'# Gab20
        self.table_names = []
        self.database='UpSkillsEmentas'
        driver = "ODBC Driver 17 for SQL Server"
        self.cnxn = pyodbc.connect(f'Driver={driver};' f'Server={server};'
                      f'Database={database};'
                      'Trusted_Connection=yes;')
        self.cursor = self.cnxn.cursor()

    def CopiaBaseDados(self):
        # Prepare the stored procedure execution script and parameter values
        # Execute Stored Procedure With Parameters
        self.cnxn.commit()
        self.cursor.execute("Exec [dbo].[P_BackUpDataBase]")

    # CRUD
    def CriaTabela(self):
        c = self.cursor.execute('''
          CREATE TABLE products (
			product_id int primary key,
			product_name nvarchar(50),
			price decimal(10, 3),
			date datetime default CURRENT_TIMESTAMP,
			foto IMAGE null,
			nome_foto nvarchar(100) null,
			ficheiroBio IMAGE null,
			nome_ficheiroBio nvarchar(100) null,
			)''')
        self.cnxn.commit()
        return c.rowcount

    def ConverteRegistoParaDicionario(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def ToString(self):
        return self.__dict__.copy()

    def getDadosTabelaLista(self, table_name):
        tsql = "SELECT * FROM %s" % table_name
        self.table_data = []
        with self.cursor.execute(tsql):
            for row in self.cursor:
                self.table_data.append(self.ConverteRegistoParaDicionario(self.cursor, row))
        return self.table_data

    def getNomesTabelas(self):
        tsql = f"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG='{self.database}' order by TABLE_NAME"
        self.table_names = []
        with self.cursor.execute(tsql):
            for row in self.cursor:
                if row[0] != 'sysdiagrams':
                    self.table_names.append(row[0])
        return self.table_names

    def getCamposTabela(self, table_name):
        tsql = "SELECT * FROM %s " % table_name
        self.table_data = []
        with self.cursor.execute(tsql):
            return [description[0] for description in self.cursor.description]

    def getEstruturaTabela0(self, table_name):
        tsql = "SELECT * FROM %s " % table_name
        self.table_data = []
        with self.cursor.execute(tsql):
            return self.cursor.description

    # https://docs.microsoft.com/en-us/sql/machine-learning/python/python-libraries-and-data-types?view=sql-server-ver16
    # Python and SQL Data Types
    def getEstruturaTabela(self, table_name):
        tsql = "SELECT * FROM %s " % table_name
        self.table_data = []
        for i in range(len(self.cursor.description)):
          print("Column {}:".format(i+1))
          desc = self.cursor.description[i]
          print("  column_name = {}".format(desc[0]))
          print("  type = {} ({})".format(desc[1], 'FieldType.get_info(desc[1])'))
          print("  null_ok = {}".format(desc[6]))
          # print("  column_flags = {}".format(desc[7]))
        return self.cursor.description

    def ExecutaComandoSQL(self, tsql):
        try:
            self.cursor.execute(tsql)
            self.cnxn.commit()
            return self.cursor.description
        except Exception as error:
            print(error)

    def Versao(self):
        #Sample select query
        self.cursor.execute("SELECT @@version;")
        row = self.cursor.fetchone()
        while row:
            print(row[0])
            row = self.cursor.fetchone()

    def InserirDefault(self):
        c = self.cursor.execute('''
            INSERT INTO products (product_id, product_name, price)
            VALUES
                (1,'Desktop Computer',800),
                (2,'Laptop',1200),
                (3,'Tablet',200),
                (4,'Monitor',350),
                (5,'Printer',150)
                ''')
        self.cnxn.commit()
        return c.rowcount

    def Inserir(self, product_id, product_name, price):
        #Sample insert query
        count = self.cursor.execute('''
            INSERT INTO products (product_id, product_name, price) 
                VALUES (?,?,?)''', product_id, product_name, price).rowcount
        self.cnxn.commit()
        return count

    def Eliminar(self, product_id):
        #Sample insert query
        count = self.cursor.execute('DELETE FROM products WHERE product_id=?', product_id).rowcount
        self.cnxn.commit()
        return count

    def AtualizaPreco(self, id, preco):
        #Sample insert query
        count = self.cursor.execute('UPDATE products SET price=? WHERE product_id=?', preco, id).rowcount
        self.cnxn.commit()
        return count

    def AtualizaNome(self, id, nome):
        #Sample insert query
        count = self.cursor.execute('UPDATE products SET product_name=? WHERE product_id=?', nome, id).rowcount
        self.cnxn.commit()
        return count

    def ListarDadosFormatoTabular(self):
        registos = self.getDadosTabelaLista('products')
        import datetime
        print('{0:<12s}'.format('product_id'), end='')
        print('{0:<20s}'.format('product_name'), end='')
        print('{0:>10s}'.format('price'), end='')
        print('{0:^22s}'.format('date'))
        for r in registos:
            # print(r)
            print('{0:^12d}'.format(r['product_id']), end='')
            print('{0:<20s}'.format(r['product_name']), end='')
            print('{0:10.2f}'.format(r['price']), end='')
            print('{0:>22s}'.format(datetime.datetime.strftime(r['date'],'%Y-%M-%d %H:%m:%S')))

    # BLOB
    # https://pynative.com/python-mysql-blob-insert-retrieve-file-image-as-a-blob-in-mysql/

    def convertToBinaryData(self, filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:   # rb - binário
            binaryData = file.read()
        return binaryData

    def Inserir_Foto_Biografia(self, id, photo_name, biodataFile_name):
        import os
        try:
            sql = 'UPDATE products SET foto=?, nome_foto=?, ficheiroBio=?, nome_ficheiroBio=? WHERE product_id=?'
            foto = self.convertToBinaryData(photo_name)
            ficheiroBio = self.convertToBinaryData(biodataFile_name)

            nome_foto = os.path.basename(photo_name)
            nome_ficheiroBio = os.path.basename(biodataFile_name)

            result = self.cursor.execute(sql, (foto, nome_foto, ficheiroBio, nome_ficheiroBio, id))
            self.cnxn.commit()
            print('Foto e bio-data inserida na BD:')
            return result

        except Exception as error:
            print('Falha a inserir foto e bio-data:', error)

    def write_file(self, data, filename):
        # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:  # wb - binário
            file.write(data)

    def Ler_Foto_Biografia_GravaFicheiro(self, id, nome_ficheiro_foto=None, nomeFicheiroBio=None):
        try:
            sql_fetch_blob_query = 'SELECT foto, nome_foto, ficheiroBio, nome_ficheiroBio from products where product_id=?'
            self.cursor.execute(sql_fetch_blob_query, (id))
            record = self.cursor.fetchall()
            for row in record:
                image = row[0]
                nome_foto = row[1]
                file = row[2]
                nome_biografia = row[3]
                print("Ler foto e bio-data da BD\n")

                if nome_ficheiro_foto is None:
                    self.write_file(image, nome_foto)
                else:
                    self.write_file(image, nome_ficheiro_foto + '.' + nome_foto.split('.')[-1])

                if nomeFicheiroBio is None:
                    self.write_file(file, nome_biografia )
                else:
                    self.write_file(file, nomeFicheiroBio + '.' + nome_biografia.split('.')[-1])

        except Exception as error:
            print("Falha lendo foto e bio-data da BD".format(error))

        return image, nome_foto, file, nome_biografia


    def VerFoto(self, fotoEmBinario):
        import matplotlib.pyplot as plt
        import matplotlib.image as mpimg
        import io

        fp = io.BytesIO(fotoEmBinario)
        img = mpimg.imread(fp) #, format='jpeg'
        plt.imshow(img)
        plt.show()

    def VerBiografia(self, nome_ficheiro):
        import os
        os.system(nome_ficheiro)

    # conn.rollback()
