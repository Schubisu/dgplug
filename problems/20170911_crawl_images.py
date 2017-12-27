import requests
import os
from bs4 import BeautifulSoup


magic_numbers = {
    'png': ["89 50 4E 47 0D 0A 1A 0A"],
    'jpg': [
        "FF D8 FF DB",
        "FF D8 FF E0",
        "FF D8 FF E1",
    ],
}


def check_image_integrity(image_data, image_name):
    image_extension = os.path.splitext(image_name)[-1].strip('.')
    image_signatures = magic_numbers.get(image_extension, [])
    for signature in image_signatures:
        signature_int = [int(i, 16) for i in signature.split(' ')]
        if list(image_data[:len(signature_int)]) == signature_int:
            return True

    print("could not verify signature of {}".format(
        image_name
    ))
    return False


def save_image(image_data, image_filename):
    if check_image_integrity(image_data, image_filename):
        with open(image_filename, 'bw') as outstream:
            outstream.write(image_data)


def save_all_images(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'lxml')
    images = soup.find_all('img')
    if images:
        for image in images:
            image_link = os.path.join(url, image['src'])
            image_filename = os.path.basename(image_link)
            image_raw = requests.get(image_link).content
            save_image(image_raw, image_filename)

    elif 'image' in request.headers['Content-Type']:
        image_filename = os.path.basename(url)
        image_raw = requests.get(url).content
        save_image(image_raw, image_filename)

    else:
        print('no images found')


if __name__ == "__main__":
    url = "https://dgplug.org/assets/img/header.png"
    save_all_images(url)
