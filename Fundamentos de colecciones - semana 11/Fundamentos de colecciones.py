import json

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id} - {self.nombre} - Cantidad: {self.cantidad} - Precio: {self.precio}"

    def convertir_a_dicc(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

# Clase Inventario
class Inventario:
    def __init__(self):
        # aquí guardamos los productos en un diccionario
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("Ese ID ya existe, no se puede repetir.")
        else:
            self.productos[producto.id] = producto
            print("Producto agregado!")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
        else:
            print("No existe un producto con ese ID.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].cantidad = nueva_cantidad
            if nuevo_precio is not None:
                self.productos[id_producto].precio = nuevo_precio
            print("Producto actualizado.")
        else:
            print("No existe ese producto.")

    def buscar_por_nombre(self, nombre):
        encontrado = False
        for p in self.productos.values():
            if p.nombre.lower() == nombre.lower():
                print(p)
                encontrado = True
        if not encontrado:
            print("No se encontró ese producto.")

    def mostrar_todos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for p in self.productos.values():
                print(p)

    # Guardar en archivo
    def guardar(self, archivo="inventario.json"):
        datos = {id: p.convertir_a_dicc() for id, p in self.productos.items()}
        with open(archivo, "w") as f:
            json.dump(datos, f)
        print("Inventario guardado en archivo.")

    # Cargar de archivo
    def cargar(self, archivo="inventario.json"):
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                for id, prod in datos.items():
                    self.productos[id] = Producto(prod["id"], prod["nombre"], prod["cantidad"], prod["precio"])
            print("Inventario cargado.")
        except FileNotFoundError:
            print("No hay archivo guardado, empezamos con inventario vacío.")

# Menú en consola
def menu():
    inv = Inventario()
    inv.cargar()

    while True:
        print("\n----- MENÚ INVENTARIO -----")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            id_p = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            nuevo = Producto(id_p, nombre, cantidad, precio)
            inv.agregar_producto(nuevo)

        elif opcion == "2":
            id_p = input("ID del producto a eliminar: ")
            inv.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("ID del producto a actualizar: ")
            cant = input("Nueva cantidad (dejar vacío si no cambia): ")
            pre = input("Nuevo precio (dejar vacío si no cambia): ")
            cant = int(cant) if cant else None
            pre = float(pre) if pre else None
            inv.actualizar_producto(id_p, cant, pre)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inv.buscar_por_nombre(nombre)

        elif opcion == "5":
            inv.mostrar_todos()

        elif opcion == "6":
            inv.guardar()

        elif opcion == "7":
            inv.guardar()
            print("Saliendo del programa...")
            break
        else:
            print("Opción incorrecta, intenta de nuevo.")

# Ejecución
if __name__ == "__main__":
    menu()