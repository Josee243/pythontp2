class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"

class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self):
        nombre = input("Introduce el nombre: ")
        telefono = input("Introduce el teléfono: ")
        email = input("Introduce el email: ")
        contacto = Contacto(nombre, telefono, email)
        self.contactos.append(contacto)
        print("Contacto añadido correctamente.")

    def listar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            for contacto in self.contactos:
                print(contacto)

    def buscar_contacto(self):
        nombre = input("Introduce el nombre del contacto a buscar: ")
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(contacto)
                return
        print("Contacto no encontrado.")

    def editar_contacto(self):
        nombre = input("Introduce el nombre del contacto a editar: ")
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print("Contacto encontrado. Ingresa los nuevos datos.")
                contacto.telefono = input("Nuevo teléfono: ")
                contacto.email = input("Nuevo email: ")
                print("Contacto actualizado.")
                return
        print("Contacto no encontrado.")

    def cerrar_agenda(self):
        print("Cerrando la agenda.")
        exit()

    def mostrar_menu(self):
        while True:
            print("\n--- Menú de la Agenda ---")
            print("1. Añadir contacto")
            print("2. Listar contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")

            opcion = input("Elige una opción: ")

            if opcion == '1':
                self.añadir_contacto()
            elif opcion == '2':
                self.listar_contactos()
            elif opcion == '3':
                self.buscar_contacto()
            elif opcion == '4':
                self.editar_contacto()
            elif opcion == '5':
                self.cerrar_agenda()
            else:
                print("Opción no válida. Inténtalo de nuevo.")


agenda = Agenda()
agenda.mostrar_menu()

