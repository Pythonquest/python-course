# Demo of Beautiful Soup web scraping
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

url = 'https://feeds.fireside.fm/bibleinayear/rss'

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

xml = soup(webpage, 'xml')


for item in xml.findAll('itunes:subtitle'):
    print(item.text)

