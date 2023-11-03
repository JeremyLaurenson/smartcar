# Step 1: Install smartcar python library by running:    pip install smartcar
# Step 2: Create an account, and register a new app to the smartcar.com dashboard
# Step 3: When you register a new app, youll get a clientID, Client Secret from the smartcar.com dashboard

import smartcar
import time
import pickle


client = smartcar.AuthClient('your-client-id-here','your-client-secret-here','http://localhost/smartcar/redirect/','live')

# Alter this list to specify the scope of permissions your application is requesting access to
scopes = ['read_vehicle_info', 'read_battery','read_charge']


new_access = client.exchange_code('put code here')


print(new_access)
file = open('tokens.txt', 'wb')
pickle.dump(new_access, file)
file.close()



