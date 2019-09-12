from Conf.database_management import DatabaseManagement # interet d import databasemanagement ?
from Conf.menu import Menu # import de la classe menu


class Main:

    def __init__(self):
        self.engine()

    def engine():
        # Avec méthode statique
        Menu.Main_menu() # ne sais plus l utilite

        choix = self.input_menu("") # appel de la methode input_menu de la classe Menu (static method?)

        if choix == '1':
            Menu.show_categories()
        elif choix == '2':
            Menu.show_substitutes()
        return choix # retourne le resultat de la valeur 1 ou 2


    # besoin explications
    def show_input(self, question, entier = False):
        resultat = input(question)

        if resultat = "Q":
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



    show_db = DatabaseManagement()  # import de la classe databasemanagement
    interface = Menu() # creation de la classe Menu avec la variable interface
    main_home = interface.Main_Menu(db) # pourquoi le db en parametre ?

    if main_home == '1':
        category_id = interface.display_products_of_category() # a travailler
        print(category_id)
        show_db.show_products_db(category_id) # a travailler

    if main_home == '2':
        sub = interface.substitut_choice() # a travailler
        print(sub)
        show_db.show_favoris() # a travailler
