class Pago:
    def __init__(self, monto, fecha, nroSocio, codigoPago):
        self.monto = monto
        self.fecha = fecha
        self.nroSocio = nroSocio
        self.codigoPago = codigoPago
    
    def __str__(self):
        return f'Monto del pago: ${self.monto}, Fecha del pago: {self.fecha}, Numero del socio que abona: {self.nroSocio}, Codigo del pago: {self.codigoPago}'
    
    