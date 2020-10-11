# -*- coding: utf-8 -*-
"""

LE BINAIRE ET L'HEXA

Created on Wed Apr 24 16:38:54 2019

@author: JEAN-PAUL GIARD
"""

"""
Partie I
for a in range(0, 300):
    abin = bin(a)
    longueur = len(abin[2:])
    print (a,"sécrit en binaire ",abin[2:]," sur ",longueur," bits")
   
"""


"""
Partie II
for a in range(0, 300):
    abin = hex(a)
    longueur = len(abin[2:])
    print (a,"sécrit en hexa ",abin[2:]," sur ",longueur," symboles")  
"""    
"""
Partie III
"""
for a in range(0, 300):
    abin = bin(a)
    ahex = hex(a)
    print (a,"sécrit en binaire ",abin[2:]," en hexa ",ahex[2:])

    
