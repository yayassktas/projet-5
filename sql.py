import mysql.connector

cnx = mysql.connector.connect(user='yayass', password='bermuda',
                              host='127.0.0.1',
                              database='elevage')
cnx.close()