'''
1.-Realizar un menú, donde podemos escoger las distintas opciones de operaciones
(multiplicación de dos números, raiz cuadrada de un número, cubo de un número y división
de dos números) hasta que seleccionamos la opción de “Salir”.
'''

from math import sqrt


def mult(a , b):
    print('La multiplicación es de los números es: ', a * b)
def Cubo(a):
    print('El cubo del número es: ', a **3)
def div(a, b):
    print('La división de los números es: ', a / b)
def RaizCuad(a):
    print('La raíz cuadra del número es', sqrt(a))


menu = int(input('''
Introduce la opción para la operación deseada:
1)Multiplicación de dos números
2)Raíz cuadrada de un número
3)Cubo de un número
4)División de dos número 
5)Salir
 '''))

 
while menu != 5:  
    if menu == 1:
        num1 = float(input('introduce un numero: '))
        num2 = float(input('introduce otro número: '))
        mult(num1, num2)
      
    elif menu == 2:
        num = float(input('intrduce un número: '))
        RaizCuad(num)
          
    elif  menu == 3:
        num = float(input('introduce un número: '))
        Cubo(num)
        
    elif menu == 4:
        num1 = float(input('introduce un numero: '))
        num2 = float(input('introduce otro número: '))
        div(num1, num2)
       
    else: 
         print('opción inválida')
        
    menu = int(input('''

Introduce la opción para la operación deseada:
1)Multiplicación de dos números
2)Raíz cuadrada de un número
3)Cubo de un número
4)División de dos número 
5)Salir
 '''))

