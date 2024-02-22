import pyodbc


class CMedicos:
    def __init__(self, server='.', database='ClinicaUpSkill'):
        self.table_names = []
        self.database = database
        driver = "ODBC Driver 17 for SQL Server"
        self.cnxn = pyodbc.connect(f'Driver={driver};' f'Server={server};'
                                   f'Database={database};'
                                   'Trusted_Connection=yes;')
        self.cursor = self.cnxn.cursor()


    def CriaTabela(self):
        # erros: https://www.educative.io/answers/what-are-the-exceptions-while-connecting-to-sql-server-in-python
        try:
            c = self.cursor.execute('''CREATE TABLE Medicos (
                                        id_medico int CONSTRAINT PK_medico PRIMARY KEY IDENTITY(1, 1),
                                        nome nvarchar(200) NOT NULL,
                                        especialidade nvarchar(200) NOT NULL,
                                        instituicao nvarchar(200),
                                        cedula_numero int NOT NULL,
                                        numero_ordem int NOT NULL,
                                        data_nascimento date NOT NULL)
                                        ''')
            self.cnxn.commit()
        except Exception as error:
            return (False, error)
        return True

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
            self.inserir(m['Nome'], m['Especialidade'], m['Instituição'], m['Cédula Número'], m['Número Ordem'], m['Data Nascimento'])

    def inserir(self, nome, especialidade, instituicao, cedula_numero, numero_ordem, data_nascimento):
        # Sample insert query
        try:
            count = self.cursor.execute('''
INSERT INTO Medicos (nome, especialidade, instituicao, cedula_numero, numero_ordem, data_nascimento) 
VALUES 
(?, ?, ?, ?, ?, ?)''', nome, especialidade, instituicao, cedula_numero, numero_ordem, data_nascimento).rowcount
            self.cnxn.commit()
        except Exception as error:
            return False
        return True
