# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:57:58 2020

@author: SOPHIE
"""

import csv

def depuis_csv(nom_fichier_csv) -> list():
    """
    Crée une liste de dictionnaires, un par ligne.
    La 1ère ligne est considérée comme la ligne des noms de champs
    """
    lecteur = csv.DictReader(open(nom_fichier_csv,'r'),delimiter = ";")
    return [dict(ligne) for ligne in lecteur]

liste_nasa = depuis_csv("nasa.csv")
poids_max = 200 

# initialisations
cumul_poids = 0
cumul_valeur = 0
choix = []

# on trie la liste mercato par force décroissante  ATTENTION DIFFICULTE ELEVE
# CECI EST L'ETAPE CLE POUR QUALIFIER L'ALGORITHME DE GLOUTON
liste_nasa_ordo =sorted(liste_nasa, key=lambda d: d["valeur"], reverse=True)
print (liste_nasa_ordo)
# on balaye sequentiellement liste_nasa_ordo
for i in range(len(liste_nasa_ordo)):   
    # on accumule tant que cela ne va pas dépasser le budget Poids
    # et que l'on ne dépasse pas le nombre d'objet, fixé à 10 par nos contraintes
    if cumul_poids + float(liste_nasa_ordo[i]["poids"]) <= poids_max and len(choix)<10: 
        cumul_valeur += int(liste_nasa_ordo[i]["valeur"])  #calcul valeur gagnée
        choix.append(liste_nasa_ordo[i])             #complément liste des recrues
        cumul_poids += float(liste_nasa_ordo[i]["poids"])  #calcul poids "dépensées"

#Affichage du résultat
print ("somme des valeurs : ",cumul_valeur)
print ("nombre d'objet : ",len(choix))
print ("poids total : ",cumul_poids)
print ("\nliste des objets\n")
for i in range(len(choix)):
    print (choix[i]["objet"], choix[i]["valeur"],"poids", choix[i]["poids"])
