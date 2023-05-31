from clases import Club


def obtenerIndice(data, dato, j):
    indice = -1
    for i in range(len(data)):
        if data[i][j] == str(dato):
            indice = i
    return indice


def splitearLista(lista, var):
    # recibe una lista de strings a splitear
    for i in range(len(lista)):
        lista[i] = lista[i].split(var)
    return lista
