'''
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás
 desde ese número hasta 0 sepaados por comas
'''

num = int(input('introduce un núemero: '))
lista = []

for i in range(num):
    lista.append(i)
    print(reversed(lista))

