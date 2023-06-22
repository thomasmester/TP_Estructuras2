import json
from clases.Admin import Admin
import verificaciones as ver
import auxiliares as aux
import opcionesMenu as op
from clases.Invitado import Invitado
from opcionesIngreso import *


def ingreso():
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
              "19: Cambiar contraseña de usuario", '\n',
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
                op.mostrarElDominioMenosUsadoEnCorreosDeInvitados()

ingreso()