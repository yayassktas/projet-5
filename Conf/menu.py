"""menu creation script"""
# -*- PipEnv -*-
# -*- coding: Utf-8 -*-
from Conf.database_management import DatabaseManagement as db
from .constantes import CATEGORY_LIST, PAGE_SIZE

class Menu:
    """method displaying the main menu of choice"""

    @staticmethod
    def Main_Menu():
        """main menu class creation"""
        print("-" * 50)
        print("MENU PRINCIPAL")
        print("-" * 50)
        print("1 - Afficher les categories")
        print("2 - Afficher les produits substituts sauvegardés")
        print("3 - Réinitialisation de la BDD")
        print("4 - Quitter le program ?")

    @staticmethod
    def category_menu():
        """displays products of the category"""
        print("-" * 50)
        print("CHOIX DE LA CATEGORIE")
        print("-" * 50)

    @staticmethod
    def print_substituts():
        """substitute display menu"""
        print("-" * 50)
        print("AFFICHAGE DES SUBSTITUTS")
        print("-" * 50)

    @staticmethod
    def display_products():
        """displays a list of 50 products"""
        print("-" * 50)
        print("CHOIX DU PRODUIT")
        print("-" * 50)

    @staticmethod
    def display_product():
        """displays a list of 50 products"""
        print("-" * 50)
        print("VOICI LE PRODUIT CHOISI")
        print("-" * 50)

    @staticmethod
    def substitut_choice():
        """display of substitute choices"""
        print("-" * 50)
        print("choix du substitut")
        print("-" * 50)

    @staticmethod
    def confirmation_substitut():
        """input method if pressed on 1, displays the categories
            if pressing 2 displays the substitutes """
        print("-" * 50)
        print("produit enregistrer")
        print("-" * 50)

    @staticmethod
    def input_menu():
        """the user enters a number corresponding to a category input"""
        r = input()
        return r

    @staticmethod
    def choice_of_the_category():
        """input of selection category"""
        user_answer = (input(":"))
        return user_answer

    @staticmethod
    def choice_of_the_products():
        """choice of input product"""
        user_answer = input("Quelle produit choisissez-vous?")
        return user_answer

    @staticmethod
    def insertfavori():
        """"ask which product to save"""
        user_answer = input("Quelle produit a sauvegarder?")
        return user_answer

    @staticmethod
    def importfood():
        """import of openfactfood data"""
        user_answer = input("voulez vous importer les donnees openfactfood")
        InsertDb.insert_categories()
        return user_answer

    @staticmethod
    def confirmation_sauvegarde():
        """choice of input product"""
        user_answer = input("voulez vous sauvegarder?")
        # InsertDb.insert_favori()
        return user_answer

    @staticmethod
    def back_to_menu():
        """method for returning to the main menu input"""
        user_answer = (input("Que voulez-vous faire? \n 1-Revenir au menu principal \n 2-Sauvegarder un substitut?"))
        return user_answer

    @staticmethod
    def back_to_fav():
        """method to return to the main menu"""
        user_answer = (input("appuyer sur entree pour revenir au menu principal"))
        return user_answer
