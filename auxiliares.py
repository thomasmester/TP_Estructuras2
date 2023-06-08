from clases import Club
import json
#sacar este import y manejar el import en Club

def obtenerIndice(data, dato, j):
    indice = -1
    for i in range(len(data)):
        if data[i][j] == str(dato):
            indice = i
    return indice
def jsonHandler(archivo):
    try:
        with open(archivo, 'r') as f:
            try:
                jsonData = json.load(f)
                f.close()
            except json.decoder.JSONDecodeError:
                jsonData = []
    except FileNotFoundError:
        print("El archivo no existe")
    return jsonData
    
def clubADicts(club):
    cDict = club.__dict__
    for i in range(len(cDict['lista_socios'])):
        cDict['lista_socios'][i] = cDict['lista_socios'][i].__dict__
    for i in range(len(cDict['lista_pagos'])):
        cDict['lista_pagos'][i] = cDict['lista_pagos'][i].__dict__
        cDict['lista_pagos'][i]['fecha'] = str(cDict['lista_pagos'][i]['fecha'])
    for i in range(len(cDict['lista_empleados'])):
        cDict['lista_empleados'][i] = cDict['lista_empleados'][i].__dict__
    for i in range(len(cDict['lista_instalaciones'])):
        cDict['lista_instalaciones'][i] = cDict['lista_instalaciones'][i].__dict__
        for j in range(len(cDict['lista_instalaciones'][i]['lista_reservas'])):
            cDict['lista_instalaciones'][i]['lista_reservas'][j] = cDict['lista_instalaciones'][i]['lista_reservas'][j].__dict__
            cDict['lista_instalaciones'][i]['lista_reservas'][j]['fechaReserva'] = str(cDict['lista_instalaciones'][i]['lista_reservas'][j]['fechaReserva'])
    return cDict

    return cDict
def splitearLista(lista, var):
    # recibe una lista de strings a splitear
    for i in range(len(lista)):
        lista[i] = lista[i].split(var)
    return lista
