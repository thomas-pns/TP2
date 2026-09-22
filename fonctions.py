# -*- coding: utf-8 -*-
"""
Header
Objectifs du fichier :
    Créer un analyseur syntaxique basé sur un automate.

Par :
    Thomas CHASSANIS PONS et Camil BOUZIRI

Réalisé le 22/09/2026

ToDo List: Générer les ; ou , collés aux mots, et non séparés par un espace.

tables_tranitions(mot) : fonction qui permet de connaitre la classe d'un mot
init(phrase) : fonction qui permet de vérifier si une phrase est correcte ou non
"""


import test


NOMS_CLASSES = {0: "article", 1: "adjectif", 2: "nom", 3: "verbe", 4: "nom propre", 5: "point"}

dictionnaire ={"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4, 
                   "mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1,
                   "bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5}

def tables_tranitions(mot): # cette fonction permet de connaitre la classe d'un mot
    """
    Retourne un tuple (bool, str) indiquant si le mot est reconnu et sa classe.
    """
    # print(test.use_json)
    

    if mot.lower() in dictionnaire:
        return (True, NOMS_CLASSES[dictionnaire[mot.lower()]], dictionnaire[mot.lower()])
    else:
        return (False, None, None)
    

def init(phrase):
    """
    Retourne True si la phrase est syntaxiquement correcte selon les chemins définis, sinon False.
    """
    #On pose ici le dictionnaire utilisé pour notre code (tout les chemin possible pour faire une phrase correcte)*
    
    chemins = [
        # Base article+nom+verbe (4 variantes)
        [0, 2, 3, 5],
        [0, 2, 1, 3, 5],
        [0, 1, 2, 3, 5],
        [0, 1, 2, 1, 3, 5],

        # Base article+nom+verbe+article+nom (16 variantes)
        [0, 2, 3, 0, 2, 5],
        [0, 2, 3, 0, 2, 1, 5],
        [0, 2, 3, 0, 1, 2, 5],
        [0, 2, 3, 0, 1, 2, 1, 5],
        [0, 2, 1, 3, 0, 2, 5],
        [0, 2, 1, 3, 0, 2, 1, 5],
        [0, 2, 1, 3, 0, 1, 2, 5],
        [0, 2, 1, 3, 0, 1, 2, 1, 5],
        [0, 1, 2, 3, 0, 2, 5],
        [0, 1, 2, 3, 0, 2, 1, 5],
        [0, 1, 2, 3, 0, 1, 2, 5],
        [0, 1, 2, 3, 0, 1, 2, 1, 5],
        [0, 1, 2, 1, 3, 0, 2, 5],
        [0, 1, 2, 1, 3, 0, 2, 1, 5],
        [0, 1, 2, 1, 3, 0, 1, 2, 5],
        [0, 1, 2, 1, 3, 0, 1, 2, 1, 5],

        # Base article+nom+verbe+nom propre (4 variantes)
        [0, 2, 3, 4, 5],
        [0, 2, 1, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 1, 3, 4, 5],

        # Base nom propre+verbe (1 variante)
        [4, 3, 5],

        # Base nom propre+verbe+article+nom (4 variantes)
        [4, 3, 0, 2, 5],
        [4, 3, 0, 2, 1, 5],
        [4, 3, 0, 1, 2, 5],
        [4, 3, 0, 1, 2, 1, 5],

        # Base nom propre+verbe+nom propre (1 variante)
        [4, 3, 4, 5],
    ]


    chemin_phrase=[]

    mots=phrase.split(" ")

    # ici on vérifie que la phrase se termine par un point, sinon on retourne une erreur
    if not mots[-1][-1] == ".":
        return "Erreur : la phrase doit se terminer par un point."
    else:
        mots[-1] = mots[-1][:-1]  # Supprimer le point final du dernier mot
        mots.append(".")  # Ajouter le point final comme un mot séparé

    # ici on traite chaque mot de la phrase pour vérifier s'il est reconnu par l'automate et pour construire le chemin de la phrase
    for mot in mots:
        transition = tables_tranitions(mot) # 0 : True ou False, 1 : classe du mot, 2 : code de la classe du mot
        if transition[0]:
            print("Le mot ",mot," est de la classe ",transition[1])
            chemin_phrase.append(transition[2])
        else:  
            print("Le mot ",mot," n'est pas reconnu par l'automate")
            break


    print("Le chemin de la phrase est :", chemin_phrase)
    return chemin_phrase in chemins #si le chamin de la phrase est dans les chemins possibles, alors la phrase est correcte, sinon elle est incorrecte


      

