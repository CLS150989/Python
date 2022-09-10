
###### diccionarios ##############


tel = { 'kof': 34567545345,
        'nudera':23456787,
        'chara':212345434,
        'osesno':213457643,
        'punky':3245678985
}

#######funciones de diccionarios###############

print(len(tel))  #función que regresa la longitud del diccionario
del(tel['kof']) #función para borrar llave o valor
print(tel)
print(tel.keys())  #función que retrona las llaves
print(tel.values()) #funcion que retorna valores
print(tel.get('chara')) #funcion para tambien obtener llaves o valores
print(tel.popitem())  #función que retorna un elemento y al mismo tiempo lo remueve
print('kof' in tel)


tel2 = {'chico': 2343567567,
      'charuda': 345675634}

tel.update(tel2) #función para mezclar diccionarios 
print(tel)

t = (1,2,3,4,5)
tel[t] = 'chara y nudo'
print(tel)