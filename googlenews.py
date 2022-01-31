# Imports
from GoogleNews import GoogleNews  # get those links
from time import sleep  # to not go over rate limiting
import requests  # convert GoogleNews url to real url
import argparse  # because I'm not going to leave my api key in the wild on github

# data strcutures
links = []

# gather argparse data
parser = argparse.ArgumentParser()
parser.add_argument('--search', type=str, required=True)
args = parser.parse_args()

# define GoogleNews criteria
gn = GoogleNews()
gn.set_lang('en')
gn.set_period('30m')
gn.set_encode('utf-8')
gn.get_news(args.search)
gnr = gn.results()

# parse news data for links
for entry in gnr:
    url = entry['link']
    url = 'https://' + url
    r = requests.head(url, allow_redirects=True)
    links.append(url)
    sleep(5)

# print links learned
print(links)
