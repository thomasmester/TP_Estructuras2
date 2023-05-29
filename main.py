import json
from clases.Admin import Admin
from verificaciones import *
from auxiliares import *


clubes = []


def case3():
    nombre = verificarInputSinNumeros(
        "Ingrese su nombre: ", "Ingreso invalido. Ingrese su nombre: ")
    apellido = verificarInputSinNumeros(
        "Ingrese su apellido: ", "Ingreso invalido. Ingrese su apellido: ")
    stringCompleto = ''
    with open('invitados.txt', 'r') as f:
        data = f.read()
        data = data.split('\n')
        data = splitearLista(data, ',')
        coincide = True
        while (coincide == True):
            coincide = False
            dni = verificarNumeroInput(
                "Ingrese su DNI: ", "Ingreso invalido: ")
            email = verificarInputMail()
            for i in range(len(data)):
                if data[i] != ['']:
                    if data[i][2] == str(dni) and data[i][3] != email:
                        coincide = True
                    if data[i][2] != str(dni) and data[i][3] == email:
                        coincide = True
            if (coincide == True):
                print('Un usuario con el mismo dni no se puede registrar con diferentes mails y no puede registrarse más de un usuario con un mismo mail.')
        encontro = False
        for i in range(len(data)):
            if data[i] != [''] and int(data[i][2]) == dni:
                data[i][4] = int(data[i][4]) + 1
                encontro = True
        if not encontro:
            datosInvitado = [nombre, apellido, dni, email, 1]
            data.append(datosInvitado)
    for i in range(len(data)):
        if data[i] != ['']:
            stringCompleto += data[i][0] + ',' + data[i][1] + ',' + \
                str(data[i][2]) + ',' + data[i][3] + \
                ',' + str(data[i][4]) + '\n'
    with open('invitados.txt', 'w') as g:
        g.write(stringCompleto)


def ingreso(archivo):
    print("Bienvenido. Seleccione alguna de las siguientes opciones", '\n',
          "1. Registrarse", '\n',
          "2. Iniciar sesión", '\n',
          "3. Ingresar como invitado")
    opcion = verificarNumeroInput(
        "Ingrese la opción: ", "Opcion invalida. Ingrese la opcion que desea elegir: ")
    while opcion not in range(1, 4):
        print("Opcion invalida")
        opcion = verificarNumeroInput(
            "Ingrese la opción: ", "Opcion invalida. Ingrese la opcion que desea elegir: ")

    match opcion:
        case 1:
            usuario = input("Ingrese usuario: ")
            with open('admins.json', 'r') as f:
                try:
                    jsonData = json.load(f)
                    f.close()
                except json.decoder.JSONDecodeError:
                    jsonData = []
            esta = True
            while esta == True:
                encontro = False
                for i in range(len(jsonData)):
                    if jsonData[i]["usuario"] == usuario:
                        encontro = True
                if encontro == True:
                    usuario = input(
                        "Este nombre de usuario ya existe, utilice otro: ")
                else:
                    esta = False
            contrasenia = input("Ingrese contraseña: ")
            nombre = verificarInputSinNumeros(
                "Ingrese su nombre: ", "Ingreso invalido. Ingrese su nombre: ")
            apellido = verificarInputSinNumeros(
                "Ingrese su apellido: ", "Ingreso invalido. Ingrese su apellido: ")
            dni = verificarNumeroInput(
                "Ingrese su DNI: ", "Ingreso invalido: ")
            email = verificarInputMail()
            usu = Admin(nombre, apellido, dni, email,
                        usuario, contrasenia).__dict__
            jsonData.append(usu)
            with open("admins.json", 'w') as file:
                js = json.dumps(jsonData)
                file.write(js)
            menuPrincipal()
        case 2:
            usuario = input("Ingrese usuario: ")
            txt = open(archivo, "r", encoding="utf-8")
            matrizUsuCon = []
            for linea in txt:
                uc = linea[:-1].split(",")
                matrizUsuCon.append(uc)
            txt.close()
            sesionIniciada = False
            while (sesionIniciada == False):
                contrasenia = input("Ingrese contraseña: ")
                for i in range(len(matrizUsuCon)):
                    if matrizUsuCon[i][0] == usuario and matrizUsuCon[i][1] == contrasenia:
                        sesionIniciada = True
                if sesionIniciada == False:
                    print(
                        "Usuario o contraseña incorrectos. Ingrese los datos nuevamente:")
                    usuario = input("Ingrese usuario: ")
        case 3:
            case3()
    menuPrincipal()


def menuPrincipal():
    inicializarListaClubes()
    for c in clubes:
        c.inicializarClub()
    termina = False
    while (not termina):
        print("Menu principal", '\n',
              "1: Registrar club", '\n',
              "2: Consultar informacion general de un club", '\n',
              "3: Registrar socio en un club", '\n',
              "4: Eliminar socio en un club", '\n',
              "5: Consultar socios de un club", '\n',
              "6: Registrar instalacion en un club", '\n',
              "7: Eliminar instalacion en un club", '\n',
              "8: Consultar instalaciones de un club", '\n',
              "9: Registrar empleado en un club", '\n',
              "10: Consultar empleados de un club", '\n',
              "11: Eliminar un empleado de un club", '\n',
              "12: Generar pago en un club", '\n',
              "13: Eliminar pago en un club", '\n',
              "14: Consultar pagos de un club", '\n',
              "15: Crear reserva en una instalacion", '\n',
              "16: Consultar reservas en una instalacion de un club", '\n',
              "17: Ver un grafico de los socios divididos por rango etario de un club", '\n',
              "18: Mostrar usuarios invitados", '\n',
              "19: Cambiar contrasena de usuario", '\n',
              "20: Actualizar datos de un usuario invitado", '\n',
              "21: Visualizar en una gráfica tipo barras los dni de los 5 usuarios invitados que menos acceso hayan tenido a la plataforma", '\n',
              "22: Eliminar un usuario invitado por DNI o Mail", '\n',
              "23: Mostrar el dominio que menos veces fue ingresado como invitado"
              )
        opcionElegida = verificarOpcionMenu("Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finalizar: ",
                                            "Opcion invalida. Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finalizar: ")
        while opcionElegida not in range(24):
            print("Opcion invalida")
            opcionElegida = verificarOpcionMenu("Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finalizar: ",
                                                "Opcion invalida. Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finalizar: ")
        match opcionElegida:
            case 0:
                termina = finalizarPrograma()
            case 1:
                registrarClub()
            case 2:
                consultarInfoClub()
            case 3:
                registrarSocio()
            case 4:
                eliminarSocio()
            case 5:
                consultarSocios()
            case 6:
                registrarInstalacion()
            case 7:
                eliminarInstalacion()
            case 8:
                consultarInstalaciones()
            case 9:
                registrarEmpleado()
            case 10:
                consultarEmpleados()
            case 11:
                eliminarEmpleado()
            case 12:
                generarPago()
            case 13:
                eliminarPago()
            case 14:
                consultarPagos()
            case 15:
                crearReserva()
            case 16:
                consultarReservas()
            case 17:
                graficoEdades()
            case 18:
                mostrarInvitados()
            case 19:
                cambiarContrasenaUsuario()
            case 20:
                actualizarDatosInvitado()
            case 21:
                visualizarInvitadosMenosAcceso()
            case 22:
                eliminarInvitado()
            case 23:
                dominioMenosVeces()


ingreso("archivo.txt")