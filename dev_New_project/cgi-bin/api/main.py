import requests
import json

BASE = 'http://127.0.0.1:5000/'

data = [{'Registration': 'MH01AV8866', 
        'Owner': 'M//S PANDURONGA TIMBLO INDUSTRIES', 
        'Maker': 'JAGUAR LAND ROVER INDIA LIMITED/ JAGUAR(XF 5.0LV8', 
        'Vehicle': 'MOTOR CAR (L)', 
        'Fuel_Type': 'PETROL', 
        'Chassis': 'SAJAAC07P8BLRXXXXX', 
        'Engine_Number': '10052323430XXXXX', 
        'Registration_Date': '22-FEB-2011', 
        'Insurance_Valid_Upto': '17-FEB-2012'
}

]

for i in range(len(data)):
    response = requests.put(BASE + "vehicle/" + data[i]['Registration'], data[i])
    print(response.json())

input()

response = requests.get(BASE + "vehicle/"+ data[0]['Registration'])

print(json.dumps(response.json(), indent=1))
