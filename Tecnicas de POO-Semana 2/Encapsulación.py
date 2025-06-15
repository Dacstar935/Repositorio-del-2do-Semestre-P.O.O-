class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad

    def mostrar_saldo(self):
        return self.__saldo

# Probamos
mi_cuenta = CuentaBancaria(100)
mi_cuenta.depositar(50)
mi_cuenta.retirar(30)
print("Saldo actual:", mi_cuenta.mostrar_saldo())