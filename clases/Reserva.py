class Reserva:
    def __init__(self, fechaReserva, horaReserva, nroReserva):
        self.nroReserva = nroReserva
        self.fechaReserva = fechaReserva
        self.horaReserva = horaReserva
    
    def __str__(self):
        return f'Información de la reserva:\n Número de reserva: {self.nroReserva}, Fecha: {self.fechaReserva}, Hora: {self.horaReserva}'