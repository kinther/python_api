# Imports
from GoogleNews import GoogleNews
import base64  # convert GoogleNews links to readable format
import argparse  # what do we want to search for?

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
r = gn.results()

# parse news data for links
for entry in r:
    url = entry['link']
    url = url + 'aa'
    url = base64.b64decode(url)
    links.append(url)

# print links learned
print(links)
