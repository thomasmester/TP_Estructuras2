from clases.Persona import Persona

class Socio(Persona):
    def __init__(self, nombre, apellido, sexo, edad, DNI, nroSocio, correoElectronico):
        super().__init__(nombre, apellido, sexo, edad, DNI)
        self.nroSocio = nroSocio
        self.correoElectronico = correoElectronico
    
    def __str__(self):
        return f'Datos del socio: Nombre:{self.nombre}, Apellido: {self.apellido}, Sexo:{self.sexo}, Edad: {self.edad}, DNI: {self.DNI}, nroSocio: {self.nroSocio}, Correo elecrónico: {self.correoElectronico}'
    
