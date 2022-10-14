'''
8.3 Ejercicio 3 (2 puntos)
Vamos a crear un programa en python donde vamos a declarar un diccionario para
guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta
y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de
los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras
cada consulta el programa nos preguntará si queremos hacer otra consulta.
'''
frutas = {'manzana':10, 'pera': 15, 'sandia': 9, 'coco': 15, }

nom_fruta = input('introduzca el nombre de la fruta: ')

sum_precio_fruta = []

while nom_fruta in frutas.keys():
    kilo_fruta = float(input('introduzca la cantidad de fruta vendida en kg: '))
    precio_fruta = kilo_fruta * frutas.get(nom_fruta)
    sum_precio_fruta.append(precio_fruta)
    nom_fruta = input('introduzca el nombre de otra fruta: ')
    if nom_fruta not in frutas.keys():
        print('fruta inexistente')
    
print('el precio total de la fruta vendida es: ', sum(sum_precio_fruta))