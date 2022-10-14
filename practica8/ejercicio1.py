'''
8.1 Ejercicio 1 (2 puntos)
Escribe un programa python que pida un número por teclado y que cree un
diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los
valores sean los cuadrados de las claves.
'''

user_num = int(input('introduce un numero: '))

empty_dict = {}

for i in range(1, user_num + 1):
    empty_dict[i] = i*i

print(empty_dict)