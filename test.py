# Testing random internet REST API's

import requests
import json

url = "https://covid19-api.com/country?name=USA&format=json"

headers = {
    'accept': "application/json"
    }


# actually pull the data
r = requests.request("GET", url, headers=headers)

# present data in JSON format
print(type(r))