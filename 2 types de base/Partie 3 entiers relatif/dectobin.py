# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 19:08:14 2019

@author: SOPHIE
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
 
def dec2bin(d,nb=0):
    """dec2bin(d,nb=0): conversion nombre entier positif ou nul -> chaîne binaire (si nb>0, complète à gauche par des zéros)"""
    if d==0:
        b="0"
    else:
        b=""
        while d!=0:
            b="01"[d&1]+b
            d=d>>1
    return b.zfill(nb)
 
# Exemple d'utilisation:
#print dec2bin(75)  # affiche: "1001011"
#print dec2bin(75,12)  # affiche: "000001001011" 