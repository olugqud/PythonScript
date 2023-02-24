import requests
import json
import time

def get_location():
    send_url = 'http://ip-api.com/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    latitude = j['lat']
    longitude = j['lon']
    return (latitude, longitude)

while True:
    current_location = get_location()
    print("Latitude: {}, Longitude: {}".format(current_location[0], current_location[1]))
    time.sleep(10)
