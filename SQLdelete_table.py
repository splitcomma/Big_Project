# SQL testing and maintanace functions - Deleting tables no longer in use  

import mysql.connector
from config import DATABASE_CONFIG
from mysql.connector import errorcode

def drop_table(table_name):
    try:
        # Connect to the database
        cnx = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = cnx.cursor()

        # Drop the table
        query = f"DROP TABLE {table_name}"
        cursor.execute(query)

        print(f"Table {table_name} dropped successfully.")

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

table_to_drop = "CITIES"
drop_table(table_to_drop)
