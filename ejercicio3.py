'''
3.-Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un
alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota
media, la nota más alta que ha sacado y la menor.

'''
lista_cal = []
for i in range(0 , 5):
    i += 1
    cal = float(input('introduce  calificacion: '))
    lista_cal.append(cal)
print('la lista de calificaciones es: ', lista_cal)
    
for m in lista_cal:
    m = m + 1
    sum_cal = sum(lista_cal)
promedio = sum_cal / len(lista_cal)


print('el promedio general de las caificaciones es:{} '.format(promedio))

print(f'la calificacion máxima obtenida es: {max(lista_cal)}')

print(f'la calificacion mínima obtenida es: {min(lista_cal)}')