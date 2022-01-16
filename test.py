# Testing random internet REST API's

import requests
import json

# define requests data
url = "https://covid19-api.com/country?name=USA&format=json"

headers = {
    'accept': "application/json"
    }

# actually pull the data
r = requests.request("GET", url, headers=headers)

# change data to dict format
data = json.loads(r.text)
data = data[0]

# present json data
print(json.dumps(data, indent=4, sort_keys=True))