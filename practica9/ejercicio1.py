'''
9.1 Ejercicio 1 (2 puntos)
Realice un programa que pregunte aleatoriamente una multiplicación. El programa
debe indicar si la respuesta ha sido correcta o no (en caso que la respuesta sea
incorrecta el programa debe indicar cuál es la correcta). El programa preguntará
10 multiplicaciones, y al finalizar mostrará el número de aciertos.
'''

import random

a = random.randint(1,10)
b = random.randint(1,10)
user_responses = []
user_validation = []
correct_answers = []


for i in range(3):
    user_input = int(input('multiplica: {} x {} = '.format(a,b)))
    correct_answers.append(a * b)
    user_responses.append(user_input)
    a = random.randint(1,10)
    b = random.randint(1,10)
    
   

print(correct_answers)
print(user_responses)
user_validation = (list(map(lambda l1, l2 : l1 == l2, correct_answers, user_responses)))
print(user_validation)
