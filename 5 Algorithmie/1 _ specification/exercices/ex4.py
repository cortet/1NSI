# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 16:02:14 2020

@author: SOPHIE
"""

#import math

def aire(a,b):
    """renvoie l'aire d'un rectangle dont les 2 côtés adjacents sont passés en paramètres
    Paramètres d'entrée : 
        a -> int ou decimal : côté
        b -> int ou decimal : côté adjacent
    Paramètres de sortie : retourne --> none
    """
    COEFFICIENT=10
    aire_rectangle=a*b*COEFFICIENT**2
    print("L'aire d'un rectangle de mesure",a,"et",b,"qui subit un agrandissement de coefficient",COEFFICIENT,"est",aire_rectangle)

#volume d'un parallélépipède de coté a,b,c qui subit un agrandissement de coefficient d
def volume(a,b,c,d):
    """renvoie le volume d'un parallépipède dont les 2 côtés adjacents sont passés en paramètres
    Paramètres d'entrée : 
        a -> int ou decimal : côté
        b -> int ou decimal : côté adjacent
        c -> int ou decimal : hauteur
        d -> Coefficient multiplicateur
    Paramètres de sortie : retourne --> volume du parallépipède doté d'un cef multiplicateur
    """
    COEFFICIENT=d
	return(a*b*c*COEFFICIENT**3)