
import json

def GravarJSON(filename_out , dados):
    f = open(filename_out , 'w', encoding='utf8')
    print(dados)
    json.dump(dados , f, ensure_ascii=False ,
              indent = 4) # to file
    f.close()
        # -------------

def LerJSON(filename_in):
    try:
        f = open(filename_in , encoding="utf8")
    except:
        return {"TipoClientes":[],
                'Clientes': [],
                'TipoAnalises':[],
                'Analises': [],
                'Pedidos': [],
                'Resultados': []
                }

        # Mudar de acordo com a estrutura de dados JSON
    dados = json.load(f)
    return dados

