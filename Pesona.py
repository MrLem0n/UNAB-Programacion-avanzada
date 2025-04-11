class Persona():
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.edad} años, {self.genero}"

