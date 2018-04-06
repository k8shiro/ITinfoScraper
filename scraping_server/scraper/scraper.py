from pymongo import MongoClient
from datetime import datetime
from janome.tokenfilter import *
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer


class Scraper:
    def __init__(self):
        self.db = MongoClient('mongo', 27017).page_db
        self.page_collection = self.db.page_collection
        self.tag_collection = self.db.tag_collection
        self.site = ""
        self.top_url = ""


    def load_new_pages(self):
        pass



    def save_page(self, page):
        page = self.add_tag_to_page(page)
        page['created_at'] = datetime.now()
        result = self.page_collection.update(
            {'url': page['url']},
            {'$setOnInsert': page},
            upsert=True
        )

        if result['updatedExisting']:
            return {'error': 'This page is already registered'}
        else:
            return page



    def load_pages(self, searching_option=None):
        pages = list(self.page_collection.find(searching_option))
        return pages

    def create_page_searching_option(self, params):
        #searching_option = {'created_at': {'$gt': one_day_ago}}
        #{'$and': [{'age': {'$gt': 20}}, {'name': {'$regex': '^b'}}]}
        searching_option = {'$and': [ {'_id':{'$exists':True}} ]}

        if 'title' in params:
            searching_option['$and'].append({'title': {'$regex': params['title']}})

        if 'url' in params:
            searching_option['$and'].append({'url': {'$regex': params['url']}})

        if 'site' in params:
            searching_option['$and'].append({'site': params['site']})

        if 'type' in params:
            searching_option['$and'].append({'type': params['type']})

        if 'tag' in params:
            tags = params['tag'].split(',')
            searching_option['$and'].append({'tag': {'$all': tags}})

        return searching_option

    def add_tag_to_page(self, page):
        tokenizer = Tokenizer()
        token_filters = [CompoundNounFilter(),POSKeepFilter(['名詞,固有名詞'])]
        analyzer = Analyzer([], tokenizer, token_filters)
        extracted_tags = [token.surface for token in analyzer.analyze(page['title'])]

        tag_names = [ tag['name'] for tag in self.load_tags() ]
        saved_tags = [ tag_name for tag_name in tag_names if tag_name.lower() in page['title'].lower() ]

        new_tags = list(set(extracted_tags) - set(saved_tags))
        for tag in new_tags:
            tag = {'name': tag}
            self.save_tag(tag)

        page_tags = list(set(extracted_tags) | set(saved_tags))
        page['tag'] = page_tags

        return page

    def save_tag(self, tag):
        if not 'description' in tag:
            tag['description'] = ""

        result = self.tag_collection.update(
            {'name': tag['name']},
            {'$setOnInsert': tag},
            upsert=True
        )

        if result['updatedExisting']:
            return {'error': 'This tag is already registered'}
        else:
            return tag

    def load_tags(self, searching_option=None):
        tags = list(self.tag_collection.find(searching_option))
        return tags
