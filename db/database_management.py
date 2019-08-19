# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

import mysql.connector
from Api.api_data import ApOpen


class DatabaseManagement:

    def __init__ (self):
        db = mysql.connector.connect(user='yayass', password='test1234', host='127.0.0.1',
                                     database='openfood')  # assigne a db mysql.connector id
        self.m_db = db  # assigne db a m_db pour commit les inserts
        self.m_cursor = db.cursor()  # assigne db.cursor a m_cursor

    def show_category(self):
        try:
            # sql = "SELECT * from category"
            sql_show_category = "select category_id, category_name from category;"
            self.m_cursor.execute(sql_show_category)
            result = self.m_cursor.fetchall()
            # print(result)
            for row in result:
                print(row[0], ":", row[1])
        except ValueError:
            pass

    def show_products_db(self, category_id):
        try:
            # sql = "SELECT products_id, product_name, description, store, nutri_score  FROM products;"
            sql_store = "SELECT products_id, product_name from products WHERE category_category_id = {};".format(
                category_id)
            self.m_cursor.execute(sql_store)
            result = self.m_cursor.fetchall()
            for row in result:
                print("Nom du produit :", row[1])
        except ValueError:
            pass


    def show_favoris(self):
        try:
            sql_show_favoris = "product_id from favoris;"
            self.m_cursor.execute(sql_show_favoris)
            result = self.m_cursor.fetchall()
            for row in result:
                print(row[0])
        except ValueError:
            pass









