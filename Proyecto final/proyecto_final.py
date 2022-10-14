from lista import palabras
from diagrama import vidas_diccionario_visual
import random 



#####función para asignar una palabra aleatoria a una variable 
##### y pedir la entrada por teclado del usuario
def random_select(palabra):    
    palabra_lista = random.choice(palabra)
    if len(palabra_lista) == 8:
        return  input("Adivna la palabra de 8 letras \n_ _ _ _ _ _ _ _: ")
    elif len(palabra_lista) == 5:
        return input("Adivna la palabra de 5 letras \n_ _ _ _ _: ")
    else:
        if len(palabra_lista) == 4:
           return input("Adivna la palabra de 4 letras \n_ _ _ _: ")    
    


palabra_juego = random_select(palabras)
palabra_usuario = input("")
if palabra_usuario in palabras:
    print('has ganado')
    

for i in reversed(vidas_diccionario_visual.keys()):

    if palabra_usuario in palabras:
        print('has ganado')
        break
    else: 
        print(vidas_diccionario_visual.get(i))
        print('intenta de nuevo')
        palabra_usuario = input("")

    


