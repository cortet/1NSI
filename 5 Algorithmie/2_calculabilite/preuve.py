# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 23:22:41 2020

@author: SOPHIE
"""

n=input("Veuillez saisir un entier : " )
if type(n)==int and n>=0 :
    k=1
    f=1
    while k<=n :
        f=f*k
        k=k+1
    print(f)
else :
    print (" Impossible ")
    
    
