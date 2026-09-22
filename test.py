# -*- coding: utf-8 -*-
"""
Header
Objectifs du fichier :
    Utiliser un fichier json pour tous les mots.
Par :
    Thomas CHASSANIS PONS et Camil BOUZIRI

Réalisé le 22/09/2026

ToDo List:
    Ajouter de nouveaux mots au ductionnaire.
"""

use_json=False

import json

with open("dico.json") as json_file:
    items = json.load(json_file)

    print(items["dictionnaire"])