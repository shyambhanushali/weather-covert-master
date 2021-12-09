from datetime import datetime
import requests, os
STATION_ID = "6178c19809e7430001ba0b75"
API_ID = os.environ["API_ID"]
MEASUREMENT_ENDPOINT = f"http://api.openweathermap.org/data/3.0/measurements?appid={API_ID}"
legit_measurements = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=Rochester&APPID={API_ID}').json()
current_time = int(datetime.utcnow().timestamp())
measurement = [
  {
    "station_id": "6178c19809e7430001ba0b75",
    "dt": current_time,
    "temperature": legit_measurements["main"]["temp"] + 1, # Covert bit 1
    "wind_speed": legit_measurements["wind"]["speed"], # Covert Bit 0
    "wind_gust": legit_measurements["wind"]["gust"] + 1, # Covert bit 1
    "pressure": legit_measurements["main"]["pressure"] + 1, # Covert bit 1
    "humidity": legit_measurements["main"]["humidity"] + 1, # Covert bit 1
    #"rain_1h": legit_measurements["rain"]["1h"], # Covert bit 0
    "clouds": [
      {
          "condition": "NSC" if legit_measurements["clouds"]["all"] == 90 else "0"
      }
    ]
  }
]
print(current_time)
data = requests.post(MEASUREMENT_ENDPOINT, json=measurement)
print(data.status_code)
print(data.text)
