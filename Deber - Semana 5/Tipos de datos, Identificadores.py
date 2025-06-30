# Este programa pide la base y la altura de un triángulo,

def calcular_area(base, altura):
    # Función que devuelve el área del triángulo
    return (base * altura) / 2


# Pedimos los datos al usuario
base_ingresada = input("Ingresa la base del triángulo: ")
altura_ingresada = input("Ingresa la altura del triángulo: ")

# Inicializamos la variable que usaremos para validar
valores_validos = True

# Intentamos convertir los valores a número decimal
try:
    base = float(base_ingresada)
    altura = float(altura_ingresada)

    # Verificamos que sean positivos
    if base <= 0 or altura <= 0:
        print("La base y la altura deben ser mayores que cero.")
        valores_validos = False

except ValueError:
    print("Por favor ingresa números válidos.")
    valores_validos = False

# Si todo está bien, calculamos el área
if valores_validos:
    area = calcular_area(base, altura)
    print(f"El área del triángulo es: {area:.2f}")
