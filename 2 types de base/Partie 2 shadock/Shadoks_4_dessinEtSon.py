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
import sys,pygame
import math


#################################
### OUTILS DE CONVERSION ########
#################################

### Fonction de conversion : système décimal => base 4 
# le résultat est un tableau de chiffres allant de 0 à 3
def convertBase4(nb:int) -> list :
    # si nb=0 alors l'écriture est 0 (et on sort)
    # sinon on fait des divisions successives par 4 :
    # * à chaque division le reste nb % 4 est stoké dans une liste, en 1ère position
    # * puis avec le quotient nb // 4, on refait une nouvelle division 4 : nb = nb // 4
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
BLANC = (255, 255, 255)
NOIR  = (0  , 0  , 0  )
ROSE  = (255, 0  , 255)


def eqParamDeCercle(ecran : pygame.Surface, xCentre :int, yCentre : int, r : int, t: int) -> None:
    # Ici, on dessine juste un point du cercle (celui de paramètre t)
    # avec les équations paramétriques du cercle :
    #    Formule :  x(t) = Xcentre + R cos(t)   et  y(t) = Ycentre + R sin(t)
    # t varie de 0 à 500. (NB : dès que t=360° le cercle sera complet) 
    # Mais Python veut des angles en radians pour cos/sin, donc t est converti
    #    en radians avec la fct   math.radians()
    x = xCentre  + int (r * math.cos( math.radians(t) ) )
    y = yCentre  + int (r * math.sin( math.radians(t) ) )
    
    # le tracé est seulement un gros point d'épaisseur 8px
    pygame.draw.circle(ecran, BLANC, (x,y), 4)
    

def dessinShadok(ecran : pygame.Surface, chiffre : int, t: int) -> None:
    ### 2 styles de figures sont possibles : 
    ## le rond pour le chiffre 0
    if chiffre == 0 :
        eqParamDeCercle(ecran,width//2,height//2, 50, t)
        return
    
    ## une ligne brisée pour les autres chiffres,
    #  mais ici, on dessine juste un point de cette ligne brisée
    if t < 200 :
        # 1er trait horizontal de longueur 200 : (50,H/2) -> (250,H/2)
        pygame.draw.circle(screen, BLANC, (50+t, height//2), 4) # un gros point d'épaisseur 8px
        return
    elif t < 300 and chiffre >= 2 :
        # si  200 <= t < 300  ( chiffre = 2 ou 3 )
        # 2e trait vertical de longueur 100 : (250, h/2) -> (250, H/2 - 100)
        pygame.draw.circle(screen, BLANC, (250, height//2 - (t-200)), 4) # 1 point de 8px
        return
    elif chiffre == 3 :
        # dernier cas : t varie de 300 à 500  (chiffre = 3)
        # 3e trait oblique de vect.dir(-1, 0.5) : (250, H/2 - 100) -> (50,H/2)  
        pygame.draw.circle(screen, BLANC, (250 - (t-300), height//2 - 100 + (t-300)//2), 4)


def ecrireTexteRose(ecran : pygame.Surface, texte : str, x :int, y : int) -> None:
    etiquette = myfont.render(texte , True, ROSE)
    ecran.blit(etiquette, (x,y))


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


### Animation @60 fps :   ce même nombre => langage Shadoks (GA, BU, ZO, MEU)
# Initialisation de pygame
pygame.init()
width  = 300
height = 250
#on crée un écran Pygame (de type Surface .. ou plus exactement pygame.Surface)
screen = pygame.display.set_mode( ( width, height) )
myfont = pygame.font.SysFont("monospace", 26)

# Chaque chiffre du tableau nbBase4[] est illustré par un dessin et un son
# .. puis il est supprimé du tableau, et on passe au chiffre suivant.
# La boucle de l'animation est donc   "while tabBase4"  [ au lieu de l'habituel while(True) ]
# (l'animation dure tant qu'il reste des chiffres ds le tableau)

# Puis t est un entier allant de 0 à 500 (t = temps), t est utilisé pour faire 
# varier l'image. lorsque t atteint 500 on passe au chiffre suivant.

t = 0
while tabBase4:
    fermerSiOnAppuieSurLaCroix()

    # Si t=0, c'est le signal pour prendre un nouveau chiffre
    if t == 0 :
        # on récupère ce chiffre (le 1er chiffre de la liste)
        chiffre = int(tabBase4[0])
        # on nettoie l'écran (en le remplissant entièrement de noir)
        screen.fill(NOIR)
        # on convertit le chiffre : base4 => GA, BU, ZO ou MEU (grâce au tableau shadok[])
        motShadok = shadok[chiffre]       
        # on l'écrit en rose à l'écran
        ecrireTexteRose(screen, motShadok , width//2 - 25, 75 + height//2)
        # on joue le son du fichier : GA.wav, BU.wav, ZO.wav ou MEU.wav
        playsound(motShadok +'.wav')
           
    ### ici, le coeur de l'animation : le dessin point par point !!
    # On ne dessine qu'un seul point mais comme les points précédents restent à
    # l'écran, ainsi on obtient une forme géométrique à la fin (rond, trait, triangle)
    dessinShadok(screen,chiffre,t)
    
    # la vitesse d'animation (framerate) : 60 frames per second
    pygame.time.Clock().tick(60)
    
    # on fait évoluer la variable de l'animation
    t += 2
    
    #Si t est au maximum, alors on supprime le chiffre (pour passer au suivant)
    if t >= 500 :
        tabBase4 = tabBase4[1:]
        t = 0  

    pygame.display.flip() # juste avant la fin, on actualise l'affichage


### Fin de l'animation .. et du programme
pygame.quit()