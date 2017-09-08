import requests
from bs4 import BeautifulSoup
import re


def download_logs(url):
    soup = BeautifulSoup(
        requests.get(url).text,
        'lxml'
    )
    links = soup.find_all(
        'a',
        string=re.compile('Logs.*')
    )
    return [a['href'] for a in links]


def get_nicks_report(text):
    nicks = set()
    lines = dict()
    words = dict()

    for line in text.split('\n')[1:-1]:
        fragments = line.split(" ")
        nick = fragments[1]
        nick = nick[1:-1]
        if nick not in nicks:
            nicks.add(nick)
            lines[nick] = 1
            words[nick] = len(fragments[2:])
        else:
            lines[nick] += 1
            words[nick] += len(fragments[2:])

    print("I have found {} nicks".format(len(nicks)))
    print("\n".join(
        ["{} has written {} word(s) in {} line(s)".format(
            nick,
            words[nick],
            lines[nick]
        ) for nick in nicks]
    ))


if __name__ == "__main__":
    url = "https://dgplug.org/irclogs/2017/"
    log_links = download_logs(url)
    for link in log_links:
        logfile = requests.get(url + link).text
        print()
        print('-' * 16)
        print('Report for log {}'.format(logfile))
        get_nicks_report(logfile)
