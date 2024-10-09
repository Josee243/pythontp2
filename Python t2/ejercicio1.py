class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = 0

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


persona1 = Persona()
persona2 = Persona()


persona1.set_nombre("Ana")
persona1.set_edad(28)

persona2.set_nombre("Carlos")
persona2.set_edad(35)


persona1.print_persona()
persona2.print_persona()
