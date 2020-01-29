#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

import util
from carte import Carte
from labyrinthe import Labyrinthe

# On vérifie si une sauvegarde existe
backup = util.read_backup()

if backup is None:
    print("Salut ! Prêt pour une nouvelle partie ? ;-)")
    # On charge les cartes existantes
    cartes = []
    for nom_fichier in os.listdir("cartes"):
        if nom_fichier.endswith(".txt"):
            chemin = os.path.join("cartes", nom_fichier)
            nom_carte = nom_fichier[:-3].lower()
            with open(chemin, "r") as fichier:
                contenu = fichier.read()
                # Création d'une carte, à compléter
                carte = Carte(contenu, nom_fichier)
                cartes.append(carte)

    # On affiche les cartes existantes
    print("Labyrinthes existants :")
    for i, carte in enumerate(cartes):
        print("  {} - {}".format(i + 1, carte.nom))

    # ... Complétez le programme ...
    numero_labyrinthe = 0
    while numero_labyrinthe <= 0:
        numero_labyrinthe = input("Entre un numéro de labyrinthe pour commencer à jouer : ")
        try:
            numero_labyrinthe = int(numero_labyrinthe)
            if (numero_labyrinthe > len(cartes)) :
                print("Numéro de labyrinthe non valide.")
                numero_labyrinthe = 0
        except:
            print("Numéro de labyrinthe non valide.")
            numero_labyrinthe = 0

    # Affichage des consignes et but du jeu
    print(util.but_du_jeu)
    util.afficher_consignes()

    # Création du labyrinthe
    index_labyrinthe = (numero_labyrinthe-1)
    carte_a_afficher = cartes[index_labyrinthe]
    Lab = Labyrinthe(cartes[index_labyrinthe].contenu)
else:
    # Si une partie a été sauvegardée
    print("Hey ! Te revoilà :-)\nReprenons la partie là où nous l'avions laissée...")
    Lab = backup
    carte_a_afficher = Carte(Lab.chaine_grille_actuelle())

# Génération de la vue du labyrinte sélectionnée ou correspondant à la sauvegarde
print("\n")
carte_a_afficher.generer_vue_labyrinthe()
is_playing = True
success = False

while is_playing:
    # On demande à l'utilisateur de saisir un déplacement
    # il peut aussi saisir "q" pour quitter le jeu
    commande = input('>>> Saisis un déplacement (ou "q") : ')
    try:
        commande = str(commande).upper()
    except:
        print("Saisis un déplacement valide")
        commande = None

    if util.verif_input_saisi(commande) == True:
        if commande[0] == 'Q':
            is_playing = False
        else:
            reponse = Lab.deplacer_robot(commande)
            if reponse == 'success':
                is_playing = False
                success = True
                util.supprimer_la_partie() # La partie est terminée, on supprime le contenu du fichier de sauvegarde
            else:
                util.sauvegarder_la_partie(Lab) # On enregistre la partie
    else:
        print("La commande n\'est pas valide. Pour rappel : ")
        util.afficher_consignes()


if is_playing == False and success == False:
    print("Votre partie a été sauvegardée. A bientôt :-)")
elif is_playing == False and success == True:
    print("Bravo ! Tu as trouvé la sortie du labyrinthe !!!\nA bientôt :-)")