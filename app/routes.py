from app import app
from flask import render_template, url_for
from GetData.GetTSVideoLink import getVideoLink
from GetData.GetHNNewsdata import getHNArticles
from GetData.GetDWNews import getDWArticles
from GetData.GetSpiegelNews import getSpiegelArticles

@app.route("/")
@app.route('/ts')
def ts():
    video_ts, video_url = getVideoLink()
    return render_template('ts.html', title='Tagesschau', video_ts=video_ts, video_url=video_url)

@app.route('/hn')
def hn():
    articles = getHNArticles()
    return render_template('hn.html', title='Hacker News', articles=articles)

@app.route('/dw')
def dw():
    articles = getDWArticles()
    return render_template('dw.html', title='Deutsche Welle', articles=articles)

@app.route('/spiegel')
def spiegel():
    articles = getSpiegelArticles()
    return render_template('spiegel.html', title='Spiegel', articles=articles)