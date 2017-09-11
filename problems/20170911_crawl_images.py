import requests
import os
from bs4 import BeautifulSoup


def save_all_images(url):
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    images = soup.find_all('img')
    for image in images:
        image_link = os.path.join(url, image['src'])
        image_filename = os.path.basename(image_link)
        image_raw = requests.get(image_link).content
        with open(image_filename, 'bw') as outstream:
            outstream.write(image_raw)
