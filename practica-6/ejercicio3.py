'''
3.-Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó
10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un programa
para determinar cuánto debe pagar mensualmente y el total de lo que pagó
hasta los 20 meses.
'''

pago = 5
i = 0
pago_mes = [] 

for i in range(0, 20):
    pago = pago * 2   
    pago_mes.append(pago)
    i += 1
    
print(pago_mes)
print('la suma total a pagar en 20 meses: ', sum(pago_mes))