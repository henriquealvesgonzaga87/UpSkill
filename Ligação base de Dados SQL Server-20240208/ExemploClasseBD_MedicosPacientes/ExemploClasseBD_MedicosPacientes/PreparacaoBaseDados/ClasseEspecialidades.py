import pyodbc

class EspecialidadesCRUDSQLServer:
    def __init__(self, server, database):
        self.table_names = []
        self.database = database
        driver = "ODBC Driver 17 for SQL Server"
        self.cnxn = pyodbc.connect(f'Driver={driver};' f'Server={server};'
                                   f'Database={database};'
                                   'Trusted_Connection=yes;')  # string conexão com banco de dados
        self.cursor = self.cnxn.cursor()

    def LerCSVParaListadeDicionarios(self, nome_ficheiro, delimitador=';'):
        import csv
        with open(nome_ficheiro, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=delimitador)
            dados = [r for r in reader]  # load all records - list of dicts
            return dados
        return []
    # Import a CSV File to SQL Server using Python
    def ImportFromCSV(self, nome_ficheiro):
        medicos = self.LerCSVParaListadeDicionarios(nome_ficheiro)
        # {'Nome': 'Abel António Rocha Branco', 'Especialidade': 'Medicina Interna', 'Instituição': 'Hospital Distrital de Santarém, E.P.E.', 'Cédula Número': '63531', 'Número Ordem': '1900', 'Data Nascimento': '1958-03-04'}
        for m in medicos:
            self.Inserir(m['Especialidade'])

    def CriaTabela(self):
        # erros: https://www.educative.io/answers/what-are-the-exceptions-while-connecting-to-sql-server-in-python
        try:
            c = self.cursor.execute('''
              CREATE TABLE Especialidade (
                IDEspecialidade int primary key identity(1,1),
                Especialidade nvarchar(100) not null unique
                )''')
            self.cnxn.commit()
        except Exception as error:
            return (False, error)
        return True

    def ApagaTabela(self):
        try:
            c = self.cursor.execute('''
                IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Especialidade]') AND 
                type in (N'U')) DROP TABLE [dbo].[Especialidade]
              ''')
            self.cnxn.commit()
        except Exception as error:
            return False
        return True

    def Inserir(self, especialidade):
        # Sample insert query
        try:
            count = self.cursor.execute('''
            INSERT INTO Especialidade (especialidade) VALUES (?)''', especialidade).rowcount
            self.cnxn.commit()
        except Exception as error:
            return False
        return True

    def Eliminar(self, IDEspecialidade):
        # Sample delete query
        try:
            count = self.cursor.execute('DELETE FROM Especialidade WHERE IDEspecialidade=?', IDEspecialidade).rowcount
            self.cnxn.commit()
        except Exception as error:
            return False
        return True

    def AtualizaNome(self, id, especialidade):
        # Sample update query
        try:
            count = self.cursor.execute('UPDATE Especialidade SET Especialidade=? WHERE IDEspecialidade=?', especialidade, id).rowcount
            self.cnxn.commit()
        except Exception as error:
            return False
        return True

    def PesquisaCodigo(self, IDEspecialidade):
        tsql = "SELECT * FROM Especialidade where IDEspecialidade = ?"
        with self.cursor.execute(tsql, IDEspecialidade):
            return self.cursor.fetchone()
        return ()

    def getDadosTabelaLista(self):
        tsql = "SELECT * FROM Especialidade"
        self.table_data = []
        with self.cursor.execute(tsql):
            for row in self.cursor:
                self.table_data.append(row)   # (1, 'Medicina Interna')
        return self.table_data

    def ListarDadosFormatoTabular(self):
        registos = self.getDadosTabelaLista()
        print('{0:<12s}'.format('IDEspecialidade'), end='')
        print(' {0:<50s}'.format('Especialidade'))
        for r in registos:
            print('{0:^12d}'.format(r[0]), end='')
            print(' {0:<20s}'.format(r[1]))

    def getDadosTabelaListaFiltro(self, especialidade_contem):
        tsql = "SELECT * FROM Especialidade where Especialidade like ?"
        self.table_data = []
        with self.cursor.execute(tsql, especialidade_contem):
            for row in self.cursor:
                print(row)
                self.table_data.append(row)
        return self.table_data

    def getDadosTabelaListaFiltroPerigosoMalFeitoSQLiAtaque(self, especialidade_contem):
        tsql = f"SELECT * FROM Especialidade where Especialidade like '{especialidade_contem}'"
        # print (tsql)
        self.table_data = []
        with self.cursor.execute(tsql):
            for row in self.cursor:
                print(row)
                self.table_data.append(row)
        return self.table_data
