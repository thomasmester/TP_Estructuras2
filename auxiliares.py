from main import clubes
from clases import Club

def obtenerIndice(data, dato, j):
    indice = -1
    for i in range(len(data)):
        if data[i][j] == str(dato):
            indice = i
    return indice

def guardarListaClubes():
    club_text = ''
    for c in clubes:
        club_text += c.nombre + ',' + \
            str(c.anioFundacion) + ',' + c.direccion + '|'
    with open("clubes.txt", "w") as f:
        f.write(club_text)


def inicializarListaClubes():
    with open('clubes.txt', 'r') as d:
        text = d.read()
        ListaClubes = text.split('|')
        ListaClubes = splitearLista(ListaClubes, ',')
        for i in range(len(ListaClubes)):
            if ListaClubes[i] != ['']:
                clubes.append(Club(*ListaClubes[i]))

def splitearLista(lista, var):
        ##recibe una lista de strings a splitear
        for i in range(len(lista)):
            lista[i] = lista[i].split(var)
        return lista