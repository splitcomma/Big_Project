import pandas as pd
import requests
import mysql.connector
from config import cfg
from config import DATABASE_CONFIG

def create_mysql_connection():
    connection = mysql.connector.connect(**DATABASE_CONFIG)
    return connection

connection = create_mysql_connection()

# Your existing code for API request
apikey = cfg("HQrevkey")
base_url = "https://market-watch-api.datascience.hqrevenue.com"
endpoint = "/api/v1/cities"
url = f"{base_url}{endpoint}"
headers = {"X-API-KEY": apikey}

response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse JSON response
    cities_data = response.json()

    # Flatten nested structure
    rows = []
    for row in cities_data:
        city_id = row['id']
        city_name = row['name']
        currency = row['currency']

        # Append the extracted data as a row
        rows.append([city_id, city_name, currency])

    # Convert data to DataFrame
    columns = ['city_id', 'city_name', 'currency']
    df = pd.DataFrame(rows, columns=columns)

    print(df)


    # Create a MySQL connection
    connection = create_mysql_connection()

    try:
        # Create a cursor
        cursor = connection.cursor()

        # Create the table if it doesn't exist
        create_table_query = """
            CREATE TABLE IF NOT EXISTS cities (
                city_id INT,
                city_name VARCHAR(255),
                currency VARCHAR(255)
            )
        """
        cursor.execute(create_table_query)

        # Insert data into the MySQL table
        insert_query = """
            INSERT INTO cities
            (city_id, city_name, currency)
            VALUES (%s, %s, %s)
        """
        values = df.values.tolist()
        cursor.executemany(insert_query, values)

        # Commit changes
        connection.commit()
        print("Data saved to MySQL database")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

else:
    # Print an error message if the request was not successful
   print(f"Error: {response.status_code} - {response.text}")