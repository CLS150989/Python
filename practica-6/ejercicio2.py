'''
2.-Pedir al usuario y determinar si el número ingresado es primo o no.
'''

num = int(input('introduzca un número: '))

primo = 0
i = 2
indicador = 0

while i < num: 
    primo = num % i
    if primo == 0:
        indicador = cont + 1
    i += 1

if cont == 0:
    print('el numero es primo')
else:
    print('el número no es primo')


