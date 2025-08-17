import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
    '1': 'Tecnicas de POO-Semana 2/Abstracción.py',
        '1.1': 'Tecnicas de POO-Semana 2/Encapsulación.py',
        '1.2': 'Tecnicas de POO-Semana 2/Herencia.py',
        '1.3': 'Tecnicas de POO-Semana 2/Polimorfismo.py',
    '2': 'Climas POO y PT - Semana 3/Climas en PT.py',
        '2.1': 'Climas POO y PT - Semana 3/Climas en PT.py',
    '3': 'EjemplosMundoReal_POO/EjemplosMundoReal_POO.py',
    '4': 'Deber - Semana 5/Tipos de datos, Identificadores.py',
    '5': 'Clases_Poo_Semana6/Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
    '6': 'Construcores y destructores - semana 7/Constructores y Destructores - Deber.py',
        '6.1': 'Construcores y destructores - semana 7/perro.txt',
    '7': 'Gestion de inventarios/Gestion de inventarios semana 9.py'
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()