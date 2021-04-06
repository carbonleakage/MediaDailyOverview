import requests

def getIds(url_type, posts_count=10):
    url = f"https://hacker-news.firebaseio.com/v0/{url_type}stories.json?print=pretty"
    response = requests.get(url)
    return response.json()[:posts_count]

def getPostDetails(id, return_fields=True):
    url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty"
    response = requests.get(url)
    return response.json()

def getHNArticles():
    url_types = ['top', 'ask', 'show']
    articles = {}
    for url_type in url_types:
        ids = getIds(url_type, posts_count=10)
        articles[url_type] = []
        for id in ids:
            details = getPostDetails(id)
            details_dict = {}
            details_dict["title"] = details['title']
            if "text" in details.keys():
                details_dict["text"] = details['text']
            elif "url" in details.keys():
                details_dict["url"] = details['url']
            articles[url_type].append(details_dict)
    return articles
# for article in articles['top']:
#     print(article)