import falcon
from resource import PageResource, TagResource #, SiteResource, KeywordResource
import requests
import json
import time
import threading
import configparser


def post_to_api_apge_new(slack_url):
    response = requests.post('http://localhost:8000/api/page/new')
    pages = response.json()

    pages = [page for page in pages if 'url' in page]
    print(pages)

    for page in pages:
        time.sleep(3)
        url = slack_url
        data = json.dumps({
            'text':  page['title'] + '\n'+ page['url'],
            'unfurl_links': 'true'
        })

        response = requests.post(url, data=data)
        print(response.text)

    t=threading.Timer(1800, post_to_api_apge_new)
    t.start()


api = falcon.API()

api.add_route('/api/page', PageResource())
api.add_route('/api/page/{order}', PageResource())
api.add_route('/api/tag', TagResource())

inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')

slack_url = inifile.get('slack', 'url')
if slack_url:
    t=threading.Thread(target=post_to_api_apge_new, args=(slack_url,))
    t.start()



#api.add_route('/api/keyword', KeywordResource())
