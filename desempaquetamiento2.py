lista = [9, 8, 11]
tupla = (13,6,19)
def func(a,b,c):
    print(a)
    print(b)
    print(c)
'''
lista.sort()
func(*lista)
'''
ordered_tuple = [*tupla]
ordered_tuple.sort()
func(*ordered_tuple)
func(zip(('a', 'b', 'c'), lista))
