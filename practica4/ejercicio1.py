
'''
1.-Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su
cubo.
'''
import random


lista = [ ]

for i in range(1, 10):
    n = random.randint(1, 10)
    lista.append(n)    
print(lista)    


print('lista cuadrados')
for i in lista:
    print(i,  i ** 2)

print('lista cubos')
for i in lista:
    print(i, i ** 3)


