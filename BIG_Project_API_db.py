import requests
import mysql.connector
from config import cfg, DATABASE_CONFIG



def get_request(url, param):
    headers = {"X-API-KEY": cfg("X-API-KEY")}

    try:
        response = requests.get(url, headers=headers, params=param)
    except requests.exceptions.RequestException as err:
        print(err)
        raise SystemExit(err)

    result = {'code': response.status_code}
    if result['code'] == 200:
        result['json'] = response.json()

    return result


def get_cities():
    endpoint = '/api/v1/cities'
    res = get_request(f'{BASE_URL}{endpoint}', None)
    return res['json']


def get_city_rates(city_id):
    endpoint = "/api/v1/cityrates"
    params = {
        "city_id": city_id,
        "starttargetdate": "2023-12-15",
        "endtargetdate": "2024-03-15",
        "snapshotdate": "2024-01-04 17:24:39.149819",
        "property_types": "hotels",
        "stars": ['3', '4', '5'],
        "occupancy": "single"
    }

    return get_request(f'{BASE_URL}{endpoint}', params).get('json')


def parse_rates(rates_data):
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

            flattened_data.append([
                city_id,
                property_type,
                stars,
                snapshot_date,
                target_date,
                minimum_rate,
                median_rate,
                maximum_rate,
                count
            ])

    return flattened_data


def create_table(table):
    cursor.execute(table)


def insert_data(key, val):
    cursor.executemany(key, val)
    connection.commit()


cities_table = """
    CREATE TABLE IF NOT EXISTS CITIES (
        city_id INT,
        city_name VARCHAR(255),
        currency VARCHAR(255)
    )
"""

insert_cities = """
    INSERT INTO CITIES
    (city_id, city_name, currency)
    VALUES (%s, %s, %s)
"""


city_rates_table = """
    CREATE TABLE IF NOT EXISTS CITY_RATES (
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

insert_city_rates = """
    INSERT INTO CITY_RATES
    (city_id, property_type, stars, snapshot_date, target_date, minimum_rate, median_rate, maximum_rate, count)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

BASE_URL = 'https://market-watch-api.datascience.hqrevenue.com'

try:
    connection = mysql.connector.connect(**DATABASE_CONFIG)
except mysql.connector.Error as err:
    print(f'Error: {err}')
else:
    cursor = connection.cursor()
    create_table(cities_table)
    create_table(city_rates_table)

    cities = get_cities()
    if cities:
        values = [list(i.values()) for i in cities]
        insert_data(insert_cities, values)

        for city in cities:
            rates = get_city_rates(city['id'])
            values = parse_rates(rates)
            insert_data(insert_city_rates, values)

    cursor.close()
    connection.close()
