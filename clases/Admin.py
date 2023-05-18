from clases.Usuario import Usuario

class Admin(Usuario):
    def __init__(self, nombre, apellido, DNI, email, usuario, contrasenia):
        super().__init__(nombre, apellido, DNI, email)
        self.usuario = usuario
        self.contrasenia = contrasenia
