# 7.2 Ejercicio 2 (2 puntos)
# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es
# una persona) y cantidad (puede tener decimales). El titular será obligatorio y la
# cantidad es opcional. Construye los siguientes métodos para la clase:
# ● Un constructor, donde los datos pueden estar vacíos.
# ● Los setters y getters para cada uno de los atributos. El atributo no se puede
# modificar directamente, sólo ingresando o retirando dinero.
# ● mostrar(): Muestra los datos de la cuenta.
# ● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad
# introducida es negativa, no se hará nada.
# ● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar
# en números negativos.


from re import I


class Cuenta:
    def __init__(self, titular = "", cantidad = 0) -> None:
        self.titular = titular
        self.cantidad = cantidad
        self.set_cantidad(cantidad)
        self.set_titular(titular)
         
    #getters
    def get_titular(self):
        return print(self.titular)
    
    def get_cantidad(self):
        return print("cantidad en la cuenta es de: ",self.cantidad)
    
    #setters
    def set_titular (self, titular):
        self.titular = titular
    
    def set_cantidad (self, cantidad):
        self.cantidad = cantidad
    
    #metodo mostrar
    def mostrar_cuenta (self):
        return print("titular: {} \ncantidad: {}".format(self.titular, self.cantidad)) 
    
    def ingresar_cantidad(self, cantidad = 0): 
        print("la cantidad en cuenta es", self.cantidad)
        cantidad =float(input("Introduce la cantidad a depositar:  "))
        while cantidad < 0 or isinstance(cantidad, str):
            print("cantidad incorrecta")
            cantidad =float(input("Introduce la cantidad a depositar:  "))
        cantidad_final = self.cantidad + cantidad
        self.cantidad = cantidad_final
        return print("la cantidad total en cuenta es:  ", cantidad_final)
            
    #método retirar
    def retirar_cantidad(self, retiro=0):
        print("la cantidad en cuenta es", self.cantidad)
        retiro =float(input("introduce la cantidad a retirar: "))
        valor_final = self.cantidad - retiro   
        self.cantidad = valor_final
        return print("la cantidad restante en cuenta es: ", valor_final) 
    

c = Cuenta()
c.set_cantidad(200)
c.ingresar_cantidad()
c.retirar_cantidad()

