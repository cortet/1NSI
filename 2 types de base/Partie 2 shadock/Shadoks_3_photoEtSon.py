# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 13:36:31 2019
@author: NLG
"""
#################################
###### == LES SHADOKS == ########
#################################

## les librairies
# faire :  pip install playsound   et   pip install pygame
from playsound import playsound
import sys,pygame,time


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
        print(tab)  # affiche la liste en console (chiffres entre 0 et 3)
        return tab
    
### Tableau de conversion : base4 => numération Shadoks
shadok=["GA", "BU", "ZO", "MEU"]

def convertShadok(chiffre : int) -> str :
    if 0<= chiffre <=3 :
        return shadok[chiffre]
    else :
        return
    
    
###############################
### OUTILS D'ANIMATION ########
###############################
NOIR  = (0  , 0  , 0  )

def fermerSiOnAppuieSurLaCroix() -> None :
    # Fermeture de pygame et du pgm, si on ferme la fenêtre prématurément
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 


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

### Animation :  1 frame pendant 8s :
# et c'est au cours de l'animation que chaque chiffre est converti en GA, BU, ZO, MEU

# Initialisation de pygame
pygame.init()
width  = 400
height = 100
#on crée un écran Pygame (de type Surface .. ou plus exactement pygame.Surface)
screen = pygame.display.set_mode( ( width, height) )

# Chaque chiffre de la liste tabBase4[] est illustré par une photo et un son
# .. puis il est supprimé de la liste, et on passe au chiffre suivant.
# La boucle de l'animation est donc   "while tabBase4" [ au lieu de l'habituel while(True) ]
# (l'animation dure tant qu'il reste des chiffres ds la liste)

while tabBase4:
    fermerSiOnAppuieSurLaCroix()
    
    # on récupère un nouveau chiffre (le 1er chiffre de la liste)
    chiffre = int(tabBase4[0])
    # on nettoie l'écran (en le remplissant entièrement de noir)
    screen.fill(NOIR)
    # on convertit le chiffre : base4 => GA, BU, ZO ou MEU (grâce au tableau shaddok[])
    motShadok = shadok[chiffre]       
    # on joue le son du fichier : GA.wav, BU.wav, ZO.wav ou MEU.wav
    playsound(motShadok +'.wav')
    # On charge l'image en mémoire
    monImg = pygame.image.load(motShadok +'.png') # monImg est de type Surface
    monImg = monImg.convert() # puis la convertit en format pygame
    screen.blit(monImg,(0,0)) # et on donne sa position sur l'écran : (0,0)
   
    pygame.display.flip() # juste avant la pause, on actualise l'affichage
    time.sleep(8)  # pause de 8s pour écouter le son jusqu'au bout
    tabBase4 = tabBase4[1:] #on supprime le chiffre

### Fin de l'animation .. et du programme
pygame.quit()