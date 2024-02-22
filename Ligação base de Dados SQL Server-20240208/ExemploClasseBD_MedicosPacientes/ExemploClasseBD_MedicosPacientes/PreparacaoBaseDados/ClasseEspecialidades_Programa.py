from ClasseEspecialidades import *

bd = EspecialidadesCRUDSQLServer(server='.', database='ClinicaUpSkill')
r = bd.ApagaTabela()
r = bd.CriaTabela()

bd.ImportFromCSV('medicos.csv')
bd.ListarDadosFormatoTabular()
# Especialidade com Int na designação
print('Antes')
especialidades = bd.getDadosTabelaListaFiltro('%Int%')
print(especialidades)

# ataque: https://www.w3schools.com/sql/sql_injection.asp
# SELECT * FROM Especialidade where Especialidade like '%Int%'; delete from Especialidade; --'
# especialidades = bd.getDadosTabelaListaFiltroPerigosoMalFeitoSQLiAtaque("%Int%'; delete from Especialidade; --")
# print(especialidades)
# print('Depois: os dados foram eliminados')
# especialidades = bd.getDadosTabelaListaFiltro('%Int%')
# print(especialidades)
