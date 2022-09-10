#### son las funciones capaces de recibir
#### una cantidad variada de parámetros
#### pueden recibir 0 o n parámetros

def lista_de_argumentos(*lista):  #*args: lista deparámetros
    print(lista)


lista_de_argumentos('nudo', 'chara','kof', 'chico')  #kwargs lista de parámetros llave valor
lista_de_argumentos(1,2,3,4,5,6)

def lista_de_argumentos_asociativos(**dic):
    print(dic)

lista_de_argumentos_asociativos(a='chara', b='nudo', c='kof')
lista_de_argumentos_asociativos(uno='chara', dos='nudo', tres='kof')

def argumetos(*args, **kwargs):
    print(args)
    print(kwargs)

argumetos(1,2,3,4, uno=1, dos=2, tres=3)