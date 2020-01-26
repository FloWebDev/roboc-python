#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-

"""Ce module contient les variables et
fonctions utiles au bon fonctionnement du jeu."""

import pickle

# Liste des commandes autorisées
commande_list = ['Q', 'N', 'E', 'S', 'O']
but_du_jeu = 'Le but du jeu : Tu es un robot (X) et tu dois sortir du labyrinthe en trouvant la porte de sortie (U).\nLes portes (.) sont tes amies, les obstacles tes ennemis (O).'

def afficher_consignes():
    print("Les commandes autorisées sont :\n- n(x) (Nord),\n- e(x) (Est),\n- s(x) (Sud),\n- o(x) (Ouest),\n- q (pour quitter le jeu)")
    print("Un déplacement peut contenir un second paramètre (x) (facultatif) pour le nombre de cases à avancer.")

def verif_input_saisi(commande):
    """Permet de vérifier que la combinaison de touche saisie
    par l'utilisateur est correcte."""

    verif = False
    commande = commande.upper() # On met en majuscules la commande pour éviter les soucis de casse
    try:
        commande = str(commande)
    except:
        verif = False
    else:
        if len(commande) == 0:
            verif = False
        elif len(commande) == 1:
            if commande in commande_list:
                verif = True
            else:
                verif = False
        else:
            try:
                int(commande[1:])
            except:
                verif = False
            else:
                if commande[0] in commande_list and commande[0] != 'Q' \
                    and int(commande[1:]) > 0:
                    verif = True
                else:
                    verif = False
    return verif


def read_backup():
    """Permet de lire et retourner une sauvegarde,
    ou à défaut de créer le fichier de sauvegarde et renvoyer une valeur None."""

    try:
        fichier = open('backup', 'rb')
    except FileNotFoundError:
        fichier = open('backup', 'wb')
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(None)
        fichier.close()
        fichier = open('backup', 'rb')
    finally:
        mon_depickler = pickle.Unpickler(fichier)
        backup = mon_depickler.load()
        fichier.close()
        return backup


def sauvegarder_la_partie(Labyrinthe):
    """Permet de sauvegarder une partie, c'est-à-dire la class
    Labyrinthe passé en param à un instant T (dans notre cas, après chaque déplacement)."""

    with open('backup', 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(Labyrinthe) # On enregistre la class Labyrinthe passée en param


def supprimer_la_partie():
    """Permet de supprimer le contenu du fichier de sauvegarde."""

    try:
        fichier = open('backup', 'wb')
    except FileNotFoundError:
        print('Aucune partie sauvegardée, aucune partie à supprimer.')
    else:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(None) # On écrase tout éventuel contenu du fichier
        fichier.close()