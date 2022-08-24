
'''
##########################
concatenando listas:
solo pueden concatenarse listas con listas. 
método pára concatenar un único  valor o elemtno a una  lista
.append:
lista.append()

###########################
símbolo para concatenar listas con más de un sólo elemento en su interior:
lista = ['elemento1', 'elemento2'] + ['elemnto3', ['elemento4'] 

###########################
función para eliminar elemtos de 
una lista:
del()

##########################
simbolo para añadir el mismo elemnto 
repetidas ocasiones  en una misma lista:
*
lista = 10 * [4]
lista = [4,4,4,4,4,4,4,4,4,4]

'''

lista = [1,2,3,4,5]
print(lista)
lista = lista + [6]
print(lista)
lista = [0] + lista
print(lista)
lista = lista + [7,8,9,10]
print(lista)
lista = lista + ['a', 'b', 'c', 'd', 'e']
print(lista)
lista2 = lista + ['punky','caramelo', 'nudo', 'nievlokov']

print(lista2)


lista3 = ['punky','caramelo', 'nudo', 'nievlokov']
print(lista3)
lista3.append('chico')
print(lista3)


lista3.append('blanco')
print(lista3)
print(lista3[-1])
del(lista3[-1])
print(lista3)


lista4 = 10*['chara'] 
print(lista4)
lista5 = lista4 + 5 *['perra']
print(lista5)