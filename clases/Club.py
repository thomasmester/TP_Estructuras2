from clases.Socio import Socio
from clases.Empleado import Empleado
from clases.Instalacion import Instalacion
from clases.Pago import Pago
from clases.Reserva import Reserva
import datetime
from array import array

def splitearLista(lista, var):
    # recibe una lista de strings a splitear
    for i in range(len(lista)):
        lista[i] = lista[i].split(var)
    return lista


class Club:
    lista_nombres = []

    def __init__(self, nombre, anioFundacion, direccion):
        if nombre in self.lista_nombres:
            raise ValueError("Nombre repetido")
        self.lista_nombres.append(nombre)
        self.nombre = nombre
        self.anioFundacion = anioFundacion
        self.direccion = direccion
        self.lista_socios = []
        self.lista_instalaciones = []
        self.lista_pagos = []
        self.lista_empleados = []
        self.edades = array("H", [])
        self.clasificacion = array("H", [])
    
    def agregaEdad(self, edad):
        self.edades.append(edad)

    def clasifica(self):
        menores = 0
        adultos = 0
        mayores = 0
        for edad in self.edades:
            if 1 <= int(edad) < 18:
                menores += 1
            if 18 <= int(edad) < 60:
                adultos += 1
            if int(edad) >= 60:
                mayores += 1

        self.clasificacion.extend([menores, adultos, mayores])
        return self.clasificacion

    def __str__(self):
        return f"El club {self.nombre} se fundo en {self.anioFundacion} y queda en {self.direccion}"

    def agregarSocio(self, socio):
        esta = False
        for i in range(len(self.lista_socios)):
            if socio.nroSocio == self.lista_socios[i].nroSocio:
                esta = True
        if esta == False:
            self.lista_socios.append(socio)
            print("El socio {} {} ha sido agregado con éxito al club.".format(
                socio.nombre, socio.apellido))
        else:
            print("Ya existe un socio con el numero de socio {}".format(socio.nroSocio))

    def eliminarSocio(self, nroSocio):
        esta = False
        for i in range(len(self.lista_socios)):
            if nroSocio == self.lista_socios[i].nroSocio:
                esta = True
                indiceAux = i
        if esta == True:
            self.lista_socios.pop(indiceAux)
            print("El socio cuyo numero de socio es {} ha sido eliminado con éxito.".format(
                nroSocio))
        else:
            print("No hay ningun socio en el club cuyo numero de socio sea el {}".format(
                nroSocio))

    def agregarPago(self, pago):
        existeSocio = False
        pagoYaExiste = False
        for s in self.lista_socios:
            if pago.nroSocio == s.nroSocio:
                existeSocio = True
        for i in range(len(self.lista_pagos)):
            if pago.codigoPago == self.lista_pagos[i].codigoPago:
                pagoYaExiste = True
        if not pagoYaExiste and existeSocio:
            self.lista_pagos.append(pago)
            print("El pago {} ha sido agregado con éxito al club.".format(
                pago.codigoPago))
        else:
            print("Ya existe un pago con el codigo de pago {} o no hay un socio con el número {} ".format(
                pago.codigoPago, pago.nroSocio))

    def eliminarPago(self, codigoPago):
        esta = False
        for i in range(len(self.lista_pagos)):
            if codigoPago == self.lista_pagos[i].codigoPago:
                esta = True
                indiceAux = i
        if esta == True:
            self.lista_pagos.pop(indiceAux)
            print("El pago cuyo codigo es {} ha sido eliminado con éxito.".format(
                codigoPago))
        else:
            print("No hay registrado un pago con el codigo {}".format(
                codigoPago))

    def agregarInstalacion(self, instalacion):
        esta = False
        for i in range(len(self.lista_instalaciones)):
            if instalacion.codigoInstalacion == self.lista_instalaciones[i].codigoInstalacion:
                esta = True
        if esta == False:
            self.lista_instalaciones.append(instalacion)
            print("La instalacion {} cuyo codigo es {} ha sido agregado con éxito al club.".format(
                instalacion.nombre, instalacion.codigoInstalacion))
        else:
            print("Ya existe una instalacion con el codigo {}".format(
                instalacion.codigoInstalacion))

    def eliminarInstalacion(self, codigoInstalacion):
        esta = False
        for i in range(len(self.lista_instalaciones)):
            if codigoInstalacion == self.lista_instalaciones[i].codigoInstalacion:
                esta = True
                indiceAux = i
        if esta == True:
            self.lista_instalaciones.pop(indiceAux)
            print("La instalacion cuyo codigo es {} ha sido eliminada con éxito.".format(
                codigoInstalacion))
        else:
            print("No hay ninguna instalacion en el club cuyo codigo sea el {}".format(
                codigoInstalacion))

    def agregarEmpleado(self, empleado):
        esta = False
        for i in range(len(self.lista_empleados)):
            if empleado.legajo == self.lista_empleados[i].legajo:
                esta = True
        if esta == False:
            self.lista_empleados.append(empleado)
            print("El empleado {} {} ha sido agregado con éxito al club.".format(
                empleado.nombre, empleado.apellido))
        else:
            print("Ya existe un empleado con el legajo {}".format(empleado.legajo))

    def eliminarEmpleado(self, legajo):
        esta = False
        for i in range(len(self.lista_empleados)):
            if legajo == self.lista_empleados[i].legajo:
                esta = True
                indiceAux = i
        if esta == True:
            self.lista_empleados.pop(indiceAux)
            print("El empleado cuyo legajo es {} ha sido eliminado con éxito.".format(
                legajo))
        else:
            print("No hay ningun empleado en el club cuyo legajo sea el {}".format(
                legajo))