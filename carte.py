#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-

"""Ce module contient la classe Carte."""

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, chaine, nom = None):
        """Constucteur de la class."""

        self.nom = nom
        self.contenu = chaine
        self.labyrinthe = self.creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        """Permet de redéfinir l'affichage de l'objet quand on tape directement son nom."""

        return "<Carte {}>".format(self.nom)

    def creer_labyrinthe_depuis_chaine(self, chaine):
        """Permet de créer une liste depuis une chaîne."""

        chaine_list = chaine.split("\n")
        return(chaine_list)
    
    def generer_vue_labyrinthe(self):
        """Permet d'afficher la représentation graphique
        de la carte du labyrinthe."""

        for val in self.labyrinthe:
            print(val)

        print("\n")