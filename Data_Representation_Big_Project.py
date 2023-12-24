from flask import Flask
import pandas as pd
import requests
from config import cfg

app = Flask(__name__)

apikey = cfg("HQrevkey")

base_url = "https://market-watch-api.datascience.hqrevenue.com"
endpoint = "/api/v1/cities"
url = f"{base_url}{endpoint}"

headers = {
    "X-API-KEY": apikey
}

#params = {
#    "city_id": 140,
#    "starttargetdate": "2023-12-24",
#    "endtargetdate": "2024-01-24",
#    "snapshotdate": "2023-12-24 19:08:23.603839",
#    "property_types": "hotels",
#    "stars": ['3', '4', '5'],
#    "occupancy": "single"
#}

response = requests.get(url, headers=headers, params=None)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse and print the JSON response
    rates_data = response.json()
    print(rates_data)
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code} - {response.text}")