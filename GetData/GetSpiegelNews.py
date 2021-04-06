import requests
from xml.etree import ElementTree

def getNews(url_type):
    if url_type == 'top':
        response = requests.get("https://www.spiegel.de/schlagzeilen/tops/index.rss")
        xml = ElementTree.fromstring(response.content)
        return xml
    elif url_type == 'wirtschaft':
        response = requests.get("https://www.spiegel.de/wirtschaft/index.rss")
        xml = ElementTree.fromstring(response.content)
        return xml


def getSpiegelArticles():
    url_types = ['top', 'wirtschaft']
    articles = {}
    for url_type in url_types:
        response = getNews(url_type)[0]
        items = response.findall("item")
        details = [{"title": i.find('title').text,
                    "description": i.find('description').text,
                    "url": i.find('link').text
                    } for i in items]
        articles[url_type] = details
    return articles
