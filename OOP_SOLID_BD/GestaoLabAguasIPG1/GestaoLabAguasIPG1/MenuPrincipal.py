
import Menus.Menus
import TipoClientes.MenuTipoClientes
import Clientes.MenuClientes
import TipoAnalises.MenuTipoAnalises
import Pedidos.MenuPedidos
import Resultados.MenuResultados
import Funcionarios.MenuUtilizadores


while True:
	op = Menus.Menus.Menu("Gestão lab águas IPG",['Tipo Clientes','Clientes','Utilizadores','Tipo Analises','Pedidos','Resultados'], 6)
	if op == 0:
		break
	elif op == 1:
		TipoClientes.MenuTipoClientes.Menu()
	elif op == 2:
		Clientes.MenuClientes.Menu()
	elif op == 3:
		Funcionarios.MenuUtilizadores.Menu()
	elif op == 4:
		TipoAnalises.MenuTipoAnalises.Menu()
	elif op == 5:
		Pedidos.MenuPedidos.Menu()
	elif op == 6:
		Resultados.MenuResultados.Menu()

