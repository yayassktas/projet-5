# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

import mysql.connector
from Conf.api_data import ApOpen
from .constantes import USER, PASSWORD, HOST, DATABASE


# class appel dans le fichier menu.py permettant d afficher les category et products
class DatabaseManagement:

    # methode init permettant la connection a la db sql
    def __init__(self):
        self.m_db = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST,
                                            database=DATABASE)  # assigne a db mysql.connector id
        # assigne db a m_db pour commit les inserts
        self.m_cursor = self.m_db.cursor()

    # class appele dans le fichier menu.py permettant d afficher les category et products
    def show_categories_db(self):
        sql_show_category = "select id, name from category;"
        self.m_cursor.execute(sql_show_category)
        result = self.m_cursor.fetchall()
        return result

    # mise en page des resultats de la table category
    def display_category_db(self):
        result = self.show_categories_db()
        for row in result:
            print(row[0], ":", row[1])

    # methode permettant d interroge la db pour recup les id, les noms des produits
    def show_products_db(self, id):
        sql_store = "SELECT id, product_name from products WHERE category_id = {};".format(
            id)
        self.m_cursor.execute(sql_store)
        result = self.m_cursor.fetchall()
        return result

    # methode permettant d interroge la db pour recup un produit
    def show_product(self, id):
        sql_store = "SELECT id, product_name from products WHERE id = {};".format(
            id)
        self.m_cursor.execute(sql_store)
        result = self.m_cursor.fetchall()
        return result

    # mise en page des resultats de la table products
    def display_product_db(self, id):
        result = self.show_product(id)
        for row in result:
            #    print(row[0]," :", row[1])
            print(row)

    # mise en page des resultats de la table products
    def display_products_db(self, id):
        result = self.show_products_db(id)
        for row in result:
            #    print(row[0]," :", row[1])
            print(row)

    # affichage de la table favoris
    def show_favoris(self):
        try:
            sql_show_favoris = "product_id from favoris;"
            self.m_cursor.execute(sql_show_favoris)
            result = self.m_cursor.fetchall()
            for row in result:
                print(row[0])
        except ValueError:
            pass

    def show_substituts_db(self, id):
        # methode permettant d afficher les substituts

        # sql_show_substituts = "select id, product_name, nutri_score from products where category_id = {} order by " \
        #                           "nutri_score limit 50; ".format(id)

        sql_show_id = "SELECT DISTINCT s.product_id, p1.product_name as product_name, p2.product_name as substitut_name, s.substitut_id FROM substituts s LEFT JOIN products p1 " \
                      " ON s.product_id = p1.id LEFT JOIN products p2 ON s.substitut_id = p2.id;"

        self.m_cursor.execute(sql_show_id)
        result = self.m_cursor.fetchall()
        print(result.format(var, var2))
        # print("Name={}, \tValue= {}".format(var, var2))
        for row in result:
            print(row[0])


show_db = DatabaseManagement
