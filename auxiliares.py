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
    with open(archivo, 'r') as f:
        try:
            jsonData = json.load(f)
            f.close()
        except json.decoder.JSONDecodeError:
            jsonData = []
        return jsonData

def splitearLista(lista, var):
    # recibe una lista de strings a splitear
    for i in range(len(lista)):
        lista[i] = lista[i].split(var)
    return lista
