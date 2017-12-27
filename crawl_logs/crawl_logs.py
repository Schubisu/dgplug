from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import sys
import os


def save_log(url, path, overwrite=False):
    if os.path.exists(path) and not overwrite:
        return
    print("Saving log: {}".format(url.split('/')[-1]))
    r = requests.get(url)

    with open(path, 'w') as outfile:
        outfile.write(r.text)


def browse_folder(url, path):
    print("Now browsing: {}".format(url.split('/')[-2]))
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except PermissionError as e:
            print("Error: You're not allowed to write here")
            return

    response = urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    links = [a['href'] for a in soup.find_all('a')]
    if len(links) > 5:
        for link in links[5:]:
            if link[-3:] in ["txt", "log"]:
                save_log(
                    url + link,
                    os.path.join(path, link)
                )
            elif link[-1] == "/":
                browse_folder(
                    url + link,
                    os.path.join(path, link.strip('/'))
                )
            else:
                print("Unknown file format: {}".format(link))


if __name__ == "__main__":
    path = ""
    base_url = 'https://www.dgplug.org/irclogs/'

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = os.path.curdir
    browse_folder(base_url, path)
