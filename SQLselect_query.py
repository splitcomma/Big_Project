# SQL testing and maintanace functions - Retriving data from selected table

import mysql.connector
from config import DATABASE_CONFIG
from mysql.connector import errorcode

#Connecting to the database
cnx = mysql.connector.connect(**DATABASE_CONFIG)
cursor = cnx.cursor()


# Query to select and display data
query = "SELECT * FROM CITIES"
cursor.execute(query)
for row in cursor:
     print(row)