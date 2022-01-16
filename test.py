# Testing random internet REST API's

import requests
import json

# actually pull the data
r = requests.get("https://covid19-api.com/country?name=USA&format=json")

# present data in JSON format
data = json.loads(r.content)

print(data)
print(type(data))

print(json.dumps(data))