'''
4.-Codifica un programa en python que nos permita guardar los nombres de los alumnos de
una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de
notas. Guarda la información en un diccionario cuya claves serán los nombres de los
alumnos y los valores serán listados con las notas de cada alumno. El programa pedirá el
número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas
hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista de
alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de
un alumno que ya existe el programa nos dará un error. 
'''

alumnos = {}
num_alum = int(input('Introduce el número de alumnos: '))
if num_alum < 0 :
    print('valor incorrecto')
    
    

for i in range(num_alum):
    nom_alum = input('introduzca el nombre del alumno: ')
    calif = []
    nota = float(input('introduce calificación: '))
    while nota >= 0: 
        calif.append(nota)
        nota = int(input('introduce calificación: '))
    
            
  
alumnos[nom_alum] = calif

for j , k in alumnos.items():
    print(j ,'el promedio es', sum(k) / len(k)) 


print(alumnos) 