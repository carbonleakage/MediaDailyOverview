from requests_html import HTMLSession
import re

def getVideoLink():
    url = "https://www.tagesschau.de/100sekunden/"

    session = HTMLSession()
    response = session.get(url)

    timestamp = response.html.find(".multimediahead__date", first=True)
    video_ts = timestamp.text
    latest_link =  response.html.find("meta[@name='twitter:player:stream']", first=True)

    pattern = 'media.tagesschau.de(.*).hi.mp3'
    video_url_core = re.search(pattern, latest_link.attrs['content']).group(1)
    video_url = "https://media.tagesschau.de/" + video_url_core + ".webm.h264.mp4"

    return video_ts, video_url
