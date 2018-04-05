from pymongo import MongoClient
from datetime import datetime

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
        self.page_collection.update(
            {'url': page['url']},
            {'$setOnInsert': page},
            upsert=True
        )


    def load_pages(self, searching_option=None):
        pages = list(self.page_collection.find(searching_option))
        return pages

    def create_page_searching_option(self, searching_option=None):
        pass

    def add_tag_to_page(self, page):
        tag_names = [ tag['name'] for tag in self.load_tags() ]
        page_tags = [ tag_name for tag_name in tag_names if tag_name.lower() in page['title'].lower() ]
        page['tag'] = page_tags
        return page

    def save_tag(self, tag):
        if not 'description' in tag:
            tag['description'] = ""

        self.tag_collection.update(
            {'name': tag['name']},
            {'$setOnInsert': tag},
            upsert=True
        )

    def load_tags(self, searching_option=None):
        tags = list(self.tag_collection.find(searching_option))
        return tags
