import mysql.connector

cnx = mysql.connector.connect(user='yayass', password='test1234', host='127.0.0.1', database='Openfood')

mycursor = cnx.cursor()

mycursor.execute("CREATE DATABASE Openfood")

mycursor.execute("CREATE TABLE category (id MEDIUMINT,"
                 " category_name VARCHAR(40))")

mycursor.execute("CREATE TABLE product (product_id MEDIUMINT,"
                 " product_name VARCHAR(40),"
                 " description TEXT,"
                 " store VARCHAR(40),"
                 " nutri_score SMALLINT,"
                 " url_product VARCHAR(40),"
                 " id_category SMALLINT)")



mycursor.execute("CREATE TABLE favoris (id MEDIUMINT,"
                 " product_id MEDIUMINT)")

