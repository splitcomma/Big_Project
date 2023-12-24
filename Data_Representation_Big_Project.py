# Data Representation - Big project
from flask import Flask

import pandas as pd
import requests
import json
#from config import cfg



#apikey = cfg("HQrevkey")
url = "https://market-watch-api.datascience.hqrevenue.com/openapi.json"

response = requests.get(url)
data = response.json()
print(data)