my_list = [1,2,3,4, 'a', 'b']

for i in range (1,11,2):
    print(i)
else:
    print('se acabó el ciclo')


mi_dict = { 1: 'hola', 2:' como', 3:'estas'}
print(mi_dict[1]) 

my_list.insert(2, 'computadora')
my_list[2] = 'comoutadora'


'''
metodos en listas
.append.
.insert
.sort
.extend
'''

my_list2 = []
for i in range(10):
    my_list.append(i)
    print(i)

a = 1
my_list3 = []
for i in 'python learning':
    a = a + 1
    my_list3.append(a)


dic = {}

a = 1
for i in range(10):
    
    dic[i] = a
    a += 1
print(dic)


for i in range(10):
    if(i==5):
        continue #omite el valor dentro del ciclo
    print(i)
print('terminó')