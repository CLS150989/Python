'''
2.-Crea una lista e inicializarla con 5 cadenas de caracteres leídas por teclado. Copia
los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la
pantalla.
'''


lista = []
t = 1
for i in range(5):
    palabra = input('introduce tu {}° palabra: '.format(t))
    lista.append(palabra)
    t += 1

print(lista)

lista_inv = []
for j in reversed(lista):
    lista_inv.append(j)
print(lista_inv)