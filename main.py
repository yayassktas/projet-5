from Conf.database_management import DatabaseManagement
from Conf.menu import Menu

class Main:
    def __init__(self):

        self.db = DatabaseManagement()
        self.engine()


    def engine(self):
        # Avec méthode statique
        Menu.Main_Menu() # ne sais plus l utilite

        choix = Menu.input_menu() # appel de la methode input_menu de la classe Menu (static method?)

        if choix == '1':
            Menu.category_menu()
            self.db.display_category_db()
            category = Menu.choice_of_the_category()
            print(category)
            self.db.display_products_db(category)
        elif choix == '2':
            Menu.show_substitutes()



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
