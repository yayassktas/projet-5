# -*- PipEnv -*-
# -*- coding: Utf-8 -*-
# import Conf.constantes as conf

import mysql.connector
# from api_data import DatabaseManagement
from api_data import ApOpen
# import constantes
from constantes import *


# from .constantes import *


class InsertDb:  # Classe permettant les inserts dans les tables categories products de la db openfood

    def __init__(self):  # methode de connection a la db sql

        self.m_db = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST,
                                            database=DATABASE)  # assigne a db mysql.connector id

        self.m_cursor = self.m_db.cursor()

    def insert_category(self, name):  # methode permettant l insert des donnees dans la table category. methode ok fonctionne
        try:
            sql = "INSERT INTO category (name) VALUES ('{}')".format(str(name))
            self.m_cursor.execute(sql)
            self.m_db.commit()
        # print(self.m_cursor)
        except ValueError:
            pass

    def insert_categories(self):
        for category in CATEGORY_LIST:
            self.insert_category(category)


    def insert_product(self, a, b, c, d, e, f):  # methode permettant les inserts dans la table product
        try:
            sql = "INSERT INTO products (product_name, description, store, nutri_score, url_product, " \
                  "category_id) VALUES ('{}', '{}', '{}', '{}', '{}', {})".format(a, b, c, d, e, f)
            self.m_cursor.execute(sql)
            self.m_db.commit()
        except ValueError:
            pass

    def insert_products(self, products):
        try:

            sql = "select * from category;"
            self.m_cursor.execute(sql)
            categories = self.m_cursor.fetchall()
            # je parcours les produits pour trouver l'id de la catégorie correspondante
            for product in products:

                # cette variable contiendra l'id de la catégorie trouvée du produit en cours (de la boucle)
                cat_id = 0
                # je parcours les catégories pour comparer leurs nom avec celui du produit (de la boucle)
                for category in categories:
                    # Je compare le nom de la catégorie avec le nom de la catégorie DU PRODUIT
                    if category[1] == product[6].lower():
                        #print (category[1])
                        # si les 2 noms sont similaires, alors je défini l'id de la catégorie dans ma variable finale
                        cat_id = category[0] # probleme les nom d id sont en majuscule
                        self.insert_product(product[1][0:150], product[2], product[3], product[4], product[5], cat_id)
            self.m_db.commit()
        except ValueError:
            pass

    #  for id in products:
    # self.insert_product(a, b, c, d, e, f, g)

    def insert_favori (self):
        try:
            sql = "INSERT INTO substituts (product_id, substitut_id) VALUES ({}, '{}')".format(id, str(name))
            self.m_cursor.execute(sql)
            self.m_cursor.commit()
        except ValueError:
            pass


def main ():
    data_api = ApOpen()  # import de la class apopen de api_data
    products_lists = data_api.get_products_list()  # recup toute les donnees appel de la methode get product list de la class apopen INTERET ?
    results = data_api.resultdata(products_lists)  # recup les donnees parses

    db = InsertDb()  # creation de la class db avec insertdb
    db.insert_categories()
    db.insert_products(results)  # paramettre result ok

    #db.m_cursor.close()


if __name__ == "__main__":
    main()

    # categories = {}  # creation dico categories
    # for result in results:  # boucle sur le tupple results avec creation de la variable result
    #     category_name = result[6]  # creation de la variable category_name = results avec 6 id en index
    #     categories[category_name] = 1  # je passe category_name dans le dico categories
    #
    # id = 0  # creation de la variable id en depart a 0
    # for categorie in categories:  # boucle sur dico categories avec creation de la variable categorie
    #     categories[categorie] = id  # creation des categories dans le dico categories
    #     id = id + 1  # incrementation de id
    #
    # # for categorie in categories: # boucle sur dico categories avec creation de la variable categorie
    # #     id = categories[categorie] # id  = a categorie de categories
    # #     name =categorie # creation variable name
    # #     db.insert_category(id, name) # insert dans la table category
    #
    # for category in categories:
    #     print(category, categories[category])
    #     db.insert_category(categories[category], category)  # fonctionne !
    #
    # for main_home in results:
    #     category_name = main_home[6]
    #     category_id = categories[category_name]
    #
    #     # print(main_home[2])
    #     product = [main_home[0], main_home[1], main_home[2], main_home[3], main_home[4], main_home[5], category_id]
    #     print(product)
    #     db.insert_product(main_home[0], main_home[1], main_home[2], main_home[3], main_home[4], main_home[5], category_id)

    # db.show_products_db()  # a faire formate en liste

# line = results[0]
# print(line)
# db.insert_product(line)
# db.insert_category()
# database.insert_category(result)

# db.insert_product()

# cursor.close()


# sql = "INSERT INTO category (category_id, category_name) VALUES (%(category_id)s, %(category_name)s)"
# self.m_cursor.executemany(sql, first_category)
# self.m_cursor.execute(("INSERT INTO category (category_id, category_name) VALUES \
# (%(category_id)s, %(category_name)s)"), {"category_id": (first_category[0]), "category_name": (first_category[1])})


# def show_category (self):
#     try:
#         # sql = "SELECT * from category"
#         sql_show_category = "select category_name from category;"
#         self.m_cursor.execute(sql_show_category)
#         result = self.m_cursor.fetchall()
#         # print(result)
#         re = ','','','.join(result)
#         print(re)
#     except ValueError:
#         pass
