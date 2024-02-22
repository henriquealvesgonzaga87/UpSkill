
import Menus.Menus
import Medicos.MenuMedicos
import Pacientes.MenuPacientes
import Especialidades.MenuEspecialidades
import Consultas.MenuConsultas

while True:
	op = Menus.Menus.Menu("Gestão Consultas Médicas",['Medicos','Pacientes','Especialidades','Consultas'], 4)
	if op == 0:
		break
	elif op == 1:
		Medicos.MenuMedicos.Menu()
	elif op == 2:
		Pacientes.MenuPacientes.Menu()
	elif op == 3:
		Especialidades.MenuEspecialidades.Menu()
	elif op == 4:
		Consultas.MenuConsultas.Menu()

