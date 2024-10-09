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

    def es_mayor_que(self, otra_persona):
        return self.edad > otra_persona.get_edad()

    @staticmethod
    def get_mayor(persona1, persona2):
        if persona1.get_edad() > persona2.get_edad():
            return persona1
        else:
            return persona2


persona1 = Persona("Ana", 28)
persona2 = Persona("Carlos", 35)

persona1.print_persona()
persona2.print_persona()


mayor_persona = Persona.get_mayor(persona1, persona2)
print(f"La persona de mayor edad es {mayor_persona.get_nombre()}, con {mayor_persona.get_edad()} años.")
