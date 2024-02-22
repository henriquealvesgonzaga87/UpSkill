
class bcolors:
    HEADER = '[95m'
    OKBLUE = '[94m'
    OKCYAN = '[96m'
    OKGREEN = '[92m'
    WARNING = '[93m'
    FAIL = '[91m'
    ENDC = '[0m'
    BOLD = '[1m'
    UNDERLINE = '[4m'
    NORMAL = '[00m'

def print2(cor, prt):
    print(f"{cor}{prt}{bcolors.NORMAL}")
    
def Menu(Titulo, Opcoes, np):
    print2(bcolors.OKBLUE, "* " * 5 + Titulo + " *" * 5)
    print()
    for i in range(np):
        print(i + 1, "-", Opcoes[i])
    print("0 - Terminar")
    while True:
        try:
            op = int(input("Opção?"))
        except ValueError:
            print ("Não digitou um número inteiro!")
            continue
        if op >= 0 and op <= np:
            break
        else:
            print ("O valor deve estar entre %d e %d" % (0, np))

    return op

def Pausa(msg=''):
    input(msg + " Prima a tecla Enter para continuar ...")


def Pausa1(msg=''):
    import keyboard
    # Check if b was pressed
    #if keyboard.is_pressed('b'):
	#   print('b Key was pressed')
    print(msg + " Prima qq tecla para continuar ...", end='')
    while True:
        if keyboard.read_key():
            print()
            break

