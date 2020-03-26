# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 16:13:40 2020

@author: SOPHIE
"""

def console_jeu_choix():
    """Fonction de menu de la console de jeu
    Paramètres d'entrée : none
    Paramètres de sortie : retourne --> choix
    """
    print("1 - jouer à la bataille navale")
    print("2 - jouer au puissance 4")
    print("3 - quitter")
    a=int(input("Taper votre choix 1 ou 2 ou 3:"))
    #Tant que l'utilisateur n'a pas choisi son menu correctement, on l'interroge
    while a!="1" or a!="2" or a!="3" :
        a=int(input("Taper votre choix :"))
    return(a)
