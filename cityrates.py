
import pandas as pd
import requests
from config import cfg
from mysql_connection import create_mysql_connection, insert_data_into_mysql

def get_request(end_point, param):
    
    headers = {
        "X-API-KEY": apikey
    }
    try:
        response = requests.get(url, headers=headers, params=param)
    except requests.exceptions.RequestException as err:
        print("Connection Error")
        
    result = {'code': response.status_code}
    if result['code'] == 200:
        result['json'] = response.json()
    return result
        

apikey = cfg("HQrevkey")

base_url = "https://market-watch-api.datascience.hqrevenue.com"
endpoint = "/api/v1/cityrates"
url = f"{base_url}{endpoint}"


params = {
   "city_id": 140,
   "starttargetdate": "2023-12-24",
   "endtargetdate": "2024-01-24",
   "snapshotdate": "2023-12-24 19:08:23.603839",
   "property_types": "hotels",
   "stars": ['3', '4', '5'],
   "occupancy": "single"
}


#print(get_request(endpoint, params))
resp = get_request(endpoint, params)
city_rates = resp.get("json")
print(city_rates)
df = pd.json_normalize(city_rates)

mysql_connection = create_mysql_connection()
insert_data_into_mysql(mysql_connection, city_rates)
mysql_connection.close()