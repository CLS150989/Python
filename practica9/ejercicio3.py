'''
9.3 Ejercicio 3 (2 puntos)
Obtener la cantidad de elementos mayores a 5 en la tupla.
tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
'''


tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
mayor_a_5 = [] 

for i in tupla:
  if i > 5:
    mayor_a_5.append(i)

print(mayor_a_5)
print('la cantidad de elementos mayor a 5 es ', len(mayor_a_5))