import json
import ast
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from scraper.scraper import Scraper
from scraper.thinkit_scraper import ThinkitScraper
from scraper.connpass_scraper import ConnpassScraper 

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
    def on_get(self, req, resp, **route):
        if not 'order' in route:
            params = req.params
            print(params)
            searching_option = self.scraper.create_page_searching_option(params)
            print(searching_option)
            pages = self.scraper.load_pages(searching_option)
            resp.body = json.dumps(pages, ensure_ascii=False, cls=mongoEncoder)
            #params = req.params
            #print(params)
            #print(params['title'])

        elif route['order']  == 'new':
            one_day_ago = datetime.now() - timedelta(days=1)
            searching_option = {'created_at': {'$gt': one_day_ago}}
            pages = self.scraper.load_pages(searching_option)
            resp.body = json.dumps(pages, ensure_ascii=False, cls=mongoEncoder)


    def on_post(self, req, resp, **route):
        if not 'order' in route:
            body = req.stream.read()
            page = json.loads(body)

            saved_page = self.scraper.save_page(page)
            resp.body = json.dumps(saved_page, ensure_ascii=False, cls=mongoEncoder)

        elif route['order']  == 'new':
            pages = []
            pages.extend(ThinkitScraper().load_new_pages())
            pages.extend(ConnpassScraper().load_new_pages())

            saved_pages = []
            for page in pages:
                saved_pages.append(self.scraper.save_page(page))

            resp.body = json.dumps(saved_pages, ensure_ascii=False, cls=mongoEncoder)

class TagResource(Resource):
    def on_get(self, req, resp, **route):
        if not 'order' in route:
            tags = self.scraper.load_tags()
            resp.body = json.dumps(tags, ensure_ascii=False, cls=mongoEncoder)



    def on_post(self, req, resp, **route):
        if not 'order' in route:
            body = req.stream.read()
            tag = json.loads(body)

            saved_tag = self.scraper.save_tag(tag)
            resp.body = json.dumps(saved_tag, ensure_ascii=False, cls=mongoEncoder)









