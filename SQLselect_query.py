import mysql.connector
from config import DATABASE_CONFIG
from mysql.connector import errorcode

cnx = mysql.connector.connect(**DATABASE_CONFIG)
cursor = cnx.cursor()


# Query to select and display data
query = "SELECT * FROM tarzan"
cursor.execute(query)
for row in cursor:
     print(row)