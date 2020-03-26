# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 21:56:19 2019

@author: Sophie
"""
#fonction qui prend en paramètre une durée exprimée en année
#calcule la population apres cette durée

def population(duree) :
    pop = 3000
    for i in range(1,duree+1):
        pop = pop*0.98
    return pop

popu=3000
duree = 0
while popu > 1500:
    popu=popu*0.98
    duree +=1
print(duree)