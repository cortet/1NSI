# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 22:23:05 2019

@author: Sophie
"""

def tarifA(nbEntree):
    return nbEntree*5.25
    
    
def tarifB(nbEntree):
    return 12+nbEntree*3.5

i=0
while tarifA(i)<tarifB(i):
    i+=1
print("Le tarif B est plus avantageux au bout de ", i, " entrées.")
    