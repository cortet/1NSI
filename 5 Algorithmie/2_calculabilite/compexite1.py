# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 22:32:12 2020

@author: SOPHIE
"""


def fonction1(n):
    a=0
    for _ in range(n):
        a=a+1

def fonction2(n):
    a=0
    for _ in range(n):
        a=a+1
    for _ in range(n):
        a=a+1
    
def fonction3(n):
    a=0
    for _ in range(n):
        for _ in range(n):
            a=a+1

from time import *
debut = perf_counter()
#code ici
fin = perf_counter()
print("temps passé : ".fin-debut)

def moyenne(uneListe):
    """
    Calcul de la moyenne d'une liste de nombres passée en argument
    """
    #Calcul de la somme des éléments de la liste
    somme =0                        #initialisation
    for elt in uneListe:            #Boucle sur les éléments de la liste
        somme = somme + elt         # ajout de l'élément courant
    #Division de la somme par le nombre de termes
    return somme/len(uneListe)
    