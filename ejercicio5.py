''' 
   5.-Crea una tupla con los meses del año, pide números al usuario, si el número está entre 1
y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un
mensaje de error. El programa termina cuando el usuario introduce un cero.
'''

meses = ('meses',
    'enero','febrero', 
    'marzo', 'abril',  
    'mayo', 'junio',
    'julio', 'agosto',
    'septiembre','octubre', 
    'noviembre','diciembre'
        )

num = int(input('introduzca un número: '))

if num > len(meses):
    print('el número debe estar en el rango de 1 a 12')
    if num < 1:
        print('el número no puede ser inferior a 1')


print(meses[num])



