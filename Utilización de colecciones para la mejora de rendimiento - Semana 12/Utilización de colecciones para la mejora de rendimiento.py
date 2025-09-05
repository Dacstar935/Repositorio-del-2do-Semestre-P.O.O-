# Clase para representar un libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Guardamos título y autor como tupla (no cambian)
        self.categoria = categoria   # Categoría del libro
        self.isbn = isbn             # ISBN único del libro
    def __str__(self):
        # Permite mostrar el libro en forma legible
        return f"{self.info[0]} por {self.info[1]} - {self.categoria} (ISBN:{self.isbn})"

# Clase para representar un usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros que el usuario tiene prestados

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}   # Diccionario: ISBN -> objeto Libro
        self.usuarios = {} # Diccionario: ID -> objeto Usuario
        self.ids = set()   # Conjunto para controlar IDs únicos de usuarios

    # Añadir un libro a la biblioteca
    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print("Libro ya existe")  # Evita duplicados por ISBN
        else:
            self.libros[libro.isbn] = libro
            print(f"'{libro.info[0]}' agregado")

    # Quitar un libro de la biblioteca
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado")
        else:
            print("No encontrado")

    # Registrar un nuevo usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids:
            print("ID ya registrado")  # Evita IDs duplicados
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado")

    # Dar de baja a un usuario
    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids.remove(id_usuario)
            print("Usuario dado de baja")
        else:
            print("Usuario no encontrado")

    # Prestar un libro a un usuario
    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros or id_usuario not in self.usuarios:
            print("Libro o usuario no existen")
            return
        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]
        if libro in usuario.libros_prestados:
            print("Ya tiene este libro")  # Evita préstamos duplicados
        else:
            usuario.libros_prestados.append(libro)
            print(f"'{libro.info[0]}' prestado a {usuario.nombre}")

    # Devolver un libro prestado
    def devolver_libro(self, isbn, id_usuario):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado")
            return
        usuario = self.usuarios[id_usuario]
        # Busca el libro en la lista de prestados y lo elimina
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                print(f"'{libro.info[0]}' devuelto")
                return
        print("El usuario no tiene ese libro")

    # Buscar libros por título, autor o categoría
    def buscar_libro(self, termino, tipo="titulo"):
        return [libro for libro in self.libros.values()
                if (tipo=="titulo" and termino.lower() in libro.info[0].lower())
                or (tipo=="autor" and termino.lower() in libro.info[1].lower())
                or (tipo=="categoria" and termino.lower() in libro.categoria.lower())]

    # Listar libros prestados de un usuario
    def listar_prestamos(self, id_usuario):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado")
            return
        usuario = self.usuarios[id_usuario]
        if not usuario.libros_prestados:
            print("No tiene libros prestados")
        else:
            print(f"Libros de {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print("-", libro)

# Menú interactivo de la biblioteca
def menu():
    print("\n--- Biblioteca Digital ---")
    print('\n1. Añadir libro',
          '\n2. Quitar libro',
          '\n3. Registrar usuario'
          '\n4. Dar de baja usuario',
          '\n5. Prestar libro',
          '\n6. Devolver libro'
          '\n7. Buscar libro',
          '\n8. Listar libros prestados',
          '\n9. Salir')
    return input("Elige opción: ")

# Crear la biblioteca
biblio = Biblioteca()

# Bucle principal para interactuar con el usuario
while True:
    opcion = menu()

    if opcion == "1":
        # Añadir libro pidiendo datos al usuario
        biblio.añadir_libro(Libro(input("Título: "), input("Autor: "), input("Categoría: "), input("ISBN: ")))
    elif opcion == "2":
        # Quitar libro por ISBN
        biblio.quitar_libro(input("ISBN del libro a quitar: "))
    elif opcion == "3":
        # Registrar usuario pidiendo nombre e ID
        biblio.registrar_usuario(Usuario(input("Nombre: "), input("ID usuario: ")))
    elif opcion == "4":
        # Dar de baja usuario por ID
        biblio.dar_baja_usuario(input("ID usuario a dar de baja: "))
    elif opcion == "5":
        # Prestar libro a usuario
        biblio.prestar_libro(input("ISBN libro: "), input("ID usuario: "))
    elif opcion == "6":
        # Devolver libro prestado
        biblio.devolver_libro(input("ISBN libro: "), input("ID usuario: "))
    elif opcion == "7":
        # Buscar libros por título, autor o categoría
        tipo = input("Buscar por (titulo/autor/categoria): ").lower()
        resultados = biblio.buscar_libro(input("Término de búsqueda: "), tipo)
        if resultados:
            print("Resultados:")
            [print("-", l) for l in resultados]
        else:
            print("No se encontraron libros")
    elif opcion == "8":
        # Listar libros prestados de un usuario
        biblio.listar_prestamos(input("ID usuario: "))
    elif opcion == "9":
        # Salir del programa
        print("Saliendo...")
        break
    else:
        print("Opción no válida")