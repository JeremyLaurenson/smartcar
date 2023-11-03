# Step 1: Install smartcar python library by running:    pip install smartcar
# Step 2: Create an account, and register a new app to the smartcar.com dashboard
# Step 3: When you register a new app, youll get a clientID, Client Secret from the smartcar.com dashboard

import smartcar
import time
import pickle


client = smartcar.AuthClient('your-client-id-here','your-client-secret-here','http://localhost/smartcar/redirect/','live')

# Alter this list to specify the scope of permissions your application is requesting access to
scopes = ['read_vehicle_info', 'read_battery','read_charge']

# Generate auth url for User OAuth flow
auth_url = client.get_auth_url(scopes)
print(auth_url)

