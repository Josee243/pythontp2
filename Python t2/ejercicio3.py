class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def print_persona(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    def es_mayor_de_edad(self):
        return self.edad >= 18

persona1 = Persona("Ana", 28)
persona2 = Persona("Carlos", 16)


persona1.print_persona()
print("Mayor de edad:", persona1.es_mayor_de_edad())

persona2.print_persona()
print("Mayor de edad:", persona2.es_mayor_de_edad())
