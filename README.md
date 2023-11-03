# smartcar
Simple scripts for getting car status from smarter.com

This is a very bare bones implimentation for someone else to take and run with. Smartcar.com allows you to set up a single user license and go query their api (300 times a month) for your car data. This, for VW cars, includes battery and charging status.

To get this working:

1... Install the smartcar library for python by executing: pip install smartcar
2... Go to smartcar.com and sign up for an account
3... On smartcar.com create a new application, and note the client id and client secret.
4... *.py files put your client id and secret into the appropriate areas
5... Execute auth_step0.py in order to get an authentiction URL. This would normally be the URL you would send your user to.
6... Copy and paste that URL into your browser, but be sure to change the "test" mode to "live" mode in the URL it returns eg:
https://connect.smartcar.com/oauth/authorize?response_type=code&client_id=blahblah&redirect_uri=http%3A%2F%2Flocalhost%2Fsmartcar%2Fredirect%2F&approval_prompt=auto&scope=read_vehicle_info+read_battery+read_charge&mode=test becomes
https://connect.smartcar.com/oauth/authorize?response_type=code&client_id=blahblah&redirect_uri=http%3A%2F%2Flocalhost%2Fsmartcar%2Fredirect%2F&approval_prompt=auto&scope=read_vehicle_info+read_battery+read_charge&mode=live
      This will take you through the user authentication phase and allow you to select your car and authorize your app to read it.
7... Edit the auth_step1.py file and use the returned CODE part of the URL to populate the 'put code here' section
8... Execute auth_step1.py   This will save the authentication and refresh tokens used to access your car via smartcar.com from here on out.
9... Execute refreshtoken.py at least once every 2 hours to exchange your authen tication tokens for fresh ones.
10.. Execute check_ev_charge.py to go get the charge status and battery charge level from your car. I do this at 8:30PM each day to check that its plugged in and charging

