# -*- coding: utf-8 -*-

import csv
import folium

def CreationDico(lecture_csv):
    """
    Création d'un dictionnaire à partir du flux de lecture CSV.
    Le dictionnaire aura autant de clé que de colonne dans le flux CSV.
    Les clés reprennent les entetes de la première ligne du fichier CSV
    @Parameters : Lecture_csv -> Flux de lecture.
    @Returns : Dictionnaire.

    """
    dicoMonuments=[]
    for colonne in lecture_csv:
        dicoMonuments.append(dict(colonne))
    return dicoMonuments

def printUnMonuments(dico, attribut):
    """
    Affiche pour chaque ligne du dictionnaire nom de l'attribut et sa valeur
    sous la forme : Monument n° 73 monument_nom = Tours et remparts d'Aigues-Mortes
    @params : dico -> un dictionnaire : Le dictionnaire des monuments
              attribut -> str : une chaîne de caractère correspondant à l'une des entetes du dictionnaire
    @return : str : La chaine de caractère retravaillé
    """
    for i in range(len(dico)):
        print("Monument n°",int(dico[i]["monument_id"]),attribut,"=",dico[i][attribut])


def creer_carte(dico) :
    """
    Création d'une carte dans un fichier de type HTML à l'aide de la bibliothèque folium
    @params : -> un dictionnaire : Le dictionnaire des monuments
    @return : None
    """
    #Centrage de la carte sur la tour Eiffel :  48,8585238, 2,2939989
    c= folium.Map(location=[48.8585238, 2.2939989],zoom_start=12)
    #Parcours du dictionnaire des monuments pour récupérer le nom, la latitude et la longitude
    for i in range (len(dico)):
        nom_monument = dico[i]["monument_nom"]
        folium.Marker([dico[i]["monument_lat"],dico[i]["monument_lon"]],popup=nom_monument).add_to(c)
    c.save('maCarte4.html')

###########################################
#         Programme Princial
###########################################
    
#Création d'un flux de lecture vers le fichier passé en paramètre
fichier_csv = open('monuments_GPS.csv','r')
#Lecture du fichier CSV dans un flux CSV en fonction des entetes de la première ligne du CSV
lecture_csv = csv.DictReader(fichier_csv)
#Création de la struture de données Dictionnaire à partir des données du fichiers CSV
dicoMonuments=CreationDico(lecture_csv)

#Appel de la fonction permettant d'afficher un des attribut du dictionnaire passé en paramètre
#printUnMonuments(dicoMonuments,"monument_nom")

#Appel de la fonction de création de la carte avec le dictionnaire des monuments passés en paramètres
creer_carte(dicoMonuments)

#Fermeture du flux de lecture sur le fichier
fichier_csv.close()
