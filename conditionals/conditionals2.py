edad = int(input("informe su edad"))
 
if(edad < 0):
    print('la edad es inválida')
elif (edad > 150):
    print('la edad es imposible')
elif(edad < 18):
    print("ustedes menor de edad")
elif(edad > 18 and edad < 150):
    print("usted tiene", edad, "años")  
