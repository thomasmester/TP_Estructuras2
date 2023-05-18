from clases.Usuario import Usuario

class Invitado(Usuario):
    def __init__(self, nombre, apellido, DNI, email, cantVecesIngresa):
        super().__init__(nombre, apellido, DNI, email)
        self.cantVecesIngresa = cantVecesIngresa