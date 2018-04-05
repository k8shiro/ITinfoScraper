import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from scraper.scraper import Scraper
from scraper.thinkit_scraper import ThinkitScraper 

class mongoEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()


class Resource:
    def __init__(self):
        self.scraper = Scraper()

class PageResource(Resource):
    def on_get(self, req, resp, **params):
        if not 'order' in params:
            pages = self.scraper.load_pages()
            resp.body = json.dumps(pages, ensure_ascii=False, cls=mongoEncoder)
        elif params['order']  == 'new':
            one_day_ago = datetime.now() - timedelta(days=1)
            searching_option = {'created_at': {'$gt': one_day_ago}}
            pages = self.scraper.load_pages(searching_option)
            resp.body = json.dumps(pages, ensure_ascii=False, cls=mongoEncoder)


    def on_post(self, req, resp, **params):
        if not 'order' in params:
            body = req.stream.read()
            page = json.loads(body)

            self.scraper.save_page(page)

        elif params['order']  == 'new':
            pages = []
            pages.extend(ThinkitScraper().load_new_pages())

            for page in pages:
                self.scraper.save_page(page)

class TagResource(Resource):
    def on_get(self, req, resp, **params):
        if not 'order' in params:
            tags = self.scraper.load_tags()
            resp.body = json.dumps(tags, ensure_ascii=False, cls=mongoEncoder)



    def on_post(self, req, resp, **params):
        if not 'order' in params:
            body = req.stream.read()
            tag = json.loads(body)

            self.scraper.save_tag(tag)









