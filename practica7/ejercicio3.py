# 7.3 Ejercicio 3 (2 puntos)
# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva
# clase Cuenta Joven que deriva de la anterior. Cuando se crea esta nueva clase,
# además del titular y la cantidad se debe guardar una bonificación que estará
# expresada en tanto por ciento.Construye los siguientes métodos para la clase:
# ● Un constructor.
# ● Los setters y getters para el nuevo atributo.
# ● En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de
# edad;, por lo tanto hay que crear un método es Titular Válido ( ) que
# devuelve verdadero si el titular es mayor de edad pero menor de 25 años y
# falso en caso contrario.
# ● Además la retirada de dinero sólo se podrá hacer si el titular es válido.
# ● El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la
# bonificación de la cuenta.
# ● Piensa los métodos heredados de la clase madre que hay que reescribir.


from ejercicio2 import Cuenta


class CuentaJoven(Cuenta):
    def __init__(self, titular="", cantidad=0, bono = 0, edad = 0) -> None:
        super().__init__(titular, cantidad)
        self.bono = bono
        self.edad = edad
        

    #getters
    def get_bono(self):
        return print(self.bono)
    
    def get_edad(self):
        return print(self.edad)


    #setters
    def set_bono(self, bono):
        self.bono = bono
    
    def set_edad(self, edad):
        self.edad = edad


    #bonificación por cuenta
    def bonificacion(self):        
        bono = self.cantidad * 10 / 100   
        return print("la cantidad bonificada es de: ", bono)


    #titular valido
    def titular_valido(self): 
        if self.edad >= 18 and self.edad <= 25:
            print("Titular válidado")      
        else:
            print("titular invalido")


    #mostrar cuenta actualizado
    def mostrar_cuenta(self):
        return print("*****Cuenta Joven***** \nTitular {} \nEdad: {} \nCantidad: {} \nBonificacion: {}" 
        .format(self.titular, self.edad, self.cantidad, self.bonificacion())) 
        
            


cj = CuentaJoven()

cj.set_cantidad(2000)
cj.bonificacion()


