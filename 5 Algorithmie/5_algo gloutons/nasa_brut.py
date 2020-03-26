# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:30:26 2019

@author: Sophie
"""

import csv
import itertools


def openFile(file, delimiter=None):
    """
    Crée une liste de dictionnaires, un par ligne.
    La 1ère ligne est considérée comme la ligne des noms de champs
    :param namefile: nom du fichier contenant les données des joueurs 1 ligne = 1 joueur
    :type namefile: str
    :return: retourne la liste des caractéristiques des joueurs
    :rtype: dictionnaire
    """
    if not delimiter:
        delimiter = ';'
    lecteur = csv.DictReader(open(file,'r'), delimiter=delimiter)
    return [dict(ligne) for ligne in lecteur]


def tri(table, attribut, decroit):
    """
    tri un dictionnaire, selon un critère passé en paramètre
    @param : table : dictionnaire à trier
             attribut : critère de tri
             decroit : sens ascendant ou descendant
    @return : retourne le dictionnaire trié
    """
    def critère(ligne):
        return ligne[attribut]
    return sorted(table, key=critère, reverse=decroit)

def sommeValeur(dico):
    force = 0
    for i in range(len(dico)):
        force += int(dico[i]["valeur"])
    return force

def listeObjet(dico):
    liste = ""
    for i in range(len(dico)):
        liste += dico[i]["objet"]+str("/")
    return (liste)

def sommePoids(dico):
    cout = 0
    for i in range(len(dico)):
        cout += float(dico[i]["poids"])
    return cout


    '''
    PROGRAMME PRINCIPAL
    
    note : 
        Il existe de nombreuses manière de coder la force brut.
        Il s'agit ci dessous de l'une de ces versions. 
    '''
dicoNasa=openFile("nasa.csv",";")
    
meilleur_valeur=0
meilleur_comb=""
meilleur_poids=0
poids_max = 200
    

for i in range(len(dicoNasa)):   
    for p in itertools.combinations(dicoNasa,i+1) :

        combinaison = listeObjet(p)
        valeurs = sommeValeur(p)
        poids = sommePoids(p)
        print(combinaison,' ',valeurs,' ',poids,'\n')
        ''''On ne garde que les combinaisons qui respectent les contraintes 
        dans notre cas : pas plus de 10 objets pour un poids inférieur à 200 
        et en maximisant la valeur
        '''
        if valeurs>meilleur_valeur and poids<=poids_max and len(p)<=10:
            # solution retenue si surpasse la meilleure
            meilleur_valeur = valeurs     # maj meilleure solution
            meilleur_comb = combinaison   # maj meilleure solution
            meilleur_poids = poids        # maj meilleure solution

print("La meilleure sélection est \n",meilleur_comb,"\n valeur = ",meilleur_valeur,"\n poids = ",meilleur_poids)