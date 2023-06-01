from clases.Usuario import Usuario

class Invitado(Usuario):
    def __init__(self, nombre, apellido, DNI, email, cantVecesIngresa):
        super().__init__(nombre, apellido, DNI, email)
        self.cantVecesIngresa = cantVecesIngresa
    
    def __str__(self):
        return f'Datos del invitado:\n Nombre:{self.nombre}, Apellido: {self.apellido}, DNI: {self.DNI}, email: {self.email}, Cantidad de veces que ingresó: {self.cantVecesIngresa}'
    
    