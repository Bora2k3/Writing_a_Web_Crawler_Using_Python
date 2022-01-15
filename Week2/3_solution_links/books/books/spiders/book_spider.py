# scrapy crawl books -o result.csv -t csv && python csv_to_txt.py
from w3lib.url import url_query_cleaner
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


def process_links(links):
    for link in links:
        link.url = url_query_cleaner(link.url)
        yield link


class ImdbCrawler(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    rule = Rule(LinkExtractor(),
                callback='parse_item',
                follow=True,
                process_links=process_links
                )
    rules = (rule,)

    def parse_item(self, response):
        return {'url': response.url}
