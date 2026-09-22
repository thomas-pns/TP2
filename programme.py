# -*- coding: utf-8 -*-
"""
Header
Objectifs du fichier :
    Créer un analyseur syntaxique basé sur un automate.

Par :
    Thomas CHASSANIS PONS et Camil BOUZIRI

Réalisé le 22/09/2026

ToDo List:
    Ajouter de nouveaux mots au ductionnaire.
"""
import sys
from typing import Dict, List, Tuple
import fonctions 


#Entrée de la phrase par l'utilisateur et éclatement pour vérification du nombre de mots.
phrase = input("Entrez une phrase (7 mots maximum) > ").strip()

print("Votre phrase est :", phrase)

#Phrase de conclusion
syntaxe = fonctions.init(phrase)
if syntaxe:
    print("La phrase est syntaxiquement correcte.") 
else:
    print("Erreur : La phrase n'est pas syntaxiquement correct.")

