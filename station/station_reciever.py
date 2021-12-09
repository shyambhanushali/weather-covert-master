from datetime import datetime
import requests, os
from pprint import pprint
import time
from termcolor import colored


STATION_ID = "6178c19809e7430001ba0b75"
API_ID = os.environ["API_ID"]

# STATION_ENDPOINT = f"http://api.openweathermap.org/data/3.0/stations/{STATION_ID}?appid={API_ID}"
#
# station_data = requests.get(STATION_ENDPOINT).json()
#
# lat_encoded_int = station_data["latitude"] + 90
# long_encoded_int = station_data["longitude"] + 180
#
# print(f"Message in bits is {'{0:07b}'.format(lat_encoded_int)}{'{0:08b}'.format(long_encoded_int)}")
i=0
data = [123, 456, 789]
# while i < 3:
# all_stattion_content = requests.get(f"http://api.openweathermap.org/data/3.0/stations?appid={API_ID}").json()
# data = [('{0:07b}'.format(station_data["latitude"] + 90)) + ('{0:08b}'.format(station_data["longitude"] + 180))
#         for station_data in all_stattion_content]


my_stations = None
flag = True
while flag:
    my_stations = requests.get(f"http://api.openweathermap.org/data/3.0/stations?appid={API_ID}").json()
    for i in range(len(my_stations)):
        # print(my_stations[i]['altitude'])
        if my_stations[i]['id'] == "6178c19809e7430001ba0b75" and my_stations[i]['altitude'] is None:
            flag = False
            break

if not flag:
    print(colored("Covert Message Received", 'red'))
    data = [('{0:07b}'.format(station_data["latitude"] + 90)) + ('{0:08b}'.format(station_data["longitude"] + 180))
                for station_data in my_stations]
    print(data)

    STATION_ENDPOINT = f"http://api.openweathermap.org/data/3.0/stations/{STATION_ID}?appid={API_ID}"
    values_for_put = requests.get(STATION_ENDPOINT).json()
    latitude = values_for_put['latitude']
    longitude = values_for_put['longitude']

    data1 = requests.put(STATION_ENDPOINT, json={
        "external_id": f"HENRIETTA_TEST_0",
        "name": "RIT's Weather Station",
        "latitude": latitude,
        "longitude": longitude,
        "altitude": 123
    })
    # print(data1)
# i+=1

print("RECEIVED MSG IN DECIMAL FORMAT: ", end='')
pprint([int(int_data, 2) for int_data in data])
print(colored("ACKNOWLEDGEMENT SENT", 'green'))