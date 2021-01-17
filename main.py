from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
import json


def scrape(request):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
        reg_url = "https://technews.acm.org"
        req = Request(url=reg_url, headers=headers)
        html = urlopen(req).read()
        # print(html)
        page_soup = soup(html, features="html.parser")
        containers = page_soup.find_all("b")
        names = page_soup.findAll("li")
        n, l = [], []
        dictionary = {}
        ss = []
        # print(soup.prettify(containers[0]))
        for container in containers:
            tags = container.find_all("a")
            if len(tags) > 0:
                for tag in tags:
                    l.append(tag.get('href', None))
        for name in names:
            tags = name.find_all("a")
            if len(tags) > 0:
                for tag in tags:
                    n.append(tag.encode_contents())
        # imgs = page_soup.find_all("img")
        # print(len(imgs))
        i = 0
        while(len(n) > 0):
            dictionary.update({i: str(n.pop())})
            i += 1
            dictionary.update({i: l.pop()})
            i += 1
        # dictionary.update(ss)
        # print(dictionary)
        # Serializing json
        # print(i)
        json_object = json.dumps(dictionary, indent=len(dictionary))
        with open("store.json", "w") as outfile:
            outfile.write(json_object)
        # print("json dump done")
        return dictionary
    except Exception as e:
        return e


print(scrape(0))
