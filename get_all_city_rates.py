import pandas as pd
import requests
import mysql.connector
from config import DATABASE_CONFIG

# Function to fetch city IDs from the API
def get_city_ids():
    base_url = "https://market-watch-api.datascience.hqrevenue.com"
    endpoint = "/api/v1/cities"
    url = f"{base_url}{endpoint}"

    response = requests.get(url)
    if response.status_code == 200:
        cities_data = response.json()
        city_ids = [city['id'] for city in cities_data]
        return city_ids
    else:
        print(f"Error fetching city IDs: {response.status_code} - {response.text}")
        return []

# Function to fetch and upload city rates data for a given city ID
def fetch_and_upload_city_rates(city_id):

    pass
# Database connection
cnx = mysql.connector.connect(**DATABASE_CONFIG)
cursor = cnx.cursor()

# Fetch city IDs
city_ids = get_city_ids()

# Iterate through each city ID and fetch/upload city rates data
for city_id in city_ids:
    fetch_and_upload_city_rates(city_id)

# Close the database connection
cursor.close()
cnx.close()