from datetime import datetime
import requests, random
from pprint import pprint
import os
from termcolor import colored
import time

start_time = time.time()


STATION_ID_1 = "6189bb7809e7430001ba0ea7"
API_ID = os.environ["API_ID"]



# pprint(my_station_details)

# messages = ['{0:15b}'.format(random.randrange(0, 32768)) for i in range(8)]
# pprint(messages)
# pprint([int(int_data, 2) for int_data in messages])
def get_covert_message():
    messages = ['{0:15b}'.format(random.randrange(0, 32768)) for i in range(8)]
    print("COVERT MESSAGE TO BE SENT: ", end='')
    print(messages)

    return messages

def check_stations()-> list():
    messages = get_covert_message()

    flag = True
    ctr = 0
    dataRead=[]
    while True:
        while flag:
            my_stations = requests.get(f"http://api.openweathermap.org/data/3.0/stations?appid={API_ID}").json()
            for station, message in zip(my_stations, messages):
                if station['id'] == "6178c19809e7430001ba0b75" and station['altitude'] is not None:
                    dataRead.append(station['altitude'])
                    flag = False
                    break

            if not flag:
                print(colored("ACK RECEIVED", 'red'))
                print("Sending Covert Message")
                put_data()
                flag = True
        if len(dataRead) == 3:
            return dataRead

def put_data():
    messages = get_covert_message()
    # pprint(messages)
    print("PRINTING IN DECIMAL FOR EASY COMPARISON: ",end="")
    pprint([int(int_data, 2) for int_data in messages])
    print(colored('Message sent', 'green'))
    station_counter = 0
    my_stations = requests.get(f"http://api.openweathermap.org/data/3.0/stations?appid={API_ID}").json()
    # print("Sending Covert Message")
    for station, message in zip(my_stations, messages):
        STATION_ID = station["id"]
        STATION_ENDPOINT_PUT = f"http://api.openweathermap.org/data/3.0/stations/{STATION_ID}?appid={API_ID}"
        lat_encoded_int = int(message[0:7], 2) - 90
        long_encoded = int(message[7:15], 2) - 180
        data = requests.put(STATION_ENDPOINT_PUT, json={
            "external_id": f"HENRIETTA_TEST_{station_counter}",
            "name": "RIT's Weather Station",
            "latitude": lat_encoded_int,
            "longitude": long_encoded,
            "altitude": None
        })
        station_counter = station_counter + 1
        # print(data.json())

    # print(colored('Next Covert Message Sent', 'red'))
    return
def check_bandwidth(start_time, end_time):
    end_time = time.time()
    time_elapsed = end_time - start_time
    print(time_elapsed)

put_data()
check_stations()
check_bandwidth(start_time, end_time)
'''
[16405, 20061, 20199, 11472, 29367, 6485, 16218, 25455]
[16405, 20061, 20199, 11472, 29367, 6485, 16218, 25455]
'''