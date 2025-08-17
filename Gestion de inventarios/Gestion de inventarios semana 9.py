# Clase para un producto/artículo
class Articulo:
    def __init__(self, codigo, nombre, stock, precio):
        # Guardamos los datos del producto
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock
        self.precio = precio

    def mostrar(self):
        # Devuelve información del producto como texto
        return f"[{self.codigo}] {self.nombre} -> {self.stock} unidades, ${self.precio}"


# Clase para manejar el inventario
class SistemaInventario:
    def __init__(self):
        self.lista = []  # Lista de productos

    # Agregar producto
    def registrar(self, articulo):
        if any(a.codigo == articulo.codigo for a in self.lista):
            print("Código repetido")
        else:
            self.lista.append(articulo)
            print("Registrado")

    # Eliminar producto
    def borrar(self, codigo):
        for a in self.lista:
            if a.codigo == codigo:
                self.lista.remove(a)
                print("Borrado")
                return
        print("No encontrado")

    # Modificar cantidad o precio
    def modificar(self, codigo, stock=None, precio=None):
        for a in self.lista:
            if a.codigo == codigo:
                if stock is not None: a.stock = stock
                if precio is not None: a.precio = precio
                print("Modificado")
                return
        print("No encontrado")

    # Buscar por nombre
    def buscar(self, texto):
        resultados = [a for a in self.lista if texto.lower() in a.nombre.lower()]
        print(*[x.mostrar() for x in resultados] if resultados else ["No encontrado"], sep="\n")

    # Mostrar todos los productos
    def ver(self):
        print(*[a.mostrar() for a in self.lista] if self.lista else ["Inventario vacío"], sep="\n")


# Menú principal
def ejecutar():
    sistema = SistemaInventario()  # Creamos el inventario
    while True:
        # Mostramos opciones
        print("\n1.Registrar \n2.Borrar \n3.Modificar \n4.Buscar \n5.Ver \n6.Salir")
        opcion = input("Opción: ")

        # Registrar producto
        if opcion == "1":
            try:
                codigo = input("Código: ")
                nombre = input("Nombre: ")
                stock = int(input("Stock: "))
                precio = float(input("Precio: "))
                sistema.registrar(Articulo(codigo, nombre, stock, precio))
            except ValueError:
                print("Cantidad o precio inválidos")

        # Borrar producto
        elif opcion == "2":
            sistema.borrar(input("Código: "))

        # Modificar producto
        elif opcion == "3":
            codigo = input("Código: ")
            stock = input("Nuevo stock (deja vacío si no cambia): ")
            precio = input("Nuevo precio (deja vacío si no cambia): ")
            sistema.modificar(
                codigo,
                int(stock) if stock else None,
                float(precio) if precio else None
            )

        # Buscar producto
        elif opcion == "4":
            sistema.buscar(input("Producto a buscar: "))

        # Ver inventario completo
        elif opcion == "5":
            sistema.ver()

        # Salir del programa
        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


# Ejecutamos el programa
ejecutar()