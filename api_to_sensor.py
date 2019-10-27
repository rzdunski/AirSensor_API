import requests
import pprint

url="http://192.168.1.16"
get_basic_state="/api/device/state"
get_network_information="/api/device/network"
get_settings_state="/api/settings/state"
get_sensor_data="/api/air/state"
get_runtime="/api/air/runtime"

data_basic_state = requests.get(url+get_basic_state)
data_sensors = requests.get(url+get_sensor_data)
json_basic_state = data_basic_state.json()
json_data_sensors= data_sensors.json()


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
        elif sensor['qualityLevel'] == 2:
            print("Good quality")
        elif sensor['qualityLevel'] == 3:
            print("Moderate quality")
        elif sensor['qualityLevel'] == 4:
            print("Sufficient quality")
        elif sensor['qualityLevel'] == 5:
            print("Poor quality")
        elif sensor['qualityLevel'] == 6:
            print("Very poor quality")
        else:
            print("Wrong value:")

    elif sensor['type'] == "pm10":
        print("pm10: ")
        print("value: ", sensor['value'])
        print("qualityLevel: ", sensor['qualityLevel'])
        if sensor['qualityLevel'] == 1:
            print("Best quality")
        elif sensor['qualityLevel'] == 2:
            print("Good quality")
        elif sensor['qualityLevel'] == 3:
            print("Moderate quality")
        elif sensor['qualityLevel'] == 4:
            print("Sufficient quality")
        elif sensor['qualityLevel'] == 5:
            print("Poor quality")
        elif sensor['qualityLevel'] == 6:
            print("Very poor quality")
        else:
            print("Wrong value:")
    
    print("###########################")
