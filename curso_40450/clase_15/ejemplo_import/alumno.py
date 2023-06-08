

class Alumno:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


    def presentarse(self):
        print(f"Soy el alumno/a {self.nombre} {self.apellido}")