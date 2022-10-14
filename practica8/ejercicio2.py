'''
Escribe un programa que lea una cadena y devuelva un diccionario donde las llaves seràn
los caracteres y los valores de dichas llaves serà el número de veces que aparece el
carácter en la cadena
'''


user_string = input('introduce una cadena de caracteres: ')

dict = {}

for i in user_string:
    dict[i] = user_string.count(i)


print(dict)