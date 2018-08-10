from pathlib import Path

import bs4
import requests

url = 'http://xkcd.com'
p_base_dir = Path(__file__).parent
p_image_dir = p_base_dir.joinpath('xkcd')
p_image_dir.mkdir(exist_ok=True)

while not url.endswith('#'):
    print(f'downloading page {url}')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    comic_elem = soup.select('#comic img')

    if comic_elem:
        comic_url = 'http:' + comic_elem[0].get('src')
        print(f'downloading image {comic_url}')
        res = requests.get(comic_url)
        res.raise_for_status()
    else:
        print('not found comic image.')

    with p_image_dir.joinpath(Path(comic_url).name).open('wb') as f:
        for chunk in res.iter_content(100000):
            f.write(chunk)

    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print('complete')
