# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 09:45:35 2021

@author: Mme FAUGERAS
"""

"""
Question 1 : modéliser les données
"""
exemple = [('Vervier', 212), ('Côtes de Sart',543),('Stavelot', 317), ('Trois-Ponts', 251), ('Vielsalm', 361), ('Trois vierges', 479)]


"""
Question 2 : Points le plus haut
"""

def point_le_plus_haut(etapes):
    """
    @params : Etapes est une liste de tuples (points, altitude)
    @Returns : Le point le plus haut
    """
    le_plus_haut, altitude_max = etapes[0]
    for (point, altitude) in etapes :
        if altitude > altitude_max :
            altitude_max = altitude
            le_plus_haut = point
    return le_plus_haut

assert (point_le_plus_haut(exemple)=='Côtes de Sart')

"""
Question 3 : Points le plus haut
"""
exemple_altitude = [212,543,317,251,361, 479, 504, 319, 417, 499, 294, 370, 321, 414, 379]

def nombre_de_descentes(liste_altitudes):
    """
    @params : liste_altitudes est une liste de nombres
    @returns : le nombre d'occurrences
    """
    compteur = 0
    for i in range(1, len(liste_altitudes)):
        if liste_altitudes[i-1] > liste_altitudes[i]:
            compteur = compteur +1
    return compteur

assert(nombre_de_descentes(exemple_altitude))==6