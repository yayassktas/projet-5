# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

import mysql.connector
# from api_data import DatabaseManagement

from .api_data import ApOpen
#import api_data
from .constantes import USER, PASSWORD, HOST, DATABASE, CATEGORY_LIST


# Classe permettant les inserts dans les tables categories products de la db openfood
class InsertDb:

    # methode de connection a la db sql
    def __init__(self):

        self.m_db = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST,
                                            database=DATABASE)  # assigne a db mysql.connector id

        self.m_cursor = self.m_db.cursor()

    # methode permettant l insert des donnees dans la table category. methode ok fonctionne

    def create_db(self):
        fd = open('sqlscript.sql', 'r')
        sqlFile = fd.read()
        fd.close()
        sqlCommands = sqlFile.split(';')
        for command in sqlCommands:

            try:
                self.m_cursor.execute(command)
            except Exception as e:

                print ('debut de la creation base de donnees')





    # def executeScriptsFromFile (filename):
    #     fd = open(filename, 'r')
    #     sqlFile = fd.read()
    #     fd.close()
    #     sqlCommands = sqlFile.split(';')
    #
    #     for command in sqlCommands:
    #         try:
    #             if command.strip() != '':
    #                 cursor.execute(command)
    #         except IOError, msg:
    #             print
    #             "Command skipped: ", msg
    #
    # executeScriptsFromFile('SQL-FILE-LOCATION')
    # cnx.commit()

    def insert_category(self, name):
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

    # methode permettant les inserts dans la table product
    def insert_product(self, a, b, c, d, e, f):
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
                print(product)
                for category in categories:
                    # Je compare le nom de la catégorie avec le nom de la catégorie DU PRODUIT
                    # print(category,product)
                    if category[1] == product[5].lower():
                        # print (category[1])
                        # si les 2 noms sont similaires, alors je défini l'id de la catégorie dans ma variable finale
                        cat_id = category[0]  # probleme les nom d id sont en majuscule
                        self.insert_product(product[0][0:150], product[1], product[2][0:1], product[3], product[4],
                                            cat_id)
            self.m_db.commit()
        except ValueError:
            pass

    #  for id in products:
    # self.insert_product(a, b, c, d, e, f, g)

    def insert_favori(self, product_id, substitut_id):
        try:
            sql = "INSERT INTO substituts (product_id, substitut_id) VALUES ({}, '{}')".format(product_id, substitut_id)
            self.m_cursor.execute(sql)
            self.m_db.commit()
        except ValueError:
            pass


#  source /home/yayass/Téléchargements/OpenFoodFacts/sqlscript.sql;


def main():
    data_api = ApOpen()  # import de la class apopen de api_data
    products_lists = data_api.get_products_list()  # recup toute les donnees appel de la methode get product list de la class apopen INTERET ?
    results = data_api.resultdata(products_lists)  # recup les donnees parses

    db = InsertDb()  # creation de la class db avec insertdb
    db.insert_categories()
    db.insert_products(results)  # paramettre result ok

    # db.m_cursor.close()


if __name__ == "__main__":
    main()



