
import pandas as pd
import requests
from config import cfg

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



# Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse JSON response
#     rates_data = response.json()

#     # Convert JSON to DataFrame
#     df = pd.json_normalize(rates_data)

#     # Save DataFrame to CSV file
#     df.to_csv('output.csv', index=False)

#     print("Data saved to 'output.csv'")
# else:
#     # Print an error message if the request was not successful
#     print(f"Error: {response.status_code} - {response.text}")
    
    
