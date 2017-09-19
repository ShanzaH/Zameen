import scrapy
from zameen_scrape.items import ZameenScrapeItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'en-US,en;q=0.8',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/60.0.3112.101 Safari/537.36'
           }

class Zameen(scrapy.Spider):
    name = "zameenspider"
    allowed_domains = ['zameen.com']
    start_urls = ['https://www.zameen.com/']

def parse(self, response):
    yield [scrapy.FormRequest( method='GET',headers=headers,
                              formdata={'tab_city':'Lahore','tab_type':'Houses','sb_sl_btn r':{'buy','rent'}},
                              callback=self.parse_item)]

def parse_item(self, response):
    if 'https://www.zameen.com/Property/':
        yield [scrapy.Request( method='GET',headers=headers, callback=self.parse_items)]

def parse_items(self, response):
    item = ItemLoader(ZameenScrapeItem(), response)
    item.add_xpath('title', '//div[contains(@class,"pr_title")]/h1/text()')
    item.add_xpath('address', '//div[contains(@class,"pr_title")]/h2/text()')
    item.add_xpath('price', '//span[contains(@class,"price")]/font/text()')
    item.add_xpath('phone', '//span[@class="l pv_data ltr txtfont"]/text()', TakeFirst())
    item.add_xpath('category', '//div[4]/span[contains(@class, "value")]/span/text()',
                    MapCompose(lambda v: v.partition(' ')[2:]))
    item.add_xpath('bedrooms', '//div[5]/span[contains(@class, "value")]/text()')
    item.add_xpath('posted_on', '//div[9]/span[contains(@class, "value")]/text()')
    item.add_xpath('area', '//div[7]/span/font/text()')

    yield item.load_item()
