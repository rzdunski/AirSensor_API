import requests
from datetime import datetime
import time

airSensor_url = "http://192.168.1.16"
switchbox_url = "http://192.168.1.29"



pm2_5_TH = 35 #according to WHO 
pm10_TH = 60  #according to WHO
    
while True:
    data_sensors = requests.get(airSensor_url+"/api/air/state").json()
    pm1_value = data_sensors['air']['sensors'][0]['value']
    pm2_5_value = data_sensors['air']['sensors'][1]['value']
    pm10_value = data_sensors['air']['sensors'][2]['value']

    if pm2_5_value <= pm2_5_TH and pm10_value <= pm10_TH:
        requests.post(switchbox_url+"/s/true")
        print(datetime.now().strftime("%H:%M:%S %d/%m/%Y"), "- pm1: {}; pm2.5: {}; pm10: {}; - Heating Recovery Ventilation ON".format(pm1_value, pm2_5_value, pm10_value))
    else:
        requests.post(switchbox_url+"/s/false")
        print(datetime.now().strftime("%H:%M:%S %d/%m/%Y"), "- pm1: {}; pm2.5: {}; pm10: {}; - Heating Recovery Ventilation OFF".format(pm1_value, pm2_5_value, pm10_value))

    time.sleep(300)
