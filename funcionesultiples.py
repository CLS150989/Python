def func():
    return 1, 2

a, b = func()

print(a)
print(b)

t = (10,20,30) #### CREAnDO UNA TUPLA

a, b, c = t #### atribución múltiple, no se pueden
            #### atribuir más valores de los marcados en la tupla

print(t)


def potencia(x):
    cuadrado = x **2
    cubo = x **3
    return cuadrado, cubo  ###los valores se reconocen como tupla

cuad, cub = potencia(10)  ###la atribución múltiple respeta el lugar que ocupa la variable en la función original
print(cuad)
print(cub)