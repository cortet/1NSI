# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:05:33 2021

@author: SOPHIE
"""

import csv
def depuis_csv(nom_fichier_csv):
    """
    Crée une liste de dictionnaires, un par ligne.
    La 1ère ligne du fichier csv est considérée comme la ligne des noms des champs
    """
    lecteur = csv.DictReader(open(nom_fichier_csv,'r')) 
    return [dict(ligne) for ligne in lecteur]

def vers_csv(nom_table, ordre_cols):
    """
    Exporte une liste de dictionnaires sous forme d'un
    fichier csv. On rentre le nom de la table sous forme de chaîne.
    On donne l'ordre des colonnes sous la forme d'une liste d'attributs.
    >>> vers_csv('Groupe1', ordre_cols=['Nom','Anglais','Info','Maths'])
    """
    with open(nom_table + '.csv', 'w') as fic_csv:
        ecrit = csv.DictWriter(fic_csv, fieldnames=ordre_cols)
        table = eval(nom_table)
        ecrit.writeheader() # pour le 1ère ligne
        for ligne in table:
            ecrit.writerow(ligne) # lignes ajoutées 1 à 1
    return None


def lire_note(liste_dico, nom, matiere):
    """
    fonction qui prend un nom d'élève et une matière en paramètre et retourne la note obtenue par l'élève
    @param entrée : liste_dico : liste de dictionnaire : contenant de l'information
                    nom : chaine de caractère : nom de l'éleve à rechercher
                    matiere : chaine de caractère : nom de la matière à rechercher
    Returns int : note obtenue
    """
    #Completer ici votre code
    pass
    
dico_eleve=depuis_csv("eleve.csv")
assert(lire_note(dico_eleve, "Joe", "Anglais")) == '17'
assert(lire_note(dico_eleve, "Max", "Info")) == '13'


                      