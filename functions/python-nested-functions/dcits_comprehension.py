##### {key:value for value in iteralbe if condition} 
#### diccionario donde el valor de la llave sern los numeros del 1 al 100 excepto los múltiplos de tres y
# el valor de la llave la llave elevada al cubo

my_dict = {i:i**3  for i in range (1, 101) if i % 3 !=0}

print(my_dict)