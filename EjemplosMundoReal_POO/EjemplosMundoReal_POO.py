# Clase que representa una habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.esta_disponible = True

    def reservar(self):
        if self.esta_disponible:
            self.esta_disponible = False
            print("Habitación", self.numero, "reservada.")
        else:
            print("Ya está ocupada.")

    def liberar(self):
        self.esta_disponible = True
        print("Habitación", self.numero, "libre.")

    def mostrar(self):
        estado = "Libre" if self.esta_disponible else "Ocupada"
        print(f"Hab {self.numero} - {self.tipo} - ${self.precio} - {estado}")

# Clase para el cliente
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

# Clase que maneja el hotel
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = {}  # Se guarda qué cliente tiene qué habitación

    def agregar_habitacion(self, hab):
        self.habitaciones.append(hab)

    def ver_habitaciones(self):
        print("\nHabitaciones del hotel", self.nombre)
        for h in self.habitaciones:
            h.mostrar()

    def reservar_habitacion(self, num_hab, cliente):
        for h in self.habitaciones:
            if h.numero == num_hab:
                if h.esta_disponible:
                    h.reservar()
                    self.reservas[num_hab] = cliente
                else:
                    print("No se puede reservar, ya está ocupada.")
                return
        print("No se encontró la habitación.")

    def cancelar_reserva(self, num_hab):
        for h in self.habitaciones:
            if h.numero == num_hab and not h.esta_disponible:
                h.liberar()
                del self.reservas[num_hab]
                return
        print("No se puede cancelar, no está reservada o no existe.")

# Parte de prueba

hotel1 = Hotel("Hotel Estudiantil")

# Se crean habitaciones
hab1 = Habitacion(1, "Simple", 25)
hab2 = Habitacion(2, "Doble", 40)
hab3 = Habitacion(3, "Suite", 70)

# Se agregan al hotel
hotel1.agregar_habitacion(hab1)
hotel1.agregar_habitacion(hab2)
hotel1.agregar_habitacion(hab3)

# Ver estado inicial
hotel1.ver_habitaciones()

# Crear cliente
cli1 = Cliente("Juan López", "1234567890")

# Reservar habitación
hotel1.reservar_habitacion(2, cli1)

# Ver después de reservar
hotel1.ver_habitaciones()

# Cancelar reserva
hotel1.cancelar_reserva(2)

# Ver al final
hotel1.ver_habitaciones()
