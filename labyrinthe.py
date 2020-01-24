#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-

"""Ce module contient la classe Labyrinthe."""

from carte import Carte

class Labyrinthe:

    """Classe représentant un labyrinthe.

    Permet d'obtenir le labyrinte actualisé par la dernière position
    du robot dans le jeu.
    
    """

    def __init__(self, str_labyrinthe):
        """Constructeur de la class Labyrinthe
        permettant d'initialiser les informations de la class."""

        self.robot = 'X'
        self.obstacle = 'O'
        self.porte = "."
        self.passage = " "
        self.sortie = "U"
        self.grille = {} # grille associée au labyrinthe d'origine
        self.grille_actuelle = {} # grille actualisée par la nouvelle position du robot
        self.position_robot = str() # position du robot d'origine
        self.position_robot_actuelle = str() # position actualisée du robot

        self.generer_grille(str_labyrinthe) 

    def generer_grille(self, str_labyrinthe):
        """Permet de générer une grille coordonnées/valeur
        depuis la chaîne de caractères du Labyrinthe."""

        grille = {}
        ligne_list = str_labyrinthe.split("\n")
        for ligne, valLigne in enumerate(ligne_list):
            for col, valCol in enumerate(valLigne):
                grille[str(ligne) + '-' + str(col)] = valCol
                if valCol == 'X':
                    self.position_robot = str(ligne) + '-' + str(col)
        self.grille = grille


    def deplacer_robot(self, commande):
        """Permet de déplacer le robot, avertir la présence d'un obstacle
        et prévenir lorsque le robot a trouvé la sortie."""
        
        commande = commande.upper()
        if(len(commande) == 2):
            axe = str(commande[0])
            nbr = int(commande[1])
        else:
            axe = str(commande[0])
            nbr = 1

        # Gestion des déplacements
        # on bouble autant de fois que demandé en second paramètre de la commande (= nbr)
        i = 1
        while i <= nbr:
            nouvelle_position_robot = self.verifier_deplacement(axe)
            if nouvelle_position_robot and nouvelle_position_robot != 'success':
                self.mise_a_jour_grille(nouvelle_position_robot) # Mise à jour de la grille avec la nouvelle position du robot
                nouvelle_chaine = self.chaine_grille_actuelle()
                nouvelle_carte = Carte(nouvelle_chaine)
                nouvelle_carte.generer_vue_labyrinthe() # Affichage de la nouvelle carte à jour des déplacements
                self.position_robot_actuelle = nouvelle_position_robot
            elif (nouvelle_position_robot == 'success'):
                return 'success'
            else:
                print("Déplacement impossible ! Vous avez rencontré un obstacle !")
                break # On stoppe la boucle
            i += 1 # on incrémente i pour ne pas finir dans une boucle infinie ;-)
        
    def verifier_deplacement(self, axe):
        """Permet de vérifier si le déplacement unitaire (1 par 1) est possible, 
        selon un ensemble de règles définies."""

        if len(self.position_robot_actuelle) == 0:
            position_robot_split = self.position_robot.split('-')
        else:
            position_robot_split = self.position_robot_actuelle.split('-')

        # Direction Nord
        if axe == 'N':
            nouvelle_position_robot = str((int(position_robot_split[0]) - 1)) + '-' + position_robot_split[1]
            if nouvelle_position_robot in self.grille and self.grille[nouvelle_position_robot] != self.obstacle:
                if self.grille[nouvelle_position_robot] != self.sortie:
                    return nouvelle_position_robot
                else:
                    return 'success'
            else:
                return False
        # Direction Sud
        elif axe == 'S':
            nouvelle_position_robot = str((int(position_robot_split[0]) + 1)) + '-' + position_robot_split[1]
            if nouvelle_position_robot in self.grille and self.grille[nouvelle_position_robot] != self.obstacle:
                if self.grille[nouvelle_position_robot] != self.sortie:
                    return nouvelle_position_robot
                else:
                    return 'success'
            else:
                return False
        # Direction Est
        elif axe == 'E':
            nouvelle_position_robot = position_robot_split[0] + '-' + str((int(position_robot_split[1]) + 1))
            if nouvelle_position_robot in self.grille and self.grille[nouvelle_position_robot] != self.obstacle:
                if self.grille[nouvelle_position_robot] != self.sortie:
                    return nouvelle_position_robot
                else:
                    return 'success'
            else:
                return False
        # Direction Ouest
        elif axe == 'O':
            nouvelle_position_robot = position_robot_split[0] + '-' + str((int(position_robot_split[1]) - 1))
            if nouvelle_position_robot in self.grille and self.grille[nouvelle_position_robot] != self.obstacle:
                if self.grille[nouvelle_position_robot] != self.sortie:
                    return nouvelle_position_robot
                else:
                    return 'success'
            else:
                return False


    def mise_a_jour_grille(self, nouvelle_position_robot):
        """Permet de mettre à jour la grille et la position du robot."""

        if len(self.grille_actuelle) == 0:
            self.grille_actuelle = dict(self.grille) # on copie la grille initiale

        if len(self.position_robot_actuelle) == 0:
            self.position_robot_actuelle = str(self.position_robot) # on copie la valeur de la position

        if self.grille[self.position_robot_actuelle] == self.porte:
            self.grille_actuelle[self.position_robot_actuelle] = self.porte # On réaffiche la porte
        else:
            self.grille_actuelle[self.position_robot_actuelle] = self.passage # On laisse un espace vide là où le robot se situé initialement

        self.grille_actuelle[nouvelle_position_robot] = self.robot # On place le robot sur sa nouvelle position


    def chaine_grille_actuelle(self):
        """Permet d'obtenir la chaîne Labyrinthe depuis la grille actuelle,
        c'est-à-dire depuis la grille à jour de la dernière position.
        
        Utile pour instancier par la suite la clas Carte qui se chargera de l'affichage du Labyrinthe
        en fonction de la chaîne donnée au construct de cette class
        
        """

        chaine = str()
        ref = '0'
        for key, valeur in self.grille_actuelle.items():
            split_key = key.split('-')
            if split_key[0] != ref and int(split_key[0]) < len(self.grille_actuelle):
                chaine += "\n"
                ref = split_key[0]
            chaine += valeur
        
        return chaine