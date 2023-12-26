import mysql.connector
from config import DATABASE_CONFIG

def create_mysql_connection():
    connection = mysql.connector.connect(**DATABASE_CONFIG)
    return connection

connection = create_mysql_connection()

if connection.is_connected():
    print("Connected to MySQL database")

    # Create tables if they don't exist
    cursor = connection.cursor()

    create_cities_table_query = """
    CREATE TABLE IF NOT EXISTS cities (
        city_id INT PRIMARY KEY,
        property_type VARCHAR(255),
        stars VARCHAR(255),
        occupancy VARCHAR(255)   
    );
    """

    create_segment_rates_table_query = """
    CREATE TABLE IF NOT EXISTS segment_rates (
        city_id INT,
        target_date DATE,
        snapshot_date DATETIME,
        minimum_rate FLOAT,
        median_rate FLOAT,
        maximum_rate FLOAT,
        count INT,
        PRIMARY KEY (city_id, target_date)
    );
    """

    cursor.execute(create_cities_table_query)
    cursor.execute(create_segment_rates_table_query)

    cursor.close()


# Function to insert data into MySQL table
def insert_data_into_mysql(connection, data):
    cursor = connection.cursor()

    try:
        for record in data:
            city_id = record['cityId']
            property_type = record['propertyType']
            stars = record['stars']
            occupancy = record['occupancy']
            

            for segment_rate in record['segmentRates']:
                target_date = segment_rate['targetDate']
                snapshot_date = segment_rate['snapshotDate']
                minimum_rate = segment_rate['minimumRate']
                median_rate = segment_rate['medianRate']
                maximum_rate = segment_rate['maximumRate']
                count = segment_rate['count']

                # Assuming you have tables named 'cities' and 'segment_rates'
                city_insert_query = """
                INSERT INTO cities (city_id, property_type, stars, occupancy)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE description=VALUES(description);
                """

                segment_rate_insert_query = """
                INSERT INTO segment_rates (city_id, target_date, snapshot_date, minimum_rate, median_rate, maximum_rate, count)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
                """

                # Insert data into 'cities' table
                city_values = (city_id, property_type, stars, occupancy)
                cursor.execute(city_insert_query, city_values)

                # Insert data into 'segment_rates' table
                segment_rate_values = (city_id, target_date, snapshot_date, minimum_rate, median_rate, maximum_rate, count)
                cursor.execute(segment_rate_insert_query, segment_rate_values)

        connection.commit()
        print("Data uploaded successfully!")

    except Exception as e:
        print(f"Error uploading data: {e}")

    finally:
        cursor.close()
