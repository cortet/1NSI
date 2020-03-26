# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:30:13 2019

@author: Sophie
"""

profondeur = 1
prix=100
while prix < 700:
    prix=prix+20
    profondeur = profondeur + 1
print("La profondeur maximal atteinte est de ", profondeur," pour un prix de ", prix)