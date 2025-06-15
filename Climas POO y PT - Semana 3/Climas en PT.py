# Función con temperaturas
def ingresar_temperaturas():
    return [22.5, 23.0, 21.8, 24.2, 22.0, 23.5, 21.9]  # Temperaturas de lunes a domingo

# Función para calcular el promedio
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    print("=== Promedio Semanal del Clima ===")
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

main()