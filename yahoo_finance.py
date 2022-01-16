# Testing random internet REST API's

import requests
import json
import argparse  # because I'm not going to leave my api key in the wild on github

# gather argparse data
parser = argparse.ArgumentParser()
parser.add_argument('--api_key', type=str, required=True)
parser.add_argument('--ticker', type=str, required=True)
args = parser.parse_args()

# define requests data
url = "https://yh-finance.p.rapidapi.com/stock/v2/get-summary"

params = {"symbol": args.ticker, "region": "US"}

headers = {
    'x-rapidapi-host': "yh-finance.p.rapidapi.com",
    'x-rapidapi-key': args.api_key
    }

# actually pull the data
r = requests.request("GET", url, headers=headers, params=params)

# present json data in json format
data = json.loads(r.text)
print(data)
print(type(data))