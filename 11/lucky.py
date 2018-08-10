import sys
import webbrowser

import bs4
import requests

print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
link_elems = soup.select('.r a')
num_open = min(5, len(link_elems))
for link_idx in range(num_open):
    webbrowser.open('http://google.com' + link_elems[link_idx].get('href'))
