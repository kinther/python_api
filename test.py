# Testing random internet REST API's

import requests

r = requests.get("https://covid19-api.com/country?name=USA&format=json")
print(r)