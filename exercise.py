import requests
import json

ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')
body = ottawa_wards_response.json()


for i in range(len(body['objects'])):
    print(body['objects'][i]['name'])
