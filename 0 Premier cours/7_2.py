# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:34:50 2019

@author: Sophie
"""

import random
somme = 0
nombre = 0
while somme != 12:
    de1 = random.randint(1,6)
    de2 = random.randint(1,6)
    somme = de1 + de2
    nombre = nombre +1
print("il a fallu ", nombre, "tirages pour obtenir 12")