import os
import seedir as sd
os.system("del *.xml /s")
os.system("del *.pyc /s")
os.system("del *.iml /s")
os.system("del .name /s")
os.system("del .gitignore /s")
os.system("del __pycache__ /s /q")


sd.seedir(os.getcwd(), style='emoji')

