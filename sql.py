import mysql.connector

cnx = mysql.connector.connect(user='yayass', password='test1234', host='127.0.0.1')

mycursor = cnx.cursor()

mycursor.execute("CREATE DATABASE Openfood")

#mycursor.execute("CREATE TABLE nutriments (name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("CREATE TABLE id (name VARCHAR(255), address VARCHAR(255))")

