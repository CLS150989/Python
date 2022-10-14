# def decorator_triangulo(func):
#     def wrapper_triangulo_area(a, b):
#         area = a * b / 2
#         print("el area del triángulo con  área: {} \n y altura: {} es: ".format( a, b ))
#         return print(area)
#     return wrapper_triangulo_area    


# @decorator_triangulo
# def parametros_tringulo(base, altura):
#     return print(base, altura)

# parametros_tringulo(4,6)


# función tradicional 

def area_triangulo(a,b):
    area = a *b / 2
    return print(area)

#función lambda: se empea para resumir la sintaxis
# de una función tradicional

area_trian = lambda a, b: a*b /2

area_triangulo(4,5)
print(area_trian(4,5))


