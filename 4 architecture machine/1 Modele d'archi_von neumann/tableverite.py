# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:06:15 2019

@author: SOPHIE
"""

def nand(a,b):
    if a==0:
        return 1
    if b==0:
        return 1
    return 0

def table2(f):
    print("a","b", "f(a,b)")
    for a in range(2):
        for b in range(2):
            print(a,b,f(a,b))

def non(a):
    return nand(a,a)

def et(a,b) :
    return non(nand(a,b))

def ou(a,b):
    return nand(non(a),non(b))