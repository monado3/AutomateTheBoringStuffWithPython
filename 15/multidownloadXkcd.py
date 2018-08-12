import threading
from pathlib import Path

import bs4
import requests

base_dir = Path(__file__).parent
image_dir = base_dir.joinpath('xkcd')
image_dir.mkdir(exist_ok=True)


def download_xkcd(start_comic, end_comic):
    for url_num in range(start_comic, end_comic):
        print(f'downloading page http://xkcd.com/{url_num}')
        res = requests.get(f'http://xkcd.com/{url_num}')
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        comic_elem = soup.select('#comic img')
        if not comic_elem:
            print('Not found comic image')
        else:
            comic_url = 'http:' + comic_elem[0].get('src')
            print(f'downloading image {comic_url}')
            res = requests.get(comic_url)
            res.raise_for_status()

            with image_dir.joinpath(Path(comic_url).name).open('wb') as image_file:
                for chunk in res.iter_content(100000):
                    image_file.write(chunk)


download_threads = []
for i in range(1, 1400, 100):
    download_thread = threading.Thread(target=download_xkcd, args=(i, i + 100))
    download_threads.append(download_thread)
    download_thread.start()

for download_thread in download_threads:
    download_thread.join()
print('complete')
