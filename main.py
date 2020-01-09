from Conf import DatabaseManagement
from Conf.menu import Menu
from Conf import InsertDb
from Conf import ApOpen





class Main:
    def __init__ (self):
        self.sql = InsertDb()
        self.db = DatabaseManagement()
        self.engine()

    def engine (self):
        statut = True
        while statut:

            # Avec méthode statique
            Menu.Main_Menu()  # affiche menu principal

            choix = Menu.input_menu()  # appel de la methode input_menu de la classe Menu (static method?)

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

                # affichage du produit choisi
                Menu.display_product()
                self.db.display_product_db(choix2)
                # affichage des potentiels substituts
                Menu.substitut_choice()
                self.db.show_substituts_db(category)

                # enregistrement du substitut
                choix3 = Menu.insertfavori()
                # print(category, choix2, choix3)
                # sauvegarde en base de donnees

                self.sql.insert_favori(choix2, choix3)
                Menu.confirmation_sauvegarde()
                print('produit enregistre')
                # confirmation sauvegarde du produit
                Menu.back_to_menu()
                if choix == '1':
                    continue

                elif choix == '2':
                    self.sql.insert_favori(choix2, choix3)
                else:
                    statut = False







            elif choix == '2':

                self.db.show_substituts_db(id)

            elif choix == '3':


                self.ini_db()
                Menu.back_to_menu()
            elif choix == '4':
                break

    # besoin explications
    def show_input (self, question, entier=False):
        resultat = input(question)

        if resultat == "Q":
            self.exit()

        # Si tu as besoin que ca soit un entier
        if (entier):
            # test du resultat
            if not isinstance(resultat, int):
                return false

        return resultat

    def ini_db(self):
        db = InsertDb()
        print('creation de la db')

        db.create_db()


        data_api = ApOpen()  # import de la class apopen de api_data
        print('insertion donnees')
        products_lists = data_api.get_products_list()  # recup toute les donnees appel de la methode get product list de la class apopen INTERET ?

        results = data_api.resultdata(products_lists)  # recup les donnees parses

          # creation de la class db avec insertdb
        db.insert_categories()
        db.insert_products(results)  # paramettre result ok
        print('import done')

# Tests
if __name__ == "__main__":
    # Lance le programme
    programme = Main()
