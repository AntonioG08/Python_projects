from os import *
""" Proyecto con el uso de clases """


class Persona:
    def __init__(self, nombre2, apellido2):
        self.nombre2 = nombre2
        self.apellido2 = apellido2


class Cliente(Persona):
    def __init__(self, nombre2, apellido2, numero_cuenta, balance):
        super().__init__(nombre2, apellido2)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def imprimir(self):
        print(f'Su estado de cuenta actual es de ${self.balance} pesos')

    def depositar(self, ingreso):
        self.balance += ingreso

    def retiro(self, retirar):
        if retirar <= self.balance:
            self.balance -= retirar
            print(f'Se ha retirado correctamente ${retirar} pesos')
        elif retirar > self.balance:
            print('Lo lamentamos, el valor es mayor a su saldo de cuenta.\n Intente nuevamente')


print('Saludos bienvenido a Santander, por favor introduzca su nombre para identificarse: ')
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
system('cls')
usuario1 = Cliente(nombre, apellido, '5579_0990_1408_0107', 0)


def inicio():
    opcion = 0

    while opcion != 4:
        system('cls')
        print(f'Saludos {usuario1.nombre2} {usuario1.apellido2}, es un gusto tenerle aqui')
        print('Idiquénos como podemos ayudarle siguiendo el siguiente menú de opciones')
        print('1 Imprimir estado de cuenta\n2 Realizar retiro de efectivo\n3 Realizar deposito de efectivo\n4 Salir')
        opcion = int(input('Ingrese su opcion: '))

        if opcion == 1:
            system('cls')
            print(f'El estado de la cuenta {usuario1.numero_cuenta} es el siguiente')
            usuario1.imprimir()
            print('------------')
            opcion = int(input('Elija una opcion\n1 Volver al menú\n2 salir\nIngrese su opcion: '))
            if opcion == 1:
                pass
            elif opcion == 2:
                opcion = 4

        if opcion == 2:
            system('cls')
            dinero2 = int(input('Ingrese la cantidad que desea retirar: '))
            usuario1.retiro(dinero2)
            opcion = int(input('Elija una opcion\n1 Volver al menú\n2 salir\nIngrese su opcion: '))
            if opcion == 1:
                pass
            elif opcion == 2:
                opcion = 4

        if opcion == 3:
            system('cls')
            dinero = int(input('Ingrese la cantidad que desea depositar: '))
            usuario1.depositar(dinero)
            print('-------------')
            print(f'Se ha depositado correctamente ${dinero} pesos')
            opcion = int(input('Elija una opcion\n1 Volver al menú\n2 salir\nIngrese su opcion: '))
            if opcion == 1:
                pass
            elif opcion == 2:
                opcion = 4

    system('cls')
    print('Sesión cerrada con éxtio')
    print('Ha sido un gusto atenderle, vuelva pronto!')


inicio()
