#!/usr/bin/python

import sys, string
import httplib
import requests
import json

# Nest API auth token.
# See here for details: https://developer.nest.com/documentation/cloud/how-to-auth
nestauthtoken = "<nest_auth_token>"

# Nest device ID.
nestdeviceid = "<nest_device_id>"

# Host you want to post to: localhost would be an
# emoncms installation on this computer, this could
# be changed to emoncms.org to post to emoncms.org.
emoncmshost = "<host>"

# Location of emoncms install on your server, the
# standard setup is to place it in a folder called emoncms
# To post to emoncms.org change this to blank: ""
emoncmspath = "emoncms"

# Write apikey of emoncms account.
emoncmsapikey = "<emoncms_api_key>"

# Node id youd like the emontx to appear from.
nodeid = 1

# Define HTTP connection to emoncms host.
emoncmsconn = httplib.HTTPConnection(emoncmshost)

try:
  # Read in json from Nest API - Your Nest API token goes here after devices?auth=
  r = requests.get('https://developer-api.nest.com/devices?auth='+nestauthtoken)
except Exception, msg:
  print "Error contacting Nest API."
  print msg
else:
  data = r.json()
  # Print data to console in JSON format.
  print json.dumps(data, sort_keys=False, indent=4)
  # Assign temperature and humidity values to new variables.
  temp = data['thermostats'][nestdeviceid]['ambient_temperature_c']
  humidity = data['thermostats'][nestdeviceid]['humidity']

  try:
    # Send to emoncms.  
    print "Send data to EmonCMS"
    # Send temp value to feed.
    emoncmsconn.request("GET", "/"+emoncmspath+"/input/post.json?apikey="+emoncmsapikey+"&node="+str(nodeid)+"&json={AmbientTempC:"+str(temp)+"}")
    response = emoncmsconn.getresponse()
    print "Response"
    print response.status, response.reason
    emoncmsconn.close()
    # Send humidity value to feed.
    emoncmsconn.request("GET", "/"+emoncmspath+"/input/post.json?apikey="+emoncmsapikey+"&node="+str(nodeid)+"&json={Humidity:"+str(humidity)+"}")
    response = emoncmsconn.getresponse()
    print "Response"
    print response.status, response.reason
    emoncmsconn.close()
  except Exception, msg:
    print "Error sending to emoncms."
    print msg
