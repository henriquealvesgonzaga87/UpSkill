# Resultados

import Menus.Menus
import  Configuration.Configuracao
import LerGravarDados.LerGravarDados as ld
import ValidationData.ValidacaoDados as vd
import ValidationData.validators_pt as vd2
from Resultados.Inserir import *
from Resultados.PesquisaTipoAnalise import *
from Resultados.ListartodosHTML import *
from Resultados.PesquisaData import *
from Resultados.PesquisaResultados import *
from Resultados.Pesquisanome import *
from Resultados.procuraresultado import *

def Menu():
	while True:
		op = Menus.Menus.Menu("Resultados",['Inserir ou Alterar','PesquisaTipoAnalise','PesquisaCliente','PesquisaData','PesquisaResultados','Listar Resultado','ListarTodosHtml'], 6)
		if op == 0:
			break
		elif op == 1:
			Inserir()
		elif op == 2:
			PesquisaTipoAnalise()
		elif op == 3:
			PesquisaCliente()
		elif op == 4:
			PesquisaData()
		elif op == 5:
			PesquisaResultados()
		elif op == 6:
			procuraresultado()
		elif op == 7:
			ListartodosHTML()

