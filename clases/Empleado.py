from clases.Persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, apellido, sexo, edad, DNI, legajo, cargo, salario):
        super().__init__(nombre, apellido, sexo, edad, DNI)
        self.legajo = legajo
        self.cargo = cargo
        self.salario = salario
