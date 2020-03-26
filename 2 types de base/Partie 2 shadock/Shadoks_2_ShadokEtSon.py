# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 13:36:31 2019
@author: NLG
"""
#################################
###### == LES SHADOKS == ########
#################################

## les librairies :  pip install playsound
import sys, time
from playsound import playsound


#################################
### OUTILS DE CONVERSION ########
#################################

### Fonction de conversion : système décimal => base 4 
# le résultat est un tableau de chiffres allant de 0 à 3
def convertBase4(nb:int) -> list :
    # si nb=0 alors l'écriture est 0 (et on sort)
    # sinon on fait des divisions successives par 4 :
    # * à chaque division le reste nb % 4 est stoké dans une liste, en 1ère position
    # * puis avec le quotient nb // 4, on refait une nouvelle division 4, donc nb = nb // 4
    # etc ... on s'arrête lorsque le quotient est 0
    if nb == 0 :
        return [0]
    else :
        tab = []
        while not(nb == 0):
            tab.insert( 0, int(nb % 4) )  #list.insert(index, element)
            nb = nb // 4
        return tab
    
### Tableau de conversion : base4 => numération Shadoks
shadok=["GA", "BU", "ZO", "MEU"]

def convertShadok(chiffre : int) -> str :
    if 0<= chiffre <=3 :
        return shadok[chiffre]
    else :
        return


###############################
### LANCEMENT DU PGM ##########
###############################        
        
### Entrer un nombre en console : 
# on le convertit : système décimal => base 4  (0, 1, 2, 3)
nb = int(input("Entrer un entier positif (par exemple : 156) : "))
if nb < 0 :
    print ("Non, il faut un entier  P O S I T I F !!! ..")
    sys.exit()
tabBase4 = convertBase4(nb)

### Conversion en Shadoks
#on le caste en tableau de string (pour pouvoir utiliser join)
tabBase4string = *map(str,tabBase4),
#ou bien plus facilement :  tabBase4string = [str(chiffre) for chiffre in tabBase4]
print("En base 4, le nombre %i s'écrit : " %(nb) +"\x1b[35m"+"".join(tabBase4string)+"\x1b[0m.")

# on convertit chaque chiffre : base4 => GA, BU, ZO ou MEU (grâce au tableau shaddok[])
motShadoks = *map(convertShadok,tabBase4),
#ou bien plus facilement :  motShadoks = [convertShadok(chiffre) for chiffre in tabBase4]
print("Et les Shadoks prononcent : \x1b[46m"+" ".join(motShadoks)+"\x1b[0m.")

### Jouer les fichiers de son dans l'ordre
for mot in motShadoks:
    playsound(mot+'.wav', False)
    time.sleep(8)  # pause de 8s pour laisser jouer le son

