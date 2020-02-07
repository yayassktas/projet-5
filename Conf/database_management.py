# -*- PipEnv -*-
# -*- coding: Utf-8 -*-
"""script for launching sql requests"""
import mysql.connector
from Conf.api_data import ApOpen
from .constantes import USER, PASSWORD, HOST, DATABASE

class DatabaseManagement:
    """init method allowing connection to the Database sql"""
    def __init__(self):

        self.m_db = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST,
                                            database=DATABASE)
        self.m_cursor = self.m_db.cursor()

    def show_categories_db(self):
        """"category display"""

        sql_show_category = "select id, name from category;"
        self.m_cursor.execute(sql_show_category)
        result = self.m_cursor.fetchall()

        return result

    def display_category_db(self):
        """category display"""
        result = self.show_categories_db()
        for row in result:
            print(row[0], ":", row[1])

    def show_products_db(self, id):
        """product display"""
        sql_store = "SELECT id, product_name from products WHERE category_id = %s;"
        v = (id,)
        self.m_cursor.execute(sql_store, v)
        result = self.m_cursor.fetchall()

        return result

    def show_potential_substitut(self, id):
        """display of substitutes"""
        sql_store = "SELECT id, product_name from products WHERE category_id = %s ORDER BY nutri_score LIMIT 20;"
        v = (id,)
        self.m_cursor.execute(sql_store, v)
        result = self.m_cursor.fetchall()

        return result

    def display_potential_substitut(self, id):
        """data formatting"""
        result = self.show_potential_substitut(id)
        for row in result:
            print(row[0], ":", row[1])

    def show_product(self, id):
        """product display"""
        sql_store = "SELECT id, product_name from products WHERE id = %s;"
        v = (id,)
        self.m_cursor.execute(sql_store, v)
        result = self.m_cursor.fetchall()

        return result

    def display_product_db(self, id):
        """layout of products table results"""
        result = self.show_product(id)
        for row in result:
            #    print(row[0]," :", row[1])
            print(row)


    def display_products_db(self, id):
        """layout of products table results"""
        result = self.show_products_db(id)

        for row in result:
            print(row)

    def show_favoris(self):
        """display of the favorites table"""
        try:
            sql_show_favoris = "product_id from favoris;"
            self.m_cursor.execute(sql_show_favoris)
            result = self.m_cursor.fetchall()

            for row in result:
                print(row[0])
        except ValueError:
            pass

    def show_substituts_db(self, id):
        """method for displaying substitutes"""
        sql_show_id = "SELECT DISTINCT s.product_id, p1.product_name as product_name, p2.product_name as substitut_name, s.substitut_id FROM substituts s LEFT JOIN products p1 " \
                      " ON s.product_id = p1.id LEFT JOIN products p2 ON s.substitut_id = p2.id;"

        self.m_cursor.execute(sql_show_id)
        result = self.m_cursor.fetchall()

        for row in result:
            print(
                "Le produit n°{} - {}, a été substitué par le produit n°{} - {}".format(row[0], row[1], row[3], row[2]))


show_db = DatabaseManagement
