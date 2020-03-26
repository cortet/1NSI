# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:59:38 2020

@author: SOPHIE
"""

from math import cos, pi
 
def conversion_degre_radian(angle):
    """renvoie la conversion des données en radians
    
	Paramètres d'entrée : x -> int ou decimal : valeur de l'angle de degré à convertir
    Paramètres de sortie : retourne --> int ou float : valeur de l'angle en radian
    
	"""
    return(angle*pi/180)

def calcul_cosinus(angle):
     """renvoie le cosinus d'un angle
    
	Paramètres d'entrée : x -> int ou decimal : valeur de l'angle en radian
    Paramètres de sortie : retourne --> int ou float : cosinus en radian
    
	"""
    return(cos(conversion_degre_radian(angle)))
