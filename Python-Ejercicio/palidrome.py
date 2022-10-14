
pal = input('ingrese un string: ')

def palindrome(pal):
    pal = pal.lower().replace(' ', '') ####necesario sustituir espacios por no espacios y converirlo todo a minúculas
    if pal == pal[::-1]:
        print('es palindrme')
    else:
        print('no es palíndrome')
    

palindrome(pal)
 





