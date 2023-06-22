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

    def guardarClub(self):
        socios_text = ""
        inst_text = ""
        pagos_text = ""
        empleados_text = ""
        for socio in self.lista_socios:
            socios_text += (socio.nombre + "," + socio.apellido + "," + socio.sexo + "," + str(socio.edad) + "," +
                            str(socio.DNI) + "," + str(socio.nroSocio) + "," + socio.correoElectronico + '|')
        for inst in self.lista_instalaciones:
            inst_text += (inst.nombre + "," + inst.descripcion + "," + str(inst.horaApertura) + "," + str(inst.horaCierre) + "," +
                          str(inst.codigoInstalacion))
            for res in inst.lista_reservas:
                inst_text += ('-' + str(res.fechaReserva.year) + ',' + str(res.fechaReserva.month) + ',' + str(
                    res.fechaReserva.day) + ',' + str(res.horaReserva) + ',' + str(res.nroReserva))
            inst_text += '|'
        for pago in self.lista_pagos:
            pagos_text += (str(pago.monto) + "," + str(pago.fecha.year) + ',' + str(pago.fecha.month) + ',' + str(pago.fecha.day) + ',' + "," +
                           str(pago.nroSocio) + "," + str(pago.codigoPago) + '|')
        for empleado in self.lista_empleados:
            empleados_text += (empleado.nombre + ',' + empleado.apellido + ',' + empleado.sexo + ',' + str(empleado.edad) +
                               ',' + str(empleado.DNI) + ',' + str(empleado.legajo) + ',' + empleado.cargo + ',' + str(empleado.salario) + '|')

        total_text = (socios_text[:-1] + '~' +
                      inst_text[:-1] + '~' + pagos_text[:-1] + '~' + empleados_text[:-1])
        with open("{}.txt".format(self.nombre), "w") as f:
            f.write(total_text)

    def inicializarClub(self):
        with open("{}.txt".format(self.nombre), "r") as f:
            data = f.read()
            texto = data.split('~')
            sociosRaw = texto[0]
            instRaw = texto[1]
            pagosRaw = texto[2]
            empleadosRaw = texto[3]

            socios = sociosRaw.split('|')
            inst = instRaw.split('|')
            pagos = pagosRaw.split('|')
            empleados = empleadosRaw.split('|')

            socios = splitearLista(socios, ',')
            i = splitearLista(inst, '-')
            inst = []
            for j in range(len(i)):
                inst.append(splitearLista(i[j], ','))
            pagos = splitearLista(pagos, ',')
            empleados = splitearLista(empleados, ',')

            if socios[0] != ['']:
                for s in socios:
                    self.lista_socios.append(
                        Socio(s[0], s[1], s[2], int(s[3]), int(s[4]), int(s[5]), s[6]))
            if inst[0] != [['']]:
                for i in range(len(inst)):
                    self.lista_instalaciones.append(Instalacion(
                        inst[i][0][0], inst[i][0][1], inst[i][0][2], inst[i][0][3], int(inst[i][0][4])))
                    if len(inst[i]) > 1:
                        for r in range(len(inst[i])-1):
                            rdate = datetime.date(
                                int(inst[i][r+1][0]), int(inst[i][r+1][1]), int(inst[i][r+1][2]))
                            self.lista_instalaciones[i].lista_reservas.append(
                                Reserva(rdate, inst[i][r+1][1], inst[i][r+1][2]))
            if pagos[0] != ['']:
                for p in pagos:
                    d = datetime.date(int(p[1]), int(p[2]), int(p[3]))
                    self.lista_pagos.append(Pago(p[0], d, p[4], p[5]))
            if empleados[0] != ['']:
                for e in empleados:
                    self.lista_empleados.append(
                        Empleado(e[0], e[1], e[2], int(e[3]), int(e[4]), int(e[5]), e[6], e[7]))

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