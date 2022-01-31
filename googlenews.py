# Imports
from GoogleNews import GoogleNews
import argparse  # because I'm not going to leave my api key in the wild on github

# data strcutures
links = []

# gather argparse data
parser = argparse.ArgumentParser()
parser.add_argument('--search', type=str, required=True)
args = parser.parse_args()

# define GoogleNews criteria
gn = GoogleNews()
gn.set_lan('en')
gn.set_period('30m')
gn.set_encode('utf-8')
gn.get_news(args.search)
r = gn.results()

# parse news data for links
for entry in r:
    links.append(entry['link'])

# print links learned
print(links)
