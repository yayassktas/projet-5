# -*- PipEnv -*-
# -*- coding: Utf-8 -*-



from Conf.database_management import DatabaseManagement as db
from .constantes import CATEGORY_LIST, PAGE_SIZE
#from .sql import *







class Menu:


# ---------------------------------------------------------------------------------------------------------
# methode print 


# methode affichant le menu principal de choix
    @staticmethod
    def Main_Menu():
        print("-" * 50)
        print("MENU PRINCIPAL")
        print("-" * 50)
        print("1 - Afficher les categories")
        print("2 - Afficher les produits substituts sauvegardés")
        print("3 - Réinitialisation de la BDD")
        print("4 - Quitte le programme ?")

     # affiche des produits de la category
    @staticmethod
    def category_menu():
        print("-" * 50)
        print("CHOIX DE LA CATEGORIE")
        print("-" * 50)

    # affiche une liste de 50 produits
    @staticmethod
    def display_products():
        print("-" * 50)
        print("CHOIX DU PRODUIT")
        print("-" * 50)

   # affiche une liste de 50 produits
    @staticmethod
    def display_product():
        print("-" * 50)
        print("VOICI LE PRODUIT CHOISI")
        print("-" * 50)


    @staticmethod
    def substitut_choice():
        print("-" * 50)
        print("choix du substitut")
        print("-" * 50)


    @staticmethod
    def confirmation_substitut():
        print("-" * 50)
        print("produit enregistrer")
        print("-" * 50)


#---------------------------------------------------------------------------------
#   methode input

 # methode input si appuis sur 1, affiche les categories si appui sur 2 affiche les substituts
    @staticmethod
    def input_menu():
        r = input()
        return r


    # l utilisateur rentre un numero correspondant a une category input
    @staticmethod
    def choice_of_the_category():
        user_answer = (input(":"))
        return user_answer

      # choix du produit input
    @staticmethod
    def choice_of_the_products():
        user_answer = input("Quelle produit choisissez-vous?")
        return user_answer

      # choix du produit input
    @staticmethod
    def insertfavori():
        user_answer = input("Quelle produit a sauvegarder?")
        #InsertDb.insert_favori()
        return user_answer


      # import des donnees openfactfood
    @staticmethod
    def importfood():
        user_answer = input("voulez vous importer les donnees openfactfood")
        InsertDb.insert_categories()
        return user_answer

     # choix du produit input
    @staticmethod
    def confirmation_sauvegarde():
        user_answer = input("voulez vous sauvegarder?")
        #InsertDb.insert_favori()
        return user_answer

     # methode permettant le retour au menu principal input
    @staticmethod
    def back_to_menu():
        user_answer = (input("Que voulez-vous faire? \n 1-Revenir au menu principal \n 2-Sauvegarder un substitut?"))
        return user_answer









