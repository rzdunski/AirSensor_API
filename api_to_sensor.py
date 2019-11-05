import requests
import pprint

AirSensor_url="http://192.168.1.16"
switch_url="http://192.168.1.29"
get_basic_state="/api/device/state"
get_network_information="/api/device/network"
get_settings_state="/api/settings/state"
get_sensor_data="/api/air/state"
get_runtime="/api/air/runtime"

data_basic_state = requests.get(AirSensor_url+get_basic_state)
data_sensors = requests.get(AirSensor_url+get_sensor_data)
json_basic_state = data_basic_state.json()
json_data_sensors= data_sensors.json()

switch_runtime=requests.get(switch_url+"/api/device/uptime")


switch_runtime
print("id:", json_basic_state['id'])
pprint.pprint(json_basic_state)

for sensor in json_data_sensors['air']['sensors']:
    if sensor['type'] == "pm1":
        print("pm1: ")
        print("value: ", sensor['value'])
    

    elif sensor['type'] == "pm2.5":
        print("pm2.5: ")
        print("value: ", sensor['value'])
        print("qualityLevel: ", sensor['qualityLevel'])
        if sensor['qualityLevel'] == 1:
            print("Best quality")
            requests.post(switch_url+"/s/true")
        elif sensor['qualityLevel'] == 2:
            print("Good quality")
            requests.post(switch_url+"/s/true")
        elif sensor['qualityLevel'] == 3:
            print("Moderate quality")
            requests.post(switch_url+"/s/false")
        elif sensor['qualityLevel'] == 4:
            print("Sufficient quality")
            requests.post(switch_url+"/s/false")
        elif sensor['qualityLevel'] == 5:
            print("Poor quality")
            requests.post(switch_url+"/s/false")
        elif sensor['qualityLevel'] == 6:
            requests.post(switch_url+"/s/false")
            print("Very poor quality")
            
        else:
            print("Wrong value:")

    elif sensor['type'] == "pm10":
        print("pm10: ")
        print("value: ", sensor['value'])
        print("qualityLevel: ", sensor['qualityLevel'])
        if sensor['qualityLevel'] == 1:
            print("Best quality")
            requests.post(switch_url+"/s/true")
        elif sensor['qualityLevel'] == 2:
            print("Good quality")
            requests.post(switch_url+"/s/true")
        elif sensor['qualityLevel'] == 3:
            print("Moderate quality")
            requests.post(switch_url+"/s/false")
        elif sensor['qualityLevel'] == 4:
            print("Sufficient quality")
            requests.post(switch_url+"/s/false")
        elif sensor['qualityLevel'] == 5:
            print("Poor quality")
            requests.post(switch_url+"/s/false")
        elif sensor['qualityLevel'] == 6:
            print("Very poor quality")
            requests.post(switch_url+"/s/false")
        else:
            print("Wrong value:")
    
    print("###########################")
