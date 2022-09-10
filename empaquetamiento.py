def persona(nombre, pais, edad):
    print(nombre)
    print(pais)
    print(edad)


tupla = ('chara', 'mex', 'chica')
lista = ['chara', 'mex', 'chica']
persona(*tupla)
persona(*lista)

dic = {'nombre': 'chara','pais':'nudos land',
        'edad':'chica'}

persona(**dic)