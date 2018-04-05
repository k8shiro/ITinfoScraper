import requests
from bs4 import BeautifulSoup
from .scraper import Scraper

class ThinkitScraper(Scraper):
    def __init__(self):
        super().__init__()
        self.site = "Think IT"
        self.top_url = "https://thinkit.co.jp/"


    def load_new_pages(self):
        html = requests.get(self.top_url)
        soup = BeautifulSoup(html.text, 'lxml')
        selector = '.view-new-arrivals > div:nth-of-type(1) > div:nth-of-type(1)'
        elems = soup.select(selector)[0].find_all('h2')

        pages = []
        for elem in elems:
            page = {
                'title': elem.a.string,
                'type': "media",
                'url': "{}{}".format(self.top_url,elem.a.get('href')),
                'site': self.site,
            }

            pages.append(page)

        return pages







if __name__ == '__main__':
    page = ThinkitScraper()
    page.load_new_pages()
