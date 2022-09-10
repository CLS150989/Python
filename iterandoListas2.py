numbers = [1,2,3,4,5,6,7]

for i in numbers:
     i = i + 10
     print(i)


# importante notar la diferencia cuando la funicón print este dentro
# y fuera del ciclo de instrucción:

lista_nums = [100, 200, 300, 400]     
lista_indice = range(4)
for item in lista_indice:
    lista_nums[item] += 1000
    print(lista_nums) #dentro del bloque de instrucción la función print se imprime 
                      #el número de veces que marca la variable iteradora

lista_nums = [100,200,300,400]
for item in range(4):
    lista_nums[item] += 1000
print(lista_nums) #fuera del bloque de instrcción la función print  se imprime una única vez hasta que
                #el proceso se llevó a cabo.


perrudos = ['punky', 'momesno', 'panke', 'osesno', 'kof' ]

for chara in range(len(perrudos)):
     perrudos[chara] = str(perrudos[chara]) +  ' y chara'    #solo pueden concatenarse datos del mismo tipo, poreso
                                                            #deben convertirse en datos del mismo tipo mediante funciones de trasformación.  

print(perrudos)
