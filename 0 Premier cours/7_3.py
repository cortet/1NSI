# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:38:54 2019

@author: Sophie
"""
import random

nombreAdeviner = random.randint(1,100)
nombreChoisi = 0
nombreEssai=0

while (nombreChoisi != nombreAdeviner) and (nombreEssai<=5) :
    nombreChoisi = int(input("Entrez un nombre entre 1 et 100 : "))
    nombreEssai +=1
    if nombreChoisi < nombreAdeviner :
        print("trop petit !")
    elif nombreChoisi > nombreAdeviner:
        print("trop grand !")

print("Vous avez fait ",nombreEssai," essais")
print("Le nombre à deviner était : ",nombreAdeviner)