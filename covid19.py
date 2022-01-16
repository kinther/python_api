# Testing random internet REST API's

import requests
import json

# define requests data
url = "https://covid19-api.com/country?name=USA"

headers = {
    'accept': "application/json"
    }

# actually pull the data
r = requests.request("GET", url, headers=headers)

# change data to dict format
data = json.loads(r.text)

# present json data in json format
print(json.dumps(data[0], indent=4, sort_keys=True))