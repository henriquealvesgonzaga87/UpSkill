# refazer: lembrar de testar o nº de empregados para depois testar o total de negocios e total de balanço

def get_empregados(msg, minimo):
    while True:
        try:
            valor = int(input(msg))
            if valor >= minimo:
                return valor
            else:
                print(f"O valor deve ser no mínimo {minimo}")
        except:
            print(f"O valor deve ser um numero a partir de {minimo}")


def get_valores_negocio_balanco(msg, minimo):
    while True:
        try:
            valor = float(input(msg))
            if valor >= minimo:
                return valor
            else:
                print(f"O valor deve ser no mínimo {minimo}")
        except:
            print(f"O valor deve ser um numero a partir de {minimo}")


def tipo_empresa(empregados, total_negocio, total_balanco):
    if (total_negocio <= 2000000 or total_balanco <= 2000000) and empregados < 10:
        empresa = 'Micro Empresa'
    else:
        if (total_negocio <= 10000000 or total_balanco <= 10000000) and empregados < 50:
            empresa = 'Pequena empresa'
        else:
            if (total_negocio <= 50000000 or total_balanco <= 43000000) and empregados < 250:
                empresa = 'Media empresa'
            else:
                empresa = 'Grande empresa'
    return empresa


empregados = int(get_empregados('Digite o nº de empregados: ', 1))
total_negocio = get_valores_negocio_balanco('Informe o total de negócios: ', 0)
total_balanco = get_valores_negocio_balanco('Informe o total do balanço: ', 0)
empresa = tipo_empresa(empregados=empregados, total_negocio=total_negocio, total_balanco=total_balanco)

print(f'''Com {empregados} empregados;
com um total de negócios {total_negocio},
com total de balanço {total_balanco}
A sua empresa é qualificada como: {empresa}''')

# # refazer: lembrar de testar o nº de empregados para depois testar o total de negocios e total de balanço
#
# def get_value(msg, minimo, maximo):
#     while True:
#         try:
#             valor = int(input(msg))
#             if minimo <= valor <= maximo:
#                 return valor
#             else:
#                 print(f"O valor deve ser entre {minimo} e {maximo}")
#         except:
#             print(f"O valor deve ser um numero entre {minimo} e {maximo}")
#
#
# empregados = int(get_value('Digite o nº de empregados: ', 1, 999999999999))
# total_negocio = get_value('Informe o total de negócios: ', 0, 999999999999)
# total_balanco = get_value('Informe o total do balanço: ', 0, 999999999999)
# empresa = ''
#
# # if (total_negocio <= 2000000 or total_balanco <= 2000000) and empregados < 10:
# #     empresa = 'Micro Empresa'
# # else:
# #     if (total_negocio <= 10000000 or total_balanco <= 10000000) and empregados < 50:
# #         empresa = 'Pequena empresa'
# #     else:
# #         if (total_negocio <= 50000000 or total_balanco <= 43000000) and empregados < 250:
# #             empresa = 'Media empresa'
# #         else:
# #             empresa = 'Grande empresa'
#
# if (total_negocio <= 2000000 or total_balanco <= 2000000) and empregados < 10:
#     empresa = 'Micro Empresa'
# if (total_negocio <= 10000000 or total_balanco <= 10000000) and empregados < 50:
#     empresa = 'Pequena empresa'
# if (total_negocio <= 50000000 or total_balanco <= 43000000) and empregados < 250:
#     empresa = 'Media empresa'
# else:
#     empresa = 'Grande empresa'
#
#
# print(f'''Com {empregados} empregados;
# com um total de negócios {total_negocio},
# com total de balanço {total_balanco}
# A sua empresa é qualificada como: {empresa}''')
