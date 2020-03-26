# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 17:57:23 2020

@author: SOPHIE
"""

def le_plus_grand(pokemons):
    grand=None
    taille_max=None
    for (nom,(taille,poids)) in pokemons.items():
        if taille_max is None or taille> taille_max:
            taille_max=taille
            grand=nom
    return (grand,taille_max)

def le_plus_leger(pokemons):
    leger=None
    poids_min=None
    for (nom,(taille,poids)) in pokemons.items():
        if poids_min is None or poids< poids_min:
            poids_min=poids
            leger=nom
    return (leger,poids_min)

exemple_pokemons = {
    'bulbizarre':(70,7),
    'herbizarre':(100,13),
    'abo':(200,7),
    'jungko':(170,52)
}

exemple_pokemons['dracofeu']=(50,6)

#fonction taille qui prend en paramètre un dictionnaire de pokemons ainsi que le nom d'un pokemon,
# et qui renvoie la taille de ce pokemon
def taille(dico,nom):
    """
    Renvoie la taille d'un pokemon
    @params : dico -> Dictionnaire : ensemble des pokemons. Structure : {'pokemon1',(taille,poids)}
              nom -> str : Nom du pokemon doit on veut connaître la taille
    @☺return : int -> Taille 
    """
    if nom in dico.keys():
        return dico[nom][0]

assert taille(exemple_pokemons,'abo')==200
assert taille(exemple_pokemons,'jungko')==170
assert taille(exemple_pokemons,'dracaufeu')==None