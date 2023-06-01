from clases.Persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, apellido, sexo, edad, DNI, legajo, cargo, salario):
        super().__init__(nombre, apellido, sexo, edad, DNI)
        self.legajo = legajo
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f'Datos del empleado: Nombre:{self.nombre}, Apellido: {self.apellido}, Sexo:{self.sexo}, Edad: {self.edad}, DNI: {self.DNI}, Legajo: {self.legajo}, Cargo: {self.cargo}'