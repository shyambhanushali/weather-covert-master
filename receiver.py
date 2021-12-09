from datetime import datetime
import requests, os
from pprint import pprint

STATION_ID = "6178c19809e7430001ba0b75"
API_ID = os.environ["API_ID"]

MEASUREMENT_ENDPOINT = f"http://api.openweathermap.org/data/3.0/measurements"

params = {
    "from" : int(datetime.utcnow().timestamp()) - (3600*24*15),
    "to" : int(datetime.utcnow().timestamp()),
    # "to": 1635319314,
    "station_id" : STATION_ID,
    "appid" : API_ID,
    "type": "d",
    "limit": 100
}

measurement_data = requests.get(MEASUREMENT_ENDPOINT, params=params)

data = (measurement_data.json())
pprint(data, indent=4)