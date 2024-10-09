class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        print(f"Nombre del alumno: {self.nombre}")
        print(f"Nota del alumno: {self.nota}")

    def resultado(self):
        if self.nota >= 5:
            print(f"{self.nombre} ha aprobado con una nota de {self.nota}.")
        else:
            print(f"{self.nombre} ha suspendido con una nota de {self.nota}.")


alumno1 = Alumno("Juan", 7)
alumno2 = Alumno("Lucía", 4)


alumno1.imprimir_datos()
alumno1.resultado()

alumno2.imprimir_datos()
alumno2.resultado()
