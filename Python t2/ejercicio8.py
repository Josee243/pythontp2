class Calculadora:
    def __init__(self):
        self.valor1 = int(input("Introduce el primer valor: "))
        self.valor2 = int(input("Introduce el segundo valor: "))

    def sumar(self):
        return self.valor1 + self.valor2

    def restar(self):
        return self.valor1 - self.valor2

    def multiplicar(self):
        return self.valor1 * self.valor2

    def dividir(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: División por cero no permitida."


calc = Calculadora()


print(f"Suma: {calc.sumar()}")
print(f"Resta: {calc.restar()}")
print(f"Multiplicación: {calc.multiplicar()}")
print(f"División: {calc.dividir()}")
