class Vehiculo:
    def encender(self):
        print("El vehículo está encendido.")

    def conducir(self):
        print("Estamos conduciendo el vehículo.")

# Creamos otra clase más específica
class Auto(Vehiculo):
    def encender(self):
        print("El auto se encendió con llave.")

    def conducir(self):
        print("Estamos manejando el auto por la ciudad.")

# Usamos la clase Auto
mi_auto = Auto()
mi_auto.encender()
mi_auto.conducir()

# Uso
mi_auto = Auto()
mi_auto.encender()
mi_auto.conducir()
