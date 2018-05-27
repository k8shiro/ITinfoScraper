import requests
from bs4 import BeautifulSoup
from .scraper import Scraper

class ConnpassScraper(Scraper):
    def __init__(self):
        super().__init__()
        self.site = "connpass"
        self.top_url = "https://connpass.com/"


    def load_new_pages(self):
        url = 'https://connpass.com/api/v1/event/'
        headers = {
                'content-type': 'application/json'
        }
        params = {
                'order': '1',
                'count': '50'
        }

        response = requests.get(url, headers=headers,params=params)
        events = response.json()['events']

        pages = []
        for event in events:
            if event['limit'] == None or event['limit'] < 40:
                continue

            page = {
                'title': event['title'],
                'type': "event",
                'url': event['event_url'],
                'site': self.site,
            }

            pages.append(page)

        return pages







if __name__ == '__main__':
    page = ThinkitScraper()
    page.load_new_pages()
