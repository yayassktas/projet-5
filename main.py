# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


from db.database_management import DatabaseManagement

MENU = [
    "Quel aliment souhaitez-vous remplacer ?",
    "Retrouver les aliments substitués."
]


class menu:

    def __init__ (self):
        pass

    def display_choice (self, db):
        print("-" * 50)
        print("MENU PRINCIPAL")
        print("-" * 50)
        print("1 - Quel aliment souhaitez - vous remplacer ?")
        print("2 - Afficher les produits substituts sauvegardés")

        r = input()
        if r == '1':
            db.show_category()
        elif r == '2':
            db.show_substituts_db()
        return r

    def select_choice (self):
        user_answer = (input(":"))
        return user_answer

    def category_choice (data):
        print("-" * 50)
        print("CHOIX DE LA CATEGORIE")
        print("-" * 50)
        user_answer = input("Quelle catégorie choisissez-vous?")

        return user_answer

    def product_choice (data):
        print("-" * 50)
        print("CHOIX DU PRODUIT")
        print("-" * 50)
        user_answer = input("Quelle produit choisissez-vous?")

        return user_answer

    def substitut_choice(data):
        print("-" * 50)
        print("MENU SUBSTITUT")
        print("-" * 50)
        user_answer = (input("Que voulez-vous faire? \n 1-Revenir au menu principal \n 2-Sauvegarder un substitut?"))

        return user_answer


def main():
    db = DatabaseManagement()  # import de la class databasemanagement
    interface = menu()
    r = interface.display_choice(db)

    if r == '1':
        category_id = interface.category_choice()
        print(category_id)
        db.show_products_db(category_id)

    if r == '2':
        sub = interface.substitut_choice()
        print(sub)
        db.show_favoris()

    # interface.select_choice()


if __name__ == "__main__":
    main()
