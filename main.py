import json
from clases.Admin import Admin
import verificaciones as ver
import auxiliares as aux
import opcionesMenu as op
from clases.Invitado import Invitado


def case3():
    nombre = ver.verificarInputSinNumeros(
        "Ingrese su nombre: ", "Ingreso invalido. Ingrese su nombre: ")
    apellido = ver.verificarInputSinNumeros(
        "Ingrese su apellido: ", "Ingreso invalido. Ingrese su apellido: ")
    jsonData = aux.jsonHandler('invitados.json')
    coincide = True
    while (coincide == True):
        coincide = False
        dni = ver.verificarNumeroInput(
            "Ingrese su DNI: ", "Ingreso invalido: ")
        email = ver.verificarInputMail()
        for i in range(len(jsonData)):
            if jsonData[i]['DNI'] == str(dni) and jsonData[i]['email'] != email:
                coincide = True
            if jsonData[i]['DNI'] != str(dni) and jsonData[i]['email'] == email:
                coincide = True
        if (coincide == True):
                print('Un usuario con el mismo dni no se puede registrar con diferentes mails y no puede registrarse más de un usuario con un mismo mail.')
        encontro = False
        for i in range(len(jsonData)):
            if int(jsonData[i]['DNI']) == dni:
                jsonData[i]['cantVecesIngresa'] = int(jsonData[i]['cantVecesIngresa']) + 1
                encontro = True
        if not encontro:
            datosInvitado = Invitado(nombre, apellido, dni, email, 1)
            jsonData.append(datosInvitado.__dict__)
        
    with open('invitados.json', 'w') as g:
        js = json.dumps(jsonData)
        g.write(js)


def ingreso(archivo):
    print("Bienvenido. Seleccione alguna de las siguientes opciones", '\n',
          "1. Registrarse", '\n',
          "2. Iniciar sesión", '\n',
          "3. Ingresar como invitado")
    opcion = ver.verificarNumeroInput(
        "Ingrese la opción: ", "Opcion invalida. Ingrese la opcion que desea elegir: ")
    while opcion not in range(1, 4):
        print("Opcion invalida")
        opcion = ver.verificarNumeroInput(
            "Ingrese la opción: ", "Opcion invalida. Ingrese la opcion que desea elegir: ")

    match opcion:
        case 1:
            usuario = input("Ingrese usuario: ")
            jsonData = aux.jsonHandler('admins.json')
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
            nombre = ver.verificarInputSinNumeros(
                "Ingrese su nombre: ", "Ingreso invalido. Ingrese su nombre: ")
            apellido = ver.verificarInputSinNumeros(
                "Ingrese su apellido: ", "Ingreso invalido. Ingrese su apellido: ")
            dni = ver.verificarNumeroInput(
                "Ingrese su DNI: ", "Ingreso invalido: ")
            email = ver.verificarInputMail()
            usu = Admin(nombre, apellido, dni, email,
                        usuario, contrasenia).__dict__
            jsonData.append(usu)
            with open("admins.json", 'w') as file:
                js = json.dumps(jsonData)
                file.write(js)
            menuPrincipal()
        case 2:
            usuario = input("Ingrese usuario: ")
            jsonData = aux.jsonHandler('admins.json')
            sesionIniciada = False
            while (sesionIniciada == False):
                contrasenia = input("Ingrese contraseña: ")
                for i in range(len(jsonData)):
                    if jsonData[i]["usuario"] == usuario and jsonData[i]["contrasenia"] == contrasenia:
                        sesionIniciada = True
                if sesionIniciada == False:
                    print(
                        "Usuario o contraseña incorrectos. Ingrese los datos nuevamente:")
                    usuario = input("Ingrese usuario: ")
        case 3:
            case3()
    menuPrincipal()


def menuPrincipal():
    op.inicializar()
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
        opcionElegida = ver.verificarOpcionMenu("Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finalizar: ",
                                                "Opcion invalida. Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finalizar: ")
        while opcionElegida not in range(24):
            print("Opcion invalida")
            opcionElegida = ver.verificarOpcionMenu("Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finalizar: ",
                                                    "Opcion invalida. Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finalizar: ")
        match opcionElegida:
            case 0:
                termina = op.finalizarPrograma()
            case 1:
                op.registrarClub()
            case 2:
                op.consultarInfoClub()
            case 3:
                op.registrarSocio()
            case 4:
                op.eliminarSocio()
            case 5:
                op.consultarSocios()
            case 6:
                op.registrarInstalacion()
            case 7:
                op.eliminarInstalacion()
            case 8:
                op.consultarInstalaciones()
            case 9:
                op.registrarEmpleado()
            case 10:
                op.consultarEmpleados()
            case 11:
                op.eliminarEmpleado()
            case 12:
                op.generarPago()
            case 13:
                op.eliminarPago()
            case 14:
                op.consultarPagos()
            case 15:
                op.crearReserva()
            case 16:
                op.consultarReservas()
            case 17:
                op.graficoEdades()
            case 18:
                op.mostrarInvitados()
            case 19:
                op.cambiarContrasenaUsuario()
            case 20:
                op.actualizarDatosInvitado()
            case 21:
                op.visualizarInvitadosMenosAcceso()
            case 22:
                op.eliminarInvitado()
            case 23:
                op.dominioMenosVeces()


def actualizarDatosInvitado():
    with open('invitados.txt', 'r', encoding='utf-8') as f:
        datos = f.read()
        datos = datos.split('\n')
        datos = aux.splitearLista(datos, ',')
        encontrado = False
        dni = ver.verificarNumeroInput('Ingresar DNI del usuario a actualizar los datos: ',
                                       'Usuario invalido. Ingrese DNI del usuario para actualizar sus datos: ')
        correo = ver.verificarInputConNumeros("Ingrese el correo del invitado al que le quiere actualizar los datos: ",
                                              "Correo invalido. Ingrese el correo del invitado al que le quiere actualizar los datos: ")
        for i in range(len(datos)):
            if datos[i] != [''] and int(datos[i][2]) == dni and datos[i][3] == correo:
                encontrado = True
                indice = i
        if not encontrado:
            print("El invitado no esta registrado")
            case3()
        else:
            print("Actualizacion de datos")
            nombre = ver.verificarInputSinNumeros(
                'Ingresar su nombre para actualizarlo: ', 'Nombre invalido. Ingrese su nombre para actualizarlo: ')
            apellido = ver.verificarInputSinNumeros(
                'Ingresar su apellido para actualizarlo: ', 'Apellido invalido. Ingrese su apellido para actualizarlo: ')
            correo = ver.verificarInputConNumeros(
                "Ingrese su correo para actualizarlo: ", "Correo invalido. Ingrese su correo para actualizarlo: ")
            datos[indice][0] = nombre
            datos[indice][1] = apellido
            datos[indice][3] = correo
            aEscribir = ''
            for j in range(len(datos)):
                if datos[j] != ['']:
                    aEscribir += datos[j][0] + ',' + datos[j][1] + ',' + \
                        datos[j][2] + ',' + datos[j][3] + \
                        ',' + datos[j][4] + '\n'

            with open('invitados.txt', 'w', encoding='utf-8') as g:
                g.write(aEscribir)
            print('Invitado actualizado exitosamente')


ingreso("admins.json")
