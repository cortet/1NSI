# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 18:15:10 2020

@author: SOPHIE
"""

from random import *

def fabrique(n):
    '''
    Fabrique une liste de n éléments en insérant un élément au hasard entre 1 et n
    @params : nombre d'élément à fabriquer
    @return : une liste de n éléments non trié
    '''
    liste = []
    for k in range(n):
        liste.append(randint(0,n))
    return liste

def recherche(liste, element) :
    i=0
    while  i<len(liste) and liste[i]!=element:
        i += 1
    if (i<len(liste) and liste[i]==element):
        return True
    else : return False

def recherche2(liste, element):
    i=0
    trouve=False
    while i<len(liste) and not trouve:
        if liste[i]==element:
            trouve=True
            break
        i = i + 1
    return trouve
     

assert recherche2([1,2,3],3)==True
assert recherche2([1],1)==True
assert recherche2([1,2,3],4)==False
assert recherche2([],1)==False