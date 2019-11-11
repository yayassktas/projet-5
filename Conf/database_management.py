# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

import mysql.connector
from .api_data import *
from .constantes import *


class DatabaseManagement: # class appele dans le fichier menu.py permettant d afficher les category et products

    def __init__(self): # methode init permettant la connection a la db sql
        self.m_db = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE)  # assigne a db mysql.connector id
        # assigne db a m_db pour commit les inserts
        self.m_cursor = self.m_db.cursor()  # assigne db.cursor a m_cursor

    def show_categories_db(self): # methode permettant d interroge la db pour recup selectionne les id les noms de la table category
        sql_show_category = "select id, name from category;"
        self.m_cursor.execute(sql_show_category)
        result = self.m_cursor.fetchall()
        return result

    def display_category_db(self): # mise en page des resultats de la table category
        result = self.show_categories_db()
        for row in result:
            print(row[0], ":", row[1])

    def show_products_db(self, id): # methode permettant d interroge la db pour recup les id, les noms des produits
        sql_store = "SELECT id, product_name from products WHERE category_id = {};".format(
            id)
        self.m_cursor.execute(sql_store)
        result = self.m_cursor.fetchall()
        return result

    def show_product(self, id): # methode permettant d interroge la db pour recup un produit
        sql_store = "SELECT id, product_name from products WHERE id = {};".format(
            id)
        self.m_cursor.execute(sql_store)
        result = self.m_cursor.fetchall()
        return result

    def display_product_db (self, id): # mise en page des resultats de la table products
        result = self.show_product(id)
        for row in result:
        #    print(row[0]," :", row[1])
             print(row)

    def display_products_db (self, id): # mise en page des resultats de la table products
        result = self.show_products_db(id)
        for row in result:
        #    print(row[0]," :", row[1])
             print(row)

    def show_favoris (self): # affichage de la table favoris 
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

        sql_show_substituts = "select id, product_name, nutri_score from products where category_id = {} order by " \
                                  "nutri_score limit 50; ".format(id)

        self.m_cursor.execute(sql_show_substituts)
        result = self.m_cursor.fetchall()

        for row in result:
            print(row)


    
# creer la class databasemangement
# display_db = DatabaseManagement

show_db = DatabaseManagement