class Instalacion:
    def __init__(self, nombre, descripcion, horaApertura, horaCierre, codigoInstalacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.horaApertura = horaApertura
        self.horaCierre = horaCierre
        self.codigoInstalacion = codigoInstalacion
        self.lista_reservas = []

    def agregarReserva(self, reserva):
        disponible = True
        for i in range(len(self.lista_reservas)):
            if reserva.fechaReserva == self.lista_reservas[i].fechaReserva and reserva.horaReserva == self.lista_reservas[i].horaReserva:
                disponible = False
        if disponible:
            self.lista_reservas.append(reserva)
            print('Su reserva para el día {} a las {} a sido agendada con éxito.'.format(
                reserva.fechaReserva, reserva.horaReserva))
        else:
            print(
                'El horario de las {} en el día {} no está disponible, por favor seleccione otro.'.format(reserva.horaReserva, reserva.fechaReserva))

    def eliminarReserva(self, nroReserva):
        horaElim = ''
        fechaElim = ''
        eliminada = False
        for j in range(len(self.lista_reservas)):
            if nroReserva == self.lista_reservas[j].nroReserva:

                horaElim = self.lista_reservas[j].horaReserva
                fechaElim = self.lista_reservas[j].fechaReserva
                self.lista_reservas.pop(j)
                eliminada = True
            if not eliminada:
                print('No existe una reserva con el número {}'.format(nroReserva))
            else:
                print('La reserva de las {} el día {} fue eliminada con éxito.'.format(
                    horaElim, fechaElim))