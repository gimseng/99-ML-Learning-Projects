#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import requests
import json

BASE = 'http://127.0.0.1:5000/'

field = cgi.FieldStorage()
vehicle_number = field.getvalue("vehicle_number")


response = requests.get(BASE + "vehicle/" + vehicle_number)
responseJson = json.dumps(response.json(), indent=1)

print(responseJson.replace("{", "").replace("}", ""))