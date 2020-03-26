# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 23:23:07 2020

@author: SOPHIE
"""

def indice_maximum_liste(l):
    """
    Renvoie l'indice de la valeur maximum de la liste passée en paramètre
    @params : une liste -> list
    @return : -> entier : indice de la valeur maximum
    """
    #Traitement du cas de la liste vide
    if len(l)==0 : return None
    
    m=0 # initialisation de la variable m
    #Parcours de la liste passée en paramètre
    for i in range(len(l)):
        #Test pour conserver le max entre 2 valeurs
        if l[i]>l[m]:
            m=i
    #Retourne l'indice du max de la liste passée en paramètre
    return m

"""
Cas de tests
"""
#cas normal
assert indice_maximum_liste([1,2,4,3])==2
#cas faux
#assert indice_maximum_liste([1,2,3,4])==2
#cas limite : cas de la liste vide
assert indice_maximum_liste([])==None
#cas limite
assert indice_maximum_liste([1])==0
assert indice_maximum_liste([7,2,3])==0
assert indice_maximum_liste([2,3,4])==2
assert indice_maximum_liste([-3,-2,-7,-4])==1
#Cas limite : plusieurs maximums
val= indice_maximum_liste([3,2,3,1])
assert val==0 or val==2

#programme principal
l=[]
print(indice_maximum_liste(l))