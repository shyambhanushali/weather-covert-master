from datetime import datetime
import requests, os
from pprint import pprint

API_ID = os.environ["API_ID"]

CREATE_STATIONS_ENDPOINT = f"http://api.openweathermap.org/data/3.0/stations?appid={API_ID}"

for station_number in range(0, 7):
    print(requests.post(CREATE_STATIONS_ENDPOINT, json={
        "external_id": f"HENRIETTA_TEST_{station_number + 1}",
        "name": "RIT's Weather Station",
        "latitude": 45,
        "longitude": -122.47,
        "altitude": 45
    }).json())