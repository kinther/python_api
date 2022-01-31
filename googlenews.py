# Imports
from GoogleNews import GoogleNews
from urllib.request import urlopen
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
    i = urlopen(url)
    print(dir(i))
    print(type(i))
    # links.append(url)

# print links learned
# print(links)
