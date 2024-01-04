# SQL testing and maintanace functions - Fetching current table names from database

import mysql.connector
from config import DATABASE_CONFIG
from mysql.connector import errorcode

def get_table_names():
    try:
        # Connect to the database
        cnx = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = cnx.cursor()

        # Get table names
        query = "SHOW TABLES"
        cursor.execute(query)

        # Fetch and print table names
        tables = cursor.fetchall()
        print("Existing tables:")
        for table in tables:
            print(table[0])

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        cursor.close()
        cnx.close()
        
        
get_table_names()
