# crypte un texte avec le chiffre de Cesar

def lettre(c):
    # retourne vrai si c est une lettre non accentuee
    car = ord(c.upper())
    return car>64 and car<91
    
def decalage(c,k):
    # decale une lettre majuscule. Les autres carateres ne sont pas modifies
    car = ord(c.upper())
    if lettre(c):
        car += k
        while car>90:
            car -= 26
        while car<65:
            car += 26
        return chr(car)
    else:
        return ""

def cesar(s,d,crypte):
    # effectue le decalage d sur la chaine de caracteres s
    chiffre=''
    for c in s:
        if lettre(c):
            if crypte:
                chiffre += decalage(c,d)
            else:
                chiffre += decalage(c,-d)
        else:
            chiffre += c
    return chiffre


# programme principal
texte="Ave Caesar morituri te salutant"
texte_code = cesar(texte,3,True)
print(texte_code)
texte_decode = cesar(texte_code,3,False)
print(texte_decode)

