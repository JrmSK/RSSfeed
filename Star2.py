from bottle import route, run, static_file
from random import randint
import json
import feedparser
import ssl

# I found this fix online to tackle the SSL issue
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

feed = feedparser.parse("https://www.engadget.com/rss.xml")


@route('/')
def index():
    return static_file("main.html", root='')


@route('/getFeed')
def headline():
    my_list = []
    r = randint(0, len(feed["entries"]) - 10)
    for i in range(r, r + 10):
        title = feed["entries"][i]["title"]
        link = "<a href='" + feed["entries"][i]["link"] + "'> article </a>"
        my_list.append({"title": title, "link": link})
    return json.dumps(my_list)


def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()
