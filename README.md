# nest_pylink
Python script to query Nest API for values and input into Emoncms.

This is a simple Python script that I put together to help gather date from a Nest thermostat and input into Emoncms (http://emoncms.org/) where I can create dashboards and run reports on temperature and humidity, etc.  In order to use this you will need both a Nest thermostat and an Emoncms install.  You will also need a Nest API key and token (see here: https://developer.nest.com/documentation/api-reference).

This script queries the Nest API and pulls back both ambient temperature and humidity and then uses the Emoncms API to input these values into feeds.

By the way to code for inputting feeds was based off of the emoncms pylink script here: https://github.com/emoncms/development/blob/master/Tutorials/Python/PyLink/pylink.py

The Python may not be that great as this is my first foray into it, so I do apologise...  I'll update this over time if needed.
