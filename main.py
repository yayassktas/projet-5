"""main file used to launch the program"""
from Conf import DatabaseManagement
from Conf.menu import Menu
from Conf import InsertDb
from Conf import ApOpen


class Main:
    """creation of the main class"""

    def __init__(self):
        self.sql = InsertDb()
        self.Database = DatabaseManagement()
        self.engine()

    # main menu display

    def engine(self):
        """main menu display"""
        statut = True
        while statut:

            # With static method

            Menu.Main_Menu()

            choix = Menu.input_menu()

            if choix == '1':

                Menu.category_menu()
                self.Database.display_category_db()

                category = Menu.choice_of_the_category()
                print(category)

                self.Database.display_products_db(category)
                choix2 = Menu.choice_of_the_products()
                print(choix2)

                Menu.display_product()
                self.Database.display_product_db(choix2)

                Menu.substitut_choice()
                self.Database.display_potential_substitut(category)

                choix3 = Menu.insertfavori()
                print(category, choix2, choix3)

                self.sql.insert_favori(choix2, choix3)
                Menu.confirmation_sauvegarde()
                print('produit enregistre')

                Menu.back_to_menu()
                if choix == '1':
                    continue

                elif choix == '2':
                    self.sql.insert_favori(choix2, choix3)
                else:
                    statut = False

            elif choix == '2':
                Menu.print_substituts()
                self.Database.show_substituts_db(id)
                Menu.back_to_fav()

            elif choix == '3':
                self.ini_db()
                Menu.back_to_menu()

            elif choix == '4':
                break

    def show_input(self, question, entier=False):
        """method waiting for user response"""
        resultat = input(question)

        if resultat == "Q":
            self.exit()

        if entier:

            if not isinstance(resultat, int):
                return false

        return resultat

    def ini_db(self):
        """db initialization method"""

        data_b = InsertDb()
        print('creation de la Database')

        data_b.create_db()

        data_api = ApOpen()
        print('insertion donnees')

        products_lists = data_api.get_products_list()

        results = data_api.resultdata(products_lists)

        data_b.insert_categories()
        data_b.insert_products(results)
        print('import done')


if __name__ == "__main__":
    program = Main()
