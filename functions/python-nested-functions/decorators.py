def mensaje(func):
    def n_mayus():
        func()
        print("tienes un mensaje {} ".format(func())) 
    return n_mayus


@mensaje
def to_uppercase():
    nom = input('Ingresa tu numbre: ')
    return print(nom.upper)


to_uppercase()