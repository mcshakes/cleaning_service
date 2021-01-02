import requests
from bs4 import BeautifulSoup
import pprint

# meta_tags = soup.find("meta", attrs={'property': "author"})


def scrape_page_metadata(url):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    pp = pprint.PrettyPrinter(indent=4)
    req = requests.get(url, headers)
    html = BeautifulSoup(req.content, "html.parser")

    metadata = {
        "title": get_title(html),
        "author": get_author(html),
        "url": url
    }

    pp.pprint(metadata)
    return metadata

# print(soup.prettify())


def get_title(html):
    # import code
    # code.interact(local=dict(globals(), **locals()))

    title = None
    if html.title.string:
        title = html.title.string
    elif html.find("meta", property="name:title"):
        title = html.find("meta", property="name:title").get("content")
    return title


def get_author(html):
    author = None

    if html.find("meta", property="author"):
        author = html.find("meta", property="author").get("content")
    return author


url = "https://www.eater.com/21551041/best-old-fashioned-cocktail-recipe"
scrape_page_metadata(url)
