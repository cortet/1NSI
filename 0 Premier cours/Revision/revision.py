# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
"""
import math

rayon = float(input("Entrez le rayon du cercle : "))
print("le périmètre du cercle est : ", 2*math.pi*rayon)
print("l'aire du cercle est de : ", math.pi*rayon**2)
"""
"""
myst  = float(input("Entrez le chiffre mystère à compter : "))
nbEntier = 0
for entier in range(10, 100) :
    unite = entier % 10
    dizaine = entier // 10
    if unite == myst or dizaine == myst :
        nbEntier = nbEntier + 1
print(nbEntier)
"""

age = int(input("Quel est ton âge ?")) # par exemple 18
estEtudiant = input("Es tu étudiant ?") # par exemple True
estChomeur = input("Es tu chômeur ?")
if (age<16 or estEtudiant=="oui" or estChomeur=="oui"):
    prix = 4.5
else : prix = 6.5
print (prix)