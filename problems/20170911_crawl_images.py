import requests
import os
from bs4 import BeautifulSoup


def save_all_images(url):
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    images = soup.find_all('img')
    if images:
        for image in images:
            image_link = os.path.join(url, image['src'])
            image_filename = os.path.basename(image_link)
            image_raw = requests.get(image_link).content
            with open(image_filename, 'bw') as outstream:
                outstream.write(image_raw)
    else:
        try:
            image_filename = os.path.basename(url)
            image_raw = requests.get(url).content
            with open(image_filename, 'bw') as outstream:
                outstream.write(image_raw)
        except:
            print("no images found")
