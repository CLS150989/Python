import math

numeros = [1,4,9,16,25]


# #sintaxis de list cpmprehensions: variable, ciclo y, si existe, condición
raices = [ int(math.sqrt(x)) for x in numeros ]

for n in numeros:
    raices.append(int(math.sqrt(n)))


print(raices)

#sintaxis: variable ,  condición para variable, ciclo  
print(numeros)
v = [ x if x > 10 else '*' for x in numeros ]

print(v)

mayus = [c.upper() for c in "Chara y Osesno son amigos"]
print(mayus)


vocal = [v if v in 'aeiou' else '*' for v in 'chara y osesno son amigos']
print(vocal)