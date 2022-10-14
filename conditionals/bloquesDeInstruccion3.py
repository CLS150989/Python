num = int(input('digite un número: '))

if(num > 10):
    print('el numero es mayor que 10')
    if(num<=15):
        print("el numero es mayor a 10 pero menor a 15")
else:
    if(num>5):
        print('el numero es menor a 10 y mayor a 5')
        if(num==7):
            print('el numero es igual a 7')
    else:
        print("el valor es menor a 5")
    
