# Clase Animal con constructor
class Animal:
    def __init__(self, color, raza):
        # Se guardan los atributos del animal
        self.color = color
        self.raza = raza

# Clase Perro que hereda de Animal
class Perro(Animal):
    def __init__(self, color, raza, nombre="Jack"):
        # Llama al constructor de la clase padre
        super().__init__(color, raza)
        self.nombre = nombre
        # Simulamos que se abre un archivo (recurso) para el perro
        self.archivo = open("perro.txt", "w")
        self.archivo.write("Nombre: " + self.nombre + "\n")
        self.archivo.write("Raza: " + self.raza + "\n")
        self.archivo.write("Color: " + self.color + "\n")
        print("Perro creado correctamente.")

    def ladrar(self):
        print(self.nombre + " dice guau")

    # Destructor que cierra el archivo cuando se elimina el objeto
    def __del__(self):
        self.archivo.close()
        print("Archivo cerrado. Perro eliminado.")

# Crear un objeto de tipo Perro
mi_perro = Perro("Blanco", "Poodle")

# Mostrar la información
print("Color del perro:", mi_perro.color)
print("Raza del perro:", mi_perro.raza)
print("Nombre del perro:", mi_perro.nombre)

# Llamar a ladrar
mi_perro.ladrar()

# Eliminar el objeto
del mi_perro

