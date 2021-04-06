import requests
from xml.etree import ElementTree

def getNews(url_type):
    response = requests.get(f"https://rss.dw.com/rdf/rss-en-{url_type}")
    xml = ElementTree.fromstring(response.content)
    return xml

def getDWArticles():
    url_types = ['top', 'ger']
    articles = {}
    for url_type in url_types:
        response = getNews(url_type)
        items = response.findall("{http://purl.org/rss/1.0/}item")
        details = [{"title": i.find('{http://purl.org/rss/1.0/}title').text,
                    "description": i.find('{http://purl.org/rss/1.0/}description').text,
                    "url": i.find('{http://purl.org/rss/1.0/}link').text
                    } for i in items]
        articles[url_type] = details
    return articles
    # for child in response:
    #     print(child.findall("{http://purl.org/rss/1.0/}item"))
