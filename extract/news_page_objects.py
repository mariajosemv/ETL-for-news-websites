import requests
import bs4

## puntos: 3167

from common import config


class NewsPage:

    def __init__(self, news_site_uid, url):  # news_site_uid = elpais, elunivesal
        self._config = config()['news_sites'][news_site_uid] # execute config() for for elpais, el universal,
        self._queries = self._config['queries'] # execute the query
        self._html = None
        self._url = url

        self._visit(url) # do the request


    def _select(self, query_string):
        return self._html.select(query_string)


    def _visit(self, url):
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'

        self._html = bs4.BeautifulSoup(response.text, 'html.parser')


class HomePage(NewsPage):  # represents the home page

    def __init__(self, news_site_uid, url):
        super().__init__(news_site_uid, url)

    @property
    def article_links(self):
        link_list = []
        title_list = []
        for link in self._select(self._queries['homepage_article_links']):
            if link and link.has_attr('title'):
                title_list.append(link)

            if link and link.has_attr('href'):
                link_list.append(link)

        return set(link['href'] for link in link_list)


class ArticlePage(NewsPage):

    def __init__(self, news_site_uid, url):
        super().__init__(news_site_uid, url)

    @property
    def url(self):
        return self._url


    @property
    def body(self):
        result = self._select(self._queries['article_body'])
        return result[0].text if len(result) else '' 

    @property
    def title(self):
        result = self._select(self._queries['article_title'])
        return result[0].text if len(result) else '' 
 