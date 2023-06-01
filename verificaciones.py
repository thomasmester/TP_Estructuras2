

def verificarExistenciaInstalacion(codigo, indiceClub, clubes):
    existe = False
    aux = -1
    for i in range(len(clubes[indiceClub].lista_instalaciones)):
        if clubes[indiceClub].lista_instalaciones[i].codigoInstalacion == codigo:
            aux = i
            existe = True
    datos = [existe, aux]
    return datos


def verificarNumeroInput(texto1, texto2):
    while True:
        varStr = input(texto1)
        try:
            varInt = int(varStr)
            if varInt > 0 and varInt!=None:
                break
            else:
                print("Ingreso invalido. Por favor, inténtelo de nuevo.")
        except ValueError:
            print(texto2)
    return varInt


def verificarOpcionMenu(texto1, texto2):
    while True:
        varStr = input(texto1)
        try:
            varInt = int(varStr)
            break
        except ValueError:
            print(texto2)
    return varInt


def verificarInputSinNumeros(texto1, texto2):
    data = input(texto1)
    while (data == "" or tieneNumeros(data)):
        data = input(texto2)
    return data


def verificarInputConNumeros(texto1, texto2):
    data = input(texto1)
    while (data == ""):
        data = input(texto2)
    return data


def tieneNumeros(data):
    tiene = False
    for char in data:
        if char.isdigit():
            tiene = True
    return tiene


def verificarInputClub(texto1, texto2):
    data = input(texto1)
    while (data == "" or data == "clubes"):
        data = input(texto2)
    return data


def verificarInputMail():
    data = input('Ingrese el correo electronico: ')
    while (data == "" or '@' not in data or '.com' != data[len(data)-4:] or len(data) < 5):
        data = input('Ingreso invalido. Ingrese el correo electronico: ')
    return data


def validarFecha(f):
    esValido = False
    if len(f) == 10:
        esValido = True if (f[0] + f[1] + f[3] + f[4] + f[6] + f[7] +
                            f[8] + f[9]).isdigit() and (f[2] + f[5]) == '--' else False
    return esValido


def verificarExistenciaClub(nombreClub, clubes):
    existe = False
    aux = -1
    for i in range(len(clubes)):
        if clubes[i].nombre == nombreClub:
            aux = i
            existe = True
    datos = [existe, aux]
    return datos
