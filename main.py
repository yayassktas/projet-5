from Conf.database_management import DatabaseManagement
from Conf.menu import Menu
from Conf.sql import InsertDb


class Main:
    def __init__(self):
        self.sql = InsertDb()
        self.db = DatabaseManagement()
        self.engine()


    def engine(self):
        # Avec méthode statique
        Menu.Main_Menu() # affiche menu principal


        choix = Menu.input_menu() # appel de la methode input_menu de la classe Menu (static method?)

        if choix == '1':

            Menu.category_menu()
            self.db.display_category_db()
            # affiche toutes les categories dispo
            category = Menu.choice_of_the_category()
            print(category)
            # affiche tout les produits de la categorie
            self.db.display_products_db(category)
            choix2 = Menu.choice_of_the_products()
            print(choix2)

            #affichage du produit choisi
            Menu.display_product()
            self.db.display_product_db(choix2)
            #affichage des potentiels substituts
            Menu.substitut_choice()
            self.db.show_substituts_db(category)
            #enregistrement du substitut
            choix3 = Menu.insertfavori()
            print(category, choix2, choix3)
            #sauvegarde en base de donnees
            self.sql.insert_favori(choix2, choix3)
            print('produit enregistre')
            #confirmation sauvegarde du produit
            Menu.back_to_menu()
            if choix == '1':
                Menu.category_menu()
            elif choix == '2':
                self.sql.insert_favori(choix2, choix3)

           





        elif choix == '2':
            #self.db.show_favoris()
            #fav = Menu.show_substitutes()
            #print(fav)
            self.db.show_substituts_db(id)
            Menu.back_to_menu()



    # besoin explications
    def show_input(self, question, entier = False):
        resultat = input(question)

        if resultat == "Q":
            self.exit()

        # Si tu as besoin que ca soit un entier
        if(entier):
            # test du resultat
            if not isinstance(resultat, int):
                return false

        return resultat


# Tests
if __name__ == "__main__":

    # Lance le programme
    programme = Main()
    #
    #
    #
    # show_db = DatabaseManagement()  # import de la classe databasemanagement
    # interface = Menu() # creation de la classe Menu avec la variable interface
    # main_home = interface.Main_Menu() # pourquoi le db en parametre ?
    #
    # if main_home == '1':
    #     category_id = interface.category_menu() # a travailler
    #     print(category_id)
    #     show_db.show_products_db(category_id) # a travailler
    #
    # if main_home == '2':
    #     sub = interface.substitut_choice() # a travailler
    #     print(sub)
    #     show_db.show_favoris() # a travailler
