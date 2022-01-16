# Testing random internet REST API's

import requests
import json

# actually pull the data
r = requests.get("https://covid19-api.com/country?name=USA&format=json")

# present data in JSON format
data = json.loads(r.json())
print(json.dumps(data, indented=4, sort_keys=True))