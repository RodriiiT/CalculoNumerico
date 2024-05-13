"""
Crear una clase llamada cuenta que trabajará con los siguientes atributos:

-titular; que es una persona
-cantidad; puede tener decimales

que el titular sea obligatorio y la cantidad opcional. Construir los
siguientes metodos para la clase:

1. Un constructor, donde los datos pueden estar vacíos.
2. Los setters y los getter para cada uno de los atributos, el atributo no
se puede modificar directamente, solo se puede modificar, ingresando o
retirando dinero.
3. Mostrar los datos de la cuenta.
4. Se ingrese una cantidad a la cuenta, si la cantidad inicial es negativa
no se hará nada.
5. Si se retira una cantidad a la cuenta, la cuenta puede mostrar números
rojos, es decir, que puede quedar en negativo.
"""

class Cuenta:
    def __init__(self,titular,cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def getTitular(self):
        return self.titular

    def setTitular(self,titular):
        self.titular = titular

    def getCantidad(self):
        return self.cantidad

    def datosCuenta(self):
        print("Titular: " + self.titular + ", Cantidad: " + str(self.cantidad))

    def ingresar(self,cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self,cantidad):
        self.cantidad -= cantidad
        

nombre = input("Ingrese el nombre del titular: ")
cant_inic = float(input("Ingrese la cantidad inicial: "))
cuenta2 = Cuenta(nombre,cant_inic)
cent = input("¿Desea continuar? (s/n)")
while cent == 's':
    opcion = input("Desea ingresar o retirar dinero (i:ingresar/r:retirar)")
    if opcion == 'i':
        cantidad = float(input("Ingrese una cantidad: "))
        cuenta2.ingresar(cantidad)
    elif opcion == 'r':
        antidad = float(input("Retire una cantidad: "))
        cuenta2.retirar(cantidad)
        
    cuenta2.datosCuenta()
    cent = input("¿Desea continuar? (s/n)")
        
    
