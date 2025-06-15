class Perro:
    def hacer_sonido(self):
        print("El perro dice: ¡Guau!")

class Gato:
    def hacer_sonido(self):
        print("El gato dice: Miau")

# Creamos los objetos
animal1 = Perro()
animal2 = Gato()

# Llamamos al mismo método en ambos
animal1.hacer_sonido()
animal2.hacer_sonido()
