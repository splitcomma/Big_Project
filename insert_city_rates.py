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
endpoint = "/api/v1/cityrates"
url = f"{base_url}{endpoint}"
headers = {"X-API-KEY": apikey}
params = {
   "city_id": 140,
   "starttargetdate": "2023-12-24",
   "endtargetdate": "2024-01-24",
   "snapshotdate": "2023-12-24 19:08:23.603839",
   "property_types": "hotels",
   "stars": ['3', '4', '5'],
   "occupancy": "single"
}
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse JSON response
    rates_data = response.json()

    # Flatten nested structure
    flattened_data = []
    for row in rates_data:
        city_id = row['cityId']
        property_type = row['propertyType']
        description = row['description']

        for rate in row['segmentRates']:
            stars = description.split(', ')[1].split(' ')[0]  # Extract stars from description
            snapshot_date = rate['snapshotDate']
            target_date = rate['targetDate']
            minimum_rate = rate['minimumRate']
            median_rate = rate['medianRate']
            maximum_rate = rate['maximumRate']
            count = rate['count']

            flattened_data.append([city_id, property_type, stars, snapshot_date, target_date, minimum_rate, median_rate, maximum_rate, count])

    # Convert flattened data to DataFrame
    columns = ['city_id', 'property_type', 'stars', 'snapshot_date', 'target_date', 'minimum_rate', 'median_rate', 'maximum_rate', 'count']
    df = pd.DataFrame(flattened_data, columns=columns)
    
    print(df)

    # Create a MySQL connection
    connection = create_mysql_connection()

    try:
        # Create a cursor
        cursor = connection.cursor()

        # Create the table if it doesn't exist
        create_table_query = """
            CREATE TABLE IF NOT EXISTS testhq (
                city_id INT,
                property_type VARCHAR(255),
                stars VARCHAR(255),
                snapshot_date VARCHAR(255),
                target_date VARCHAR(255),
                minimum_rate FLOAT,
                median_rate FLOAT,
                maximum_rate FLOAT,
                count INT
            )
        """
        cursor.execute(create_table_query)

        # Insert data into the MySQL table
        insert_query = """
            INSERT INTO testhq
            (city_id, property_type, stars, snapshot_date, target_date, minimum_rate, median_rate, maximum_rate, count)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
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
