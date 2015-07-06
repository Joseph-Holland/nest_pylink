#!/usr/bin/python

import sys, string
import httplib
import requests
import json

# Define hosts for http calls
emoncmshost = "localhost"

# Location of emoncms in your server, the standard setup is to place it in a folder called emoncms
# To post to emoncms.org change this to blank: ""
emoncmspath = "emoncms"

# Write apikey of emoncms account
emoncmsapikey = "<emoncms_api_key>"

# Node id youd like the emontx to appear as
nodeid = 1

emoncmsconn = httplib.HTTPConnection(emoncmshost)

# Read in json from Nest API - Your Nest API token goes here after devices?auth=
r = requests.get('https://developer-api.nest.com/devices?auth=<nest_token>')
data = r.json()

#try:
#  decoded json.loads(data)

print json.dumps(data, sort_keys=False, indent=4)
print "Ambient temperature is: ", data['thermostats']['<nest_device_id>']['ambient_temperature_c']
temp = data['thermostats']['<nest_device_id>']['ambient_temperature_c']
humidity = data['thermostats']['<nest_device_id>']['humidity']

#except (ValueError, KeyError, TypeError):
#  print "JSON format error"

# Send to emoncms
#try
print "Send data to EmonCMS"
# Send temp
emoncmsconn.request("GET", "/"+emoncmspath+"/input/post.json?apikey="+emoncmsapikey+"&node="+str(nodeid)+"&json={AmbientTempC:"+str(temp)+"}")
response = emoncmsconn.getresponse()
print "Response"
print response.status, response.reason
emoncmsconn.close()
# Send humidity
emoncmsconn.request("GET", "/"+emoncmspath+"/input/post.json?apikey="+emoncmsapikey+"&node="+str(nodeid)+"&json={Humidity:"+str(humidity)+"}")
response = emoncmsconn.getresponse()
print "Response"
print response.status, response.reason
emoncmsconn.close()