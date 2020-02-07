"""script allowing the insert in the db"""
# -*- PipEnv -*-
# -*- coding: Utf-8 -*-
import mysql.connector
from .api_data import ApOpen
from .constantes import USER, PASSWORD, HOST, DATABASE, CATEGORY_LIST


class InsertDb:
    """Class allowing inserts in the product category tables of the Database openfood"""

    def __init__(self):

        self.m_db = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST,
                                            database=DATABASE)  # assigne a Database mysql.connector id
        self.m_cursor = self.m_db.cursor()

    def create_db (self):
        """method for inserting data into the category table. method ok works"""
        fscript = open('sqlscript.sql', 'r')
        sqlFile = fscript.read()
        fscript.close()
        sqlCommands = sqlFile.split(';')
        for command in sqlCommands:
            try:
                self.m_cursor.execute(command)
            except Exception as e:
                print('debut de la creation base de donnees')

    def insert_category(self, name):
        """category insert method"""
        try:
            sql = "INSERT INTO category (name) VALUES (%s)"
            n = (name,)
            print('insert_category:', n)
            self.m_cursor.execute(sql, n)
            self.m_db.commit()
            print(self.m_cursor)
        except ValueError:
            pass


    def insert_categories(self):
        """loop for inserting into the category table"""
        for category in CATEGORY_LIST:
            self.insert_category(category)

    def insert_product(self, product, descri, store, nutri, url, cat):
        """method allowing inserts in the product table"""
        try:
            sql = "INSERT INTO products (product_name, description, store, nutri_score, url_product, " \
                  "category_id) VALUES (%s, %s, %s, %s, %s, %s)"

            v = (product, descri, store, nutri, url, cat)
            self.m_cursor.execute(sql, v)
            self.m_db.commit()
        except ValueError:
            pass

    def insert_products(self, products):
        """method for inserting data into the product table"""
        try:
            sql = "select * from category;"
            self.m_cursor.execute(sql)
            categories = self.m_cursor.fetchall()

            for product in products:
                #print(product)
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

    def insert_favori(self, product_id, substitut_id):
        """favorite table data insert method"""
        try:
            sql = "INSERT INTO substituts (product_id, substitut_id)" \
                  " VALUES (%s, %s)"
            v = (product_id, substitut_id)
            self.m_cursor.execute(sql, v)
            self.m_db.commit()
        except ValueError:
            pass

def main():
    """import of apopen class from api_data"""
    data_api = ApOpen()
    products_lists = data_api.get_products_list()
    results = data_api.resultdata(products_lists)
    database = InsertDb()
    database.insert_categories()
    database.insert_products(results)

if __name__ == "__main__":
    main()
