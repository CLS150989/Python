'''
9.2 Ejercicio 2 (2 puntos)
Obtener el cuadrado de todos los elementos en la lista.
Lista: [1,2,3,4,5,6,7,8,9,10]
'''

lista = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrados = []

for i in lista:
    cuadrados = i*i
    lista_cuadrados.append(cuadrados)

print(lista_cuadrados)