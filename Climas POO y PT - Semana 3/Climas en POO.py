# proemdio semanal del clima
class ClimaSemana:
    def __init__(self):
        # Lista con temperaturas ya establecidas
        self.__temperaturas = [22.5, 23.0, 21.8, 24.2, 22.0, 23.5, 21.9]

    def calcular_promedio(self):
        return sum(self.__temperaturas) / len(self.__temperaturas)

    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

# Clase hija que puede obtener la temperatura máxima
class ClimaSemanaExtendido(ClimaSemana):
    def max_temperatura(self):
        return max(self._ClimaSemana__temperaturas)

# Función principal
def main():
    print("=== Promedio Semanal del Clima (POO) ===")
    clima = ClimaSemana()
    clima.mostrar_promedio()

main()