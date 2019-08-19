# -*- PipEnv -*-
# -*- coding: Utf-8 -*-
import mysql
import mysql.connector






cnx = mysql.connector.connect(user='yayass', password='test1234', host='127.0.0.1', database='Openfood')
# mettre user en ma




#db = connection.MySQLConnection(user='yayass', password='test1234',
                                 #host='127.0.0.1',
                                 #database='Openfood')





category_list = ["Soda",
                 "Fromages",
                 "Desserts",
                 "Viandes",
                 "Fruits"]
