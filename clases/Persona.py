class Persona:
    def __init__(self, nombre, apellido, sexo, edad, DNI):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
        self.DNI = DNI

    def presentacion(self):
        print("Me llamo {} {} y tengo {} años".format(
            self.nombre, self.apellido, self.edad))