class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0

    def depositar(self, monto):
        if monto > 0:
            self.cantidad += monto
            print(f"{self.nombre} ha depositado {monto} euros.")
        else:
            print("El monto debe ser mayor a 0.")

    def extraer(self, monto):
        if monto > 0 and monto <= self.cantidad:
            self.cantidad -= monto
            print(f"{self.nombre} ha extraído {monto} euros.")
        elif monto > self.cantidad:
            print(f"{self.nombre} no tiene suficiente saldo para extraer {monto} euros.")
        else:
            print("El monto debe ser mayor a 0.")

    def mostrar_total(self):
        print(f"{self.nombre} tiene un saldo de {self.cantidad} euros.")

class Banco:
    def __init__(self):
        # Inicializar tres clientes
        self.cliente1 = Cliente("Ana")
        self.cliente2 = Cliente("Carlos")
        self.cliente3 = Cliente("Lucía")

    def operar(self):
        # Ejemplo de operaciones para los clientes
        self.cliente1.depositar(1000)
        self.cliente1.extraer(300)

        self.cliente2.depositar(2000)
        self.cliente2.extraer(500)

        self.cliente3.depositar(1500)
        self.cliente3.extraer(700)

    def deposito_total(self):
        total_depositos = (self.cliente1.cantidad + 
                           self.cliente2.cantidad + 
                           self.cliente3.cantidad)
        print(f"El total de dinero en el banco es: {total_depositos} euros.")


banco = Banco()


banco.operar()


banco.cliente1.mostrar_total()
banco.cliente2.mostrar_total()
banco.cliente3.mostrar_total()


banco.deposito_total()
