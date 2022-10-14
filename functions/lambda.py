#suma = lambda x, y: x + y
#print (suma(3,5))



frutas = ['Apple', 'Kiwi', 'Watermelon', 'pineaple']


def empieza_con_a(word):
    return word[0] == 'A' or word[0] == 'a'



trueOrFalseList = list(map(lambda a: a[0] == 'A' or a[0] == 'a', frutas ))  ## map: iterable function returns a list
print(trueOrFalseList)




numList = [1,23, 4, 4, 7, 9, 4, 6, 8, 9, 2, 56]

numTrueOrFlase = list(filter(lambda a: a%3 == 0, numList)) ## filter: iterable function returns a list 
print(numTrueOrFlase)

print(sum(numTrueOrFlase))


