import smartcar
import time
import pickle
from dateutil import parser
import urllib.request


client = smartcar.AuthClient('your-client-id-here','your-client-secret-here','http://localhost/smartcar/redirect/','live')


# Alter this list to specify the scope of permissions your application is requesting access to
scopes = ['read_vehicle_info', 'read_battery','read_charge']

file = open('tokens.txt', 'rb')
tokens = pickle.load(file)
file.close()

token=tokens.access_token
print("Saved access token is " + token)



vehicles = smartcar.get_vehicles(token)

print(vehicles.vehicles)
vehicle_id = vehicles.vehicles[0]

vehicle = smartcar.Vehicle(vehicle_id, token)


charge=vehicle.charge()
is_plugged_in = charge.is_plugged_in
state = charge.state
meta=charge.meta
validDate=meta.data_age
date = parser.parse(validDate)

print("Valid time {}".format(date.astimezone().isoformat()))

print(state)

# Charge(is_plugged_in=False, state='NOT_CHARGING', meta=Meta(data_age='2023-11-03T12:19:37.000Z', request_id='5b304e0f-3185-4208-92eb-761e1bb1864e'))
#Battery(percent_remaining=0.75, range=176, meta=Meta(data_age='2023-11-03T12:19:37.000Z', unit_system='metric', request_id='1998d993-e6a6-45a1-b21c-e99f371cd2e0'))

print(charge)

battery = vehicle.battery()
meta=battery.meta
validDate=meta.data_age
date = parser.parse(validDate)

print("Valid time {}".format(date.astimezone().isoformat()))
percentage=battery.percent_remaining
print(percentage)

if(percentage<.80):
    if(state=="NOT_CHARGING"):
        print("Alert - car is not charged, and is not charging!")
        # this is where I post a status to homebridge/homeassistant
        url = 'http://localhost:51828/?accessoryId=evchargealert&state=true'
        page = urllib.request.urlopen(url)
        print(page.read())


