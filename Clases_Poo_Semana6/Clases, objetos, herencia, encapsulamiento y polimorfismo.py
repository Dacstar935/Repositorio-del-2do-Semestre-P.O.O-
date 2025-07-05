class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre      # Atributo protegido (encapsulación)
        self._edad = edad          # Atributo protegido (encapsulación)

    def hacer_sonido(self):
        # se sobreescribirá en las clases hijas (polimorfismo)
        return "Hace un sonido"

    def mostrar_info(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}"


# Clase derivada (herencia)
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.__raza = raza               # Atributo privado (encapsulación)

    def hacer_sonido(self):  # Sobrescribe el método de la clase base (polimorfismo)
        return "Guau guau"

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Raza: {self.__raza}"


# Otra clase derivada
class Gato(Animal):
    def hacer_sonido(self):  # Polimorfismo: mismo método, comportamiento distinto
        return "Miau"

# Crear instancias
mi_perro = Perro("Jack", 4, "French Poodle")
mi_gato = Gato("Sima", 1)

# Uso de métodos
print(mi_perro.mostrar_info())      # Herencia + encapsulación + métodp sobrescrito
print("Sonido del perro:", mi_perro.hacer_sonido())  # Polimorfismo

print(mi_gato.mostrar_info())       # Herencia
print("Sonido del gato:", mi_gato.hacer_sonido())    # Polimorfismo
