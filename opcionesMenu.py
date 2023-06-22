from verificaciones import *
from auxiliares import *
import matplotlib.pyplot as plt
from datetime import date
from operator import itemgetter
from clases.Club import *
from clases.Socio import *
from clases.Instalacion import *
from clases.Reserva import *
from clases.Empleado import *
from clases.Pago import *
from clases.Invitado import *
from opcionesIngreso import *
clubes = []


def guardarListaClubes():
    club_text = ''
    for c in clubes:
        club_text += c.nombre + ',' + \
            str(c.anioFundacion) + ',' + c.direccion + '|'
    with open("clubes.txt", "w") as f:
        f.write(club_text)


def getListaClubes():
    return clubes


def inicializarListaClubes():
    with open('clubes.txt', 'r') as d:
        text = d.read()
        ListaClubes = text.split('|')
        ListaClubes = splitearLista(ListaClubes, ',')
        for i in range(len(ListaClubes)):
            if ListaClubes[i] != ['']:
                clubes.append(Club(*ListaClubes[i]))


def inicializar():
    inicializarListaClubes()
    for c in clubes:
        inicializarClub(c)


def inicializarClub(c):
    data = jsonHandler(c.nombre + '.json')

    for i in range(len(data['lista_socios'])):
        c.lista_socios.append(Socio(**data['lista_socios'][i]))
    for i in range(len(data['lista_pagos'])):
        c.lista_pagos.append(Pago(**data['lista_pagos'][i]))
    for i in range(len(data['lista_empleados'])):
        c.lista_empleados.append(Empleado(**data['lista_empleados'][i]))
    for i in range(len(data['lista_instalaciones'])):
        c.lista_instalaciones.append(Instalacion(
            *list(data['lista_instalaciones'][i].values())[0:5]))
        for j in range(len(data['lista_instalaciones'][i]['lista_reservas'])):
            c.lista_instalaciones[i].lista_reservas.append(
                Reserva(**data['lista_instalaciones'][i]['lista_reservas'][j]))


def eliminarInvitado():
    jsonData = jsonHandler('invitados.json')
    indice = -1
    while (indice == -1):
        opcion = verificarOpcionMenu("Seleccione de que manera quiere eliminar al invitado" + '\n' + "1: Por DNI" + '\n'+"2: Por mail" +
                                     '\n', "Opcion invalida. Seleccione de que manera quiere eliminar al invitado" + '\n' + "1: Por DNI" + '\n'+"2: Por mail" + '\n')
        match opcion:
            case 1:
                dni = verificarNumeroInput(
                    'Ingresar DNI: ', 'Ingresar un DNI valido: ')
                indice = obtenerIndiceJson(jsonData, str(dni), "DNI")
            case 2:
                Mail = verificarInputMail()
                indice = obtenerIndiceJson(jsonData, str(Mail), "email")
        if (indice == -1):
            print('Datos invalidos. Ingresar los datos nuevamente')
    jsonData.pop(indice)
    with open("invitados.json", 'w') as file:
        js = json.dumps(jsonData)
        file.write(js)
    print('El invitado ha sido eliminado correctamente. ')


def visualizarInvitadosMenosAcceso():
    jsonData = jsonHandler('invitados.json')
    jsonDataOrdenado = sorted(jsonData, key=itemgetter("cantVecesIngresa"))
    DNIs = []
    cantidadIngresos = []
    for i in range(len(jsonDataOrdenado)):
        if i < 5:
            DNIs.append(str(jsonDataOrdenado[i]["DNI"]))
            cantidadIngresos.append(
                int(jsonDataOrdenado[i]["cantVecesIngresa"]))
    x_vals = list(range(len(DNIs)))
    plt.title(label='Cant. ingresos por usuario con menor acceso',
              fontsize=20, color='red')
    plt.xticks(x_vals, DNIs)
    plt.xlabel('DNIs')
    plt.ylabel('Cantidad de ingresos')
    plt.bar(DNIs, cantidadIngresos, color='blue', width=0.5)
    plt.show()


def cambiarContrasenaUsuario():
    jsonData = jsonHandler('admins.json')
    encontrado = False
    texto = ''
    while not encontrado:
        print(texto)
        usuario = verificarInputConNumeros(
            'Ingresar usuario: ', 'Usuario invalido. Ingrese otro usuario: ')
        contrasenaActual = verificarInputConNumeros(
            'Ingresar contrasena actual: ', 'Contrasena actual invalida. Ingrese otra contrasena: ')
        for i in range(len(jsonData)):
            if jsonData[i] != [''] and jsonData[i]["usuario"] == usuario and jsonData[i]["contrasenia"] == str(contrasenaActual):
                encontrado = True
                indice = i
        texto = 'Usuario o contraseña invalidos. Ingresar los datos nuevamente.'
    contrasenaNueva = verificarInputConNumeros(
        'Ingresar contrasena nueva: ', 'Contrasena actual invalida. Ingrese otra contrasena: ')
    jsonData[indice]["contrasenia"] = contrasenaNueva
    with open("admins.json", 'w') as file:
        js = json.dumps(jsonData)
        file.write(js)
    print('Contrasena actualizada exitosamente')


def mostrarInvitados():
    jsonData = jsonHandler('invitados.json')
    if jsonData != None:
        for i in range(len(jsonData)):
            invitado = Invitado(jsonData[i]["nombre"], jsonData[i]["apellido"], jsonData[i]
                                ["DNI"], jsonData[i]["email"], jsonData[i]["cantVecesIngresa"])
            print(invitado)
    else:
        print('No hay usuarios invitados registrados.')


def clubGrafico():
    nombreClub = input(
        "Ingrese el nombre del club que quiere consultar informacion: ")
    datos = verificarExistenciaClub(nombreClub, clubes)
    while (datos[0] == False):
        nombreClub = input(
            "Ese club no existe. Ingrese el nombre del club que quiere consultar informacion: ")
        datos = verificarExistenciaClub(nombreClub, clubes)
    for socio in clubes[datos[1]].lista_socios:
        clubes[datos[1]].agregaEdad(socio.edad)
    clubes[datos[1]].clasifica()
    return clubes[datos[1]].clasificacion


def graficoEdades():
    clasificacion = clubGrafico()
    rangos = ["1-18", "18-60", "+60"]
    cantidad = []
    for i in clasificacion:
        cantidad.append(i)
    plt.title("Socios por rango etario")
    plt.xlabel("Rangos", loc="right")
    plt.ylabel("Cantidad")
    plt.bar(rangos, cantidad, color="blue", width=0.5)
    return plt.show()


def finalizarPrograma():
    for c in clubes:
        cDict = clubADicts(c)
        with open('{}.json'.format(cDict['nombre']), 'w') as f:
            cDict.pop('edades')
            cDict.pop('clasificacion')
            js = json.dumps(cDict)
            f.write(js)
        guardarListaClubes()
    print('Sesión cerrada, programa finalizado')
    quit()


def actualizarDatosInvitado():
    jsonData = jsonHandler('invitados.json')
    encontrado = False
    dni = verificarNumeroInput('Ingresar DNI del usuario a actualizar los datos: ',
                               'Usuario invalido. Ingrese DNI del usuario para actualizar sus datos: ')
    correo = verificarInputConNumeros("Ingrese el correo del invitado al que le quiere actualizar los datos: ",
                                      "Correo invalido. Ingrese el correo del invitado al que le quiere actualizar los datos: ")
    for i in range(len(jsonData)):
        if jsonData[i] != [''] and int(jsonData[i]["DNI"]) == dni and jsonData[i]["email"] == correo:
            encontrado = True
            indice = i
    if not encontrado:
        print("El invitado no esta registrado. A continuacion puede registrarlo: ")
        case3()
    else:
        print("Actualizacion de datos")
        nombre = verificarInputSinNumeros(
            'Ingresar su nombre para actualizarlo: ', 'Nombre invalido. Ingrese su nombre para actualizarlo: ')
        apellido = verificarInputSinNumeros(
            'Ingresar su apellido para actualizarlo: ', 'Apellido invalido. Ingrese su apellido para actualizarlo: ')
        correo = verificarInputConNumeros(
            "Ingrese su correo para actualizarlo: ", "Correo invalido. Ingrese su correo para actualizarlo: ")
        jsonData[indice]["nombre"] = nombre
        jsonData[indice]["apellido"] = apellido
        jsonData[indice]["email"] = correo
        with open("invitados.json", 'w') as file:
            js = json.dumps(jsonData)
            file.write(js)
        print('Invitado actualizado exitosamente')


def registrarClub():
    agrega = True
    nombre = verificarInputClub(
        "Ingrese el nombre del club: ", "Ingrese un nombre de club valido: ")
    anioFundacionInt = verificarNumeroInput(
        "Ingrese el año de fundacion: ", "Ingrese un año de fundacion valido: ")
    direccion = verificarInputConNumeros(
        "Ingrese la direccion: ", "Ingrese una direccion de club valida: ")
    try:
        club = Club(nombre, anioFundacionInt, direccion)
    except ValueError:
        print("Ese nombre ya existe")
        agrega = False
    if agrega:
        clubes.append(club)
        print("Se ha registrado el club exitosamente")


def consultarInfoClub():
    nombreClub = input(
        "Ingrese el nombre del club que quiere consultar informacion: ")
    datos = verificarExistenciaClub(nombreClub, clubes)
    while (datos[0] == False):
        nombreClub = input(
            "Ese club no existe. Ingrese el nombre del club que quiere consultar informacion: ")
        datos = verificarExistenciaClub(nombreClub, clubes)
    print(clubes[datos[1]])


def registrarSocio():
    nombre = verificarInputSinNumeros(
        "Ingrese el nombre del socio: ", "Ingrese un nombre valido: ")
    apellido = verificarInputSinNumeros(
        "Ingrese el apellido del socio: ", "Ingrese un apellido valido: ")
    sexo = verificarInputSinNumeros(
        "Ingrese el sexo del socio: ", "Ingrese un sexo valido: ")
    edadInt = verificarNumeroInput(
        "Ingrese la edad del socio: ", "Edad invalida. Ingrese la edad del socio: ")
    dniInt = verificarNumeroInput(
        "Ingrese el DNI del socio: ", "DNI invalido. Ingrese el DNI del socio: ")
    nroSocioInt = verificarNumeroInput(
        "Ingrese el numero de socio: ", "Numero de socio invalido. Ingrese el numero de socio: ")
    correoElectronico = verificarInputMail()
    nombreClub = input(
        "Ingrese el nombre del club en el que desea registrar el socio: ")
    datos = verificarExistenciaClub(nombreClub, clubes)
    while (datos[0] == False):
        nombreClub = input(
            "Club inexistente. Ingrese el nombre del club en el que desea registrar el socio: ")
        datos = verificarExistenciaClub(nombreClub, clubes)
    socio = Socio(nombre, apellido, sexo, edadInt,
                  dniInt, nroSocioInt, correoElectronico)
    clubes[datos[1]].agregarSocio(socio)


def eliminarSocio():
    nombreClub = input(
        "Ingrese el nombre del club en el que desea eliminar un socio: ")
    datos = verificarExistenciaClub(nombreClub, clubes)
    while (datos[0] == False):
        nombreClub = input(
            "Club inexistente. Ingrese el nombre del club en el que desea eliminar un socio: ")
        datos = verificarExistenciaClub(nombreClub, clubes)
    nroSocioInt = verificarNumeroInput(
        "Ingrese el numero de socio del socio que desea eliminar: ", "Numero de socio invalido. Intente nuevamente")
    clubes[datos[1]].eliminarSocio(nroSocioInt)


def consultarSocios():
    nombreClub = input("Ingrese el club del que quiere consultar los socios: ")
    datos = verificarExistenciaClub(nombreClub, clubes)
    while (datos[0] == False):
        nombreClub = input(
            "Nombre de club inexistente. Ingrese el club del que quiere consultar los socios: ")
        datos = verificarExistenciaClub(nombreClub, clubes)
    if len(clubes[datos[1]].lista_socios) == 0:
        print("No hay socios registrados en este club")
        for j in range(len(clubes[datos[1]].lista_socios)):
            print(clubes[datos[1]].lista_socios[j])


def registrarInstalacion():
    nombre = verificarInputSinNumeros(
        "Ingrese el nombre de la instalacion: ", "Ingrese un nombre valido: ")
    descripcion = verificarInputConNumeros(
        "Ingrese la descripcion de la instalacion: ", "Ingrese una descripcion valida: ")
    horaApertura = verificarInputConNumeros(
        "Ingrese la hora de apertura de la instalacion: ", "Ingrese un horario valido: ")
    horaCierre = verificarInputConNumeros(
        "Ingrese la hora de cierre de la instalacion: ", "Ingrese un horario valido: ")
    codigoInstalacionInt = verificarNumeroInput(
        "Ingrese el codigo de la instalacion que desea registrar: ", "Ingrese un codigo de instalacion valido: ")
    nombreClub = input(
        "Ingrese el nombre del club en el que desea registrar la instalacion: ")
    datos = verificarExistenciaClub(nombreClub, clubes)
    while (datos[0] == False):
        nombreClub = input(
            "Club inexistente. Ingrese el nombre del club en el que desea registrar la instalacion: ")
        datos = verificarExistenciaClub(nombreClub, clubes)
    instalacion = Instalacion(
        nombre, descripcion, horaApertura, horaCierre, codigoInstalacionInt)
    clubes[datos[1]].agregarInstalacion(instalacion)


def eliminarInstalacion():
    nombreClub = input(
        "Ingrese el nombre del club en el que desea eliminar una instalacion: ")
    datos = verificarExistenciaClub(nombreClub, clubes)
    while (datos[0] == False):
        nombreClub = input(
            "Club inexistente. Ingrese el nombre del club en el que desea eliminar una instalacion: ")
        datos = verificarExistenciaClub(nombreClub, clubes)
    codigoInstalacionInt = verificarNumeroInput(
        "Ingrese el codigo de la instalacion que desea eliminar: ", "Ingrese un codigo de instalacion valido: ")
    clubes[datos[1]].eliminarInstalacion(codigoInstalacionInt)


def consultarInstalaciones():
    nombreClub = input(
        'Ingrese el club del que desea consultar las instalaciones: ')
    datos = verificarExistenciaClub(nombreClub, clubes)
    while (datos[0] == False):
        nombreClub = input(
            'Nombre del club inexistente. Ingrese el club del que quiere consultar las instalaciones: ')
        datos = verificarExistenciaClub(nombreClub, clubes)
    if len(clubes[datos[1]].lista_instalaciones) == 0:
        print("No hay instalaciones registradas en este club")
        for j in range(len(clubes[datos[1]].lista_instalaciones)):
            print(clubes[datos[1]].lista_instalaciones[j])


def registrarEmpleado():
    nombre = verificarInputSinNumeros(
        "Ingrese el nombre del empleado: ", "Ingrese un nombre valido: ")
    apellido = verificarInputSinNumeros(
        "Ingrese el apellido del empleado: ", "Ingrese un apellido valido: ")
    sexo = verificarInputSinNumeros(
        "Ingrese el sexo del empleado: ", "Ingrese un sexo valido: ")
    edadInt = verificarNumeroInput(
        "Ingrese la edad del empleado: ", "Edad invalida. Ingrese la edad del empleado: ")
    dniInt = verificarNumeroInput(
        "Ingrese el DNI del empleado: ", "DNI invalido. Ingrese el DNI del empleado: ")
    legajoInt = verificarNumeroInput("Ingrese el numero de legajo del empleado: ",
                                     "Numero de legajo invalido. Ingrese el numero de legajo del empleado: ")
    cargo = verificarInputSinNumeros(
        "Ingrese el cargo del empleado: ", "Ingrese un cargo valido: ")
    salarioInt = verificarNumeroInput(
        "Ingrese el salario actual del empleado: ", "Salario invalido. Ingrese el salario del empleado: ")
    nombreClub = input(
        "Ingrese el nombre del club en el que desea registrar el empleado: ")
    datos = verificarExistenciaClub(nombreClub, clubes)
    while (datos[0] == False):
        nombreClub = input(
            "Club inexistente. Ingrese el nombre del club en el que desea registrar el empleado: ")
        datos = verificarExistenciaClub(nombreClub, clubes)
    empleado = Empleado(nombre, apellido, sexo, edadInt,
                        dniInt, legajoInt, cargo, salarioInt)
    clubes[datos[1]].agregarEmpleado(empleado)


def eliminarEmpleado():
    nombreClub = input(
        "Ingrese el nombre del club en el que desea eliminar un empleado: ")
    datos = verificarExistenciaClub(nombreClub, clubes)
    while (datos[0] == False):
        nombreClub = input(
            "Club inexistente. Ingrese el nombre del club en el que desea eliminar un socio: ")
        datos = verificarExistenciaClub(nombreClub, clubes)
    legajo = verificarNumeroInput(
        "Ingrese el legajo del empleado que desea eliminar: ", "Numero de legajo invalido. Intente nuevamente")
    clubes[datos[1]].eliminarEmpleado(legajo)


def consultarEmpleados():
    nombreClub = input(
        'Ingrese el club del que desea consultar los empleados: ')
    datos = verificarExistenciaClub(nombreClub, clubes)
    while (datos[0] == False):
        nombreClub = input(
            'Nombre del club inexistente. Ingrese el club del que quiere consultar los empleados: ')
        datos = verificarExistenciaClub(nombreClub, clubes)
    if len(clubes[datos[1]].lista_empleados) == 0:
        print("No hay empleados registrados en este club")
        for j in range(len(clubes[datos[1]].lista_empleados)):
            print(clubes[datos[1]].lista_empleados[j])


def generarPago():
    montoInt = verificarNumeroInput(
        "Ingrese el monto: ", "Monto invalido. Ingrese el monto: ")
    fecha = verificarInputConNumeros("Ingrese la fecha con el formato DD-MM-YYYY: ",
                                     "Ingrese una fecha valida siguiendo el formato DD-MM-YYYY: ")
    esValido = validarFecha(fecha)
    while esValido == False:
        fecha = verificarInputConNumeros("Formato invalido. Ingrese la fecha con el formato DD-MM-YYYY: ",
                                         "Ingrese una fecha valida siguiendo el formato DD-MM-YYYY: ")
        esValido = validarFecha(fecha)
    ano = int(fecha[6:])
    mes = int(fecha[3:5])
    dia = int(fecha[0:2])
    while (mes not in range(1, 13) or dia not in range(1, 32) or ano < 0):
        print('Fecha invalida')
        fecha = verificarInputConNumeros(
            "Ingrese la fecha con el formato DD-MM-YYYY: ", "Ingrese una fecha valida siguiendo el formato DD-MM-YYYY: ")
        esValido = validarFecha(fecha)
        while esValido == False:
            fecha = verificarInputConNumeros("Formato invalido. Ingrese la fecha con el formato DD-MM-YYYY: ",
                                             "Ingrese una fecha valida siguiendo el formato DD-MM-YYYY: ")
            esValido = validarFecha(fecha)
        ano = int(fecha[6:])
        mes = int(fecha[3:5])
        dia = int(fecha[0:2])
    fechadt = date(ano, mes, dia)
    codigoPagoInt = verificarNumeroInput(
        "Ingrese el codigo de pago: ", "Codigo de pago invalido. Ingrese el codigo de pago: ")
    nombreClub = input(
        "Ingrese el nombre del club en el que desea generar el pago: ")
    datos = verificarExistenciaClub(nombreClub, clubes)
    while (datos[0] == False):
        nombreClub = input(
            "Club inexistente. Ingrese el nombre del club en el que desea generar el pago: ")
        datos = verificarExistenciaClub(nombreClub, clubes)
    nroSocioInt = verificarNumeroInput(
        "Ingrese el numero de socio: ", "Numero de socio invalido. Ingrese el numero de socio: ")
    pago = Pago(montoInt, fechadt, nroSocioInt, codigoPagoInt)
    clubes[datos[1]].agregarPago(pago)


def eliminarPago():
    nombreClub = input(
        "Ingrese el nombre del club en el que desea eliminar un pago: ")
    datos = verificarExistenciaClub(nombreClub, clubes)
    while (datos[0] == False):
        nombreClub = input(
            "Club inexistente. Ingrese el nombre del club en el que desea eliminar un pago: ")
        datos = verificarExistenciaClub(nombreClub, clubes)
    nroPagoInt = verificarNumeroInput("Ingrese el numero de pago del pago que desea eliminar: ",
                                      "Numero de pago invalido. Ingrese el numero de pago del pago que desea eliminar: ")
    clubes[datos[1]].eliminarPago(nroPagoInt)


def consultarPagos():
    nombreClub = input('Ingrese el club del que desea consultar los pagos: ')
    datos = verificarExistenciaClub(nombreClub, clubes)
    while (datos[0] == False):
        nombreClub = input(
            'Nombre del club inexistente. Ingrese el club del que quiere consultar los pagos: ')
        datos = verificarExistenciaClub(nombreClub, clubes)
    if len(clubes[datos[1]].lista_pagos) == 0:
        print("No hay pagos registrados en este club")
        for j in range(len(clubes[datos[1]].lista_pagos)):
            print(clubes[datos[1]].lista_pagos[j])


def crearReserva():
    fecha = verificarInputConNumeros("Ingrese la fecha con el formato DD-MM-YYYY: ",
                                     "Ingrese una fecha valida siguiendo el formato DD-MM-YYYY: ")
    esValido = validarFecha(fecha)
    while esValido == False:
        fecha = verificarInputConNumeros("Formato invalido. Ingrese la fecha con el formato DD-MM-YYYY: ",
                                         "Ingrese una fecha valida siguiendo el formato DD-MM-YYYY: ")
        esValido = validarFecha(fecha)
    ano = int(fecha[6:])
    mes = int(fecha[3:5])
    dia = int(fecha[0:2])
    while (mes not in range(1, 13) or dia not in range(1, 32) or ano < 0):
        print('Fecha invalida')
        fecha = verificarInputConNumeros(
            "Ingrese la fecha con el formato DD-MM-YYYY: ", "Ingrese una fecha valida siguiendo el formato DD-MM-YYYY: ")
        esValido = validarFecha(fecha)
        while esValido == False:
            fecha = verificarInputConNumeros("Formato invalido. Ingrese la fecha con el formato DD-MM-YYYY: ",
                                             "Ingrese una fecha valida siguiendo el formato DD-MM-YYYY: ")
            esValido = validarFecha(fecha)
        ano = int(fecha[6:])
        mes = int(fecha[3:5])
        dia = int(fecha[0:2])
    fechadt = date(ano, mes, dia)
    horaReserva = verificarInputConNumeros(
        "Ingrese la hora de reserva:", "Ingrese una hora valida: ")
    nroReservaInt = verificarNumeroInput(
        "Ingrese el numero de reserva: ", "Numero de reserva invalido. Ingrese el numero de reserva: ")
    nombreClub = input(
        "Ingrese el nombre del club en el que desea realizar la reserva: ")
    datos1 = verificarExistenciaClub(nombreClub, clubes)
    while (datos1[0] == False):
        nombreClub = input(
            "Club inexistente. Ingrese el nombre del club en el que desea realizar la reserva: ")
        datos1 = verificarExistenciaClub(nombreClub, clubes)
    codigoInstalacionInt = verificarNumeroInput(
        "Ingrese el codigo de la instalacion que desea reservar: ", "Codigo invalido. Ingrese el codigo de la instalacion que desea reservar: ")
    datos2 = verificarExistenciaInstalacion(
        codigoInstalacionInt, datos1[1], clubes)
    while (datos2[0] == False):
        print("Instalacion inexistente. Ingrese el codigo de la instalacion que desea reservar: ")
        codigoInstalacionInt = verificarNumeroInput(
            "Ingrese el codigo de la instalacion que desea reservar: ", "Codigo invalido. Ingrese el codigo de la instalacion que desea reservar: ")
        datos2 = verificarExistenciaInstalacion(
            codigoInstalacionInt, datos1[1], clubes)
    reserva = Reserva(fechadt, horaReserva, nroReservaInt)
    clubes[datos1[1]].lista_instalaciones[datos2[1]].agregarReserva(reserva)


def consultarReservas():
    nombreClub = input(
        'Ingrese el nombre del club del que desea consultar las reservas de una instalacion: ')
    datos1 = verificarExistenciaClub(nombreClub, clubes)
    while (datos1[0] == False):
        nombreClub = input(
            'Nombre del club inexistente. Ingrese el nombre del club del que desea consultar las reservas de una instalacion: ')
        datos1 = verificarExistenciaClub(nombreClub, clubes)
    codigoInstalacionInt = verificarNumeroInput("Ingrese el codigo de la instalacion que desea consultar las reservas: ",
                                                "Codigo invalido. Ingrese el codigo de la instalacion que desea consultar las reservas: ")
    datos2 = verificarExistenciaInstalacion(
        codigoInstalacionInt, datos1[1], clubes)
    while (datos2[0] == False):
        print("Instalacion inexistente. Ingrese el codigo de la instalacion que desea consultar las reservas: ")
        codigoInstalacionInt = verificarNumeroInput("Ingrese el codigo de la instalacion que desea consultar las reservas: ",
                                                    "Codigo invalido. Ingrese el codigo de la instalacion que desea consultar las reservas: ")
        datos2 = verificarExistenciaInstalacion(
            codigoInstalacionInt, datos1[1], clubes)
    if len(clubes[datos1[1]].lista_instalaciones[datos2[1]].lista_reservas) == 0:
        print("No hay reservas registradas en esta instalacion")
        for r in range(len(clubes[datos1[1]].lista_instalaciones[datos2[1]].lista_reservas)):
            print(
                clubes[datos1[1]].lista_instalaciones[datos2[1]].lista_reservas[r])


def mostrarElDominioMenosUsadoEnCorreosDeInvitados():
    jsonData = jsonHandler('invitados.json')
    dominios = []
    for i in range(len(jsonData)):
        dominios.append(jsonData[i]["email"].split("@")[1])
    dominios = list(set(dominios))
    dominios.sort()
    dominios.sort(key=len)
    dominioMenosUsado = dominios[0]
    print("El dominio menos usado en los correos de los invitados es: " +
          dominioMenosUsado)
