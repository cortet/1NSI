# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:20:40 2020

@author: SOPHIE
"""
def decalage(c,k):
    # decale une lettre majuscule. Les autres carateres ne sont pas modifies
    car = ord(c.upper())
    car += k
    while car>90:
        car -= 26
    while car<65:
        car += 26
    return chr(car)

def cesar (text, decal, crypte) :
    #codage de césar
    # effectue le decalage d sur la chaine de caracteres s
    chiffre=''
    for i in range(len(text)):
        if crypte:
            chiffre += decalage(text[i],decal)
        else:
            chiffre += decalage(text[i],-decal)
    return chiffre

# programme principal
#texte="Ave Caesar morituri te salutant"
texte=str(input('saisir une phrase    : '))
d = int(input('saisir le décalage    : '))

texte_code = cesar(texte,d,True)
print(texte_code)
texte_decode = cesar(texte_code,d,False)
print(texte_decode)