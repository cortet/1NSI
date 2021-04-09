# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 23:22:16 2020

@author: SOPHIE
"""

n=int(input("Veuillez saisir un entier : " ))
if type(n)==int and n>=0 :
    p=1
    while n>0 :
        p=2*p
        n=n-1
    print (p)
else :
    print (" Impossible ")
