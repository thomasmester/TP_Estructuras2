from clases.Socio import *

class ColaSocios():
    def _init_(self):
        self.cola = []
    def esVacia(self):
        return len(self.cola) == 0
    def encolar(self,socio:Socio):
        self.cola.append(socio)
    def desencolar(self):
        if self.esVacia():
            print("Cola vacía")
            return
        else:
            return self.cola.pop(0)
    def _str_(self):
        cadena  = ''
        if self.esVacia():
            return "Cola vacía"
        else:
            for socio in self.cola:
                cadena  += socio.dni + " " + socio.nombre + " " + socio.aellido + "|"
            return cadena