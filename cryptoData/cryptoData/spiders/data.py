import scrapy


class DataSpider(scrapy.Spider):
    name = 'data'
    start_urls = [
        'https://bscscan.com/token/0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
    ]
    def parse(self, response):
        block = response.css(".mb-1 span::text")
        yield block;

