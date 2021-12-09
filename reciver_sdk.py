from datetime import datetime

import pyowm, os
from pyowm.stationsapi30.measurement import Measurement

owm = pyowm.OWM(os.environ["API_ID"])
mgr = owm.stations_manager()        # Obtain the Stations API client

current_time = int(datetime.utcnow().timestamp())

retrieved_station = mgr.get_station("6178c19809e7430001ba0b75")

measurement = Measurement.from_dict({
    "station_id" : "6178c19809e7430001ba0b75",
    "temperature": 18.7,
    "wind_speed": 1.2,
    "timestamp": current_time,
})

mgr.send_measurement(measurement)

print(mgr.get_measurements("6178c19809e7430001ba0b75", "d", current_time-3600, current_time, 100))