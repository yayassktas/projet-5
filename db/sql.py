# -*- PipEnv -*-
# -*- coding: Utf-8 -*-
# import Conf.constantes as conf
import mysql.connector
import sys

sys.path.append('../')
from Api.api_data import ApOpen


class InsertDb:

    def __init__ (self):
        db = mysql.connector.connect(user='yayass', password='test1234', host='127.0.0.1',
                                     database='openfood')  # assigne a db mysql.connector id
        self.m_db = db  # assigne db a m_db pour commit les inserts
        self.m_cursor = db.cursor()  # assigne db.cursor a m_cursor

    #  faire les inserts de donnees api

    def insert_category (self, id, name):
        try:
            sql = "INSERT INTO category (category_id, category_name) VALUES ({}, '{}')".format(id, str(name))
            self.m_cursor.execute(sql)
            self.m_db.commit()
        except ValueError:
            pass

    def show_category (self):
        try:
            #sql = "SELECT * from category"
            sql_show_category = "select category_name from category;"
            self.m_cursor.execute(sql_show_category)
            result = self.m_cursor.fetchall()
           # print(result)
            re = ','','','.join(result)
            print(re)
        except ValueError:
            pass

    def insert_product (self, a, b, c, d, e, f, g):
        try:
            sql = "INSERT INTO products (products_id, product_name, description, store, nutri_score, url_product, " \
                  "category_category_id) VALUES ({}, '{}', '{}', '{}', '{}', '{}', {})".format(a, b, c, d, e, f, g)
            self.m_cursor.execute(sql)
            self.m_db.commit()
        except ValueError:
            pass



    def show_substituts_db (self):
            pass


def main ():
    # Download the responseen
    data_api = ApOpen()  # import de la class apopen de apidata
    products_lists = data_api.get_products_list()  # recup toute les donnees appel de la methode get product list
    results = data_api.resultdata(products_lists)  # recup les donnees parses

    db = InsertDb()  # creation de la class db avec insertdb

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
    # for r in results:
    #     category_name = r[6]
    #     category_id = categories[category_name]
    #
    #     # print(r[2])
    #     product = [r[0], r[1], r[2], r[3], r[4], r[5], category_id]
    #     print(product)
    #     db.insert_product(r[0], r[1], r[2], r[3], r[4], r[5], category_id)

    db.show_category()
    #db.show_products_db()  # a faire formate en liste


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

if __name__ == "__main__":
    main()
