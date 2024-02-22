import Menus.Menus

import LerGravarDados.LerGravarDados as ld
import Configuration.Configuracao as c


def ListartodosHTML():
    dados = ld.LerJSON(c.nomeFicheiroTipoJSON)

    fic = 'Resultados.HTML'
    f = open(fic, 'w', encoding='utf8')

    style ='''
    <style>
        table, th, td {
        border: 1px solid blue;
        border-collapse: collapse;
        }
    </style>    
    '''
    print(style, file=f)

    print('<img height="50px" src="https://cloud.sysnovare.pt/ipg/imagens/LogotipoSIdtmod20211209120035" id="logotipo">',file=f)


    print('<img height="50px" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEASABIAAD/4QCgRXhpZgAATU0AKgAAAAgABQEaAAUAAAABAAAASgEbAAUAAAABAAAAUgEoAAMAAAABAAIAAAEyAAIAAAAUAAAAWodpAAQAAAABAAAAbgAAAAAAAABIAAAAAQAAAEgAAAABMjAyMToxMjowOSAxMTo0MDo0MgAAA6ABAAMAAAABAAEAAKACAAMAAAABASMAAKADAAMAAAABAIIAAAAAAAD/4Qs1aHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLwA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA1LjUuMCI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zLmFkb2JlLmNvbS9waG90b3Nob3AvMS4wLyIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIgcGhvdG9zaG9wOkNvbG9yTW9kZT0iMyIgcGhvdG9zaG9wOklDQ1Byb2ZpbGU9InNSR0IgSUVDNjE5NjYtMi4xIiB4bXA6TW9kaWZ5RGF0ZT0iMjAyMS0xMi0wOVQxMTo0MDo0MloiIHhtcDpNZXRhZGF0YURhdGU9IjIwMjEtMTItMDlUMTE6NDA6NDJaIj4gPHhtcE1NOkhpc3Rvcnk+IDxyZGY6U2VxPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0icHJvZHVjZWQiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFmZmluaXR5IERlc2lnbmVyIDEuMTAuNCIgc3RFdnQ6d2hlbj0iMjAyMS0xMi0wOVQxMTo0MDo0MloiLz4gPC9yZGY6U2VxPiA8L3htcE1NOkhpc3Rvcnk+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDw/eHBhY2tldCBlbmQ9InciPz7/7QAsUGhvdG9zaG9wIDMuMAA4QklNBCUAAAAAABDUHYzZjwCyBOmACZjs+EJ+/+ICZElDQ19QUk9GSUxFAAEBAAACVGxjbXMEMAAAbW50clJHQiBYWVogB+UADAAJAAsAJwARYWNzcE1TRlQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPbWAAEAAAAA0y1sY21zAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALZGVzYwAAAQgAAAA+Y3BydAAAAUgAAABMd3RwdAAAAZQAAAAUY2hhZAAAAagAAAAsclhZWgAAAdQAAAAUYlhZWgAAAegAAAAUZ1hZWgAAAfwAAAAUclRSQwAAAhAAAAAgZ1RSQwAAAhAAAAAgYlRSQwAAAhAAAAAgY2hybQAAAjAAAAAkbWx1YwAAAAAAAAABAAAADGVuVVMAAAAiAAAAHABzAFIARwBCACAASQBFAEMANgAxADkANgA2AC0AMgAuADEAAG1sdWMAAAAAAAAAAQAAAAxlblVTAAAAMAAAABwATgBvACAAYwBvAHAAeQByAGkAZwBoAHQALAAgAHUAcwBlACAAZgByAGUAZQBsAHlYWVogAAAAAAAA9tYAAQAAAADTLXNmMzIAAAAAAAEMQgAABd7///MlAAAHkwAA/ZD///uh///9ogAAA9wAAMBuWFlaIAAAAAAAAG+gAAA4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">',file=f)

    print("<table>", file=f)
    print(f"<tr><th>{'Código':>6}</th><th>{'Data':>20}</th><th>{'CódigoCliente':>15}</th><th>{'CódigoTipoAnalise':>20}</th><th>{'Resultado':>10}</th></tr>",file=f)
    for x in dados["Resultados"]:
        print(f"<tr><td>{x['Código']:>6}</td><td>{x['Data']:>20}</td><td>{x['CódigoCliente']:>15}</td><td>{x['CódigoTipoAnalise']:>20}</td><td>{x['Resultado']:>10}</td></tr>",file=f)

    print("</table>", file=f)
    f.close()
    import os

    os.system(fic)

    Menus.Menus.Pausa('Listar todos HTML')