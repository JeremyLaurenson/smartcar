# smartcar
Simple scripts for getting car status from smarter.com
By Jeremy Laurenson
Please include attribition if you reuse this kernel of code.

I use this to remind us at 8:30P if the car isnt charged up past 70% and isnt currently charging.

This is a very bare bones implimentation for someone else to take and run with. Smartcar.com allows you to set up a single user license and go query their api (300 times a month) for your car data. This, for VW cars, includes battery and charging status.

To get this working:
<UL>
<LI>Install the smartcar library for python by executing: pip install smartcar</LI>
<LI>Install the pickle library for python by executing: pip install pickle</LI>
<LI>Go to smartcar.com and sign up for an account</LI>
<LI>On smartcar.com create a new application, and note the client id and client secret.</LI>
<LI>*.py files put your client id and secret into the appropriate areas (I know about includes but I rushed this)</LI>
<LI>Execute auth_step0.py in order to get an authentiction URL. This would normally be the URL you would send your user to.</LI>
<LI>Copy and paste that URL into your browser, but be sure to change the "test" mode to "live" mode in the URL it returns eg:
<BR><PRE>https://connect.smartcar.com/oauth/authorize?response_type=code&client_id=blahblah&redirect_uri=http%3A%2F%2Flocalhost%2Fsmartcar%2Fredirect%2F&approval_prompt=auto&scope=read_vehicle_info+read_battery+read_charge&mode=test</PRE> becomes
<BR><PRE>https://connect.smartcar.com/oauth/authorize?response_type=code&client_id=blahblah&redirect_uri=http%3A%2F%2Flocalhost%2Fsmartcar%2Fredirect%2F&approval_prompt=auto&scope=read_vehicle_info+read_battery+read_charge&mode=live</PRE>
<BR>      This will take you through the user authentication phase and allow you to select your car and authorize your app to read it and redirect you ro a new URL... the code part of that url is what youre looking for</LI>
<LI>7... Edit the auth_step1.py file and use the returned CODE part of the URL to populate the 'put code here' section</LI>
<LI>8... Execute auth_step1.py   This will save the authentication and refresh tokens used to access your car via smartcar.com from here on out.</LI>
<LI>9... Execute refreshtoken.py at least once every 2 hours to exchange your authen tication tokens for fresh ones.</LI>
<LI>10.. Execute check_ev_charge.py to go get the charge status and battery charge level from your car. I do this at 8:30PM each day to check that its plugged in and charging</LI>
</UL>
