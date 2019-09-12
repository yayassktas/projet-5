# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


from Conf import database_management
from Conf.database_management import DatabaseManagement
from Conf.constantes import MENU


MENU


class Menu:


# ---------------------------------------------------------------------------------------------------------
# methode print 

    @staticmethod
    def Main_Menu (self, db): # methode affichant le menu principal de choix 
        print("-" * 50)
        print("MENU PRINCIPAL")
        print("-" * 50)
        print("1 - Quel aliment souhaitez - vous remplacer ?")
        print("2 - Afficher les produits substituts sauvegardés")    
  
    @staticmethod    
    def display_products_of_category (data): # affiche des produits de la category
        print("-" * 50)
        print("CHOIX DE LA CATEGORIE")
        print("-" * 50)
    
    @staticmethod 
    def display_products(data): # affiche une liste de 50 produits 
        print("-" * 50)
        print("CHOIX DU PRODUIT")
        print("-" * 50)

    @staticmethod
    def substitut_choice (data):
        print("-" * 50)
        print("MENU SUBSTITUT")
        print("-" * 50)       


#---------------------------------------------------------------------------------
#   methode input

    @staticmethod
    def input_menu (self): # methode input si appuis sur 1, affiche les categories si appui sur 2 affiche les substituts
        r = input()
        if r == '1':
            db.show_category()
        elif r == '2':
            db.show_substituts_db()
        return r

    @staticmethod
    def choice_of_the_category (self): # l utilisateur rentre un numero correspondant a une category input
        user_answer = (input(":"))
        return user_answer


    @staticmethod
    def put_category (self): # affiche le message quelle category choisir input
        user_answer = input("Quelle catégorie choisissez-vous?")
        return user_answer


    @staticmethod
    def choice_of_the_products (self): # choix du produit input
        user_answer = input("Quelle produit choisissez-vous?")
        return user_answer


    @staticmethod
    def back_to_menu(data): # methode permettant le retour au menu principal input
        user_answer = (input("Que voulez-vous faire? \n 1-Revenir au menu principal \n 2-Sauvegarder un substitut?"))
        return user_answer








# def main():
#     db = DatabaseManagement()  # import de la class databasemanagement
#     interface = menu()
#     main_home = interface.display_choice(db)
#
#     if main_home == '1':
#         category_id = interface.category_choice()
#         print(category_id)
#         db.show_products_db(category_id)
#
#     if main_home == '2':
#         sub = interface.substitut_choice()
#         print(sub)
#         db.show_favoris()
#
#     # interface.select_choice()
#
#
# if __name__ == "__main__":
#     main()