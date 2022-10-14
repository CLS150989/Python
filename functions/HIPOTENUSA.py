import math


def pendiente(x1, y1, x2, y2):
    lado_a= x2 - x1 
    lado_b= y2 - y1
    pendiente_cuadrada = lado_a**2  + lado_b**2 
    pendiente = math.sqrt(pendiente_cuadrada)
    return pendiente
   
        
def intercepta( x1, x2, y1, y2):
    lado_a= x2 - x1
    lado_b= y2 - y1
    if lado_a > 0: 
          print("la línea intercepta con ¨y¨ es  ", lado_b)
    return intercepta







x1= 20
y1= 17

x2= 25
y2= 22
 
print("la pendiente o hipotenusa de la línea es" , pendiente(x1, y1, x2, y2))







