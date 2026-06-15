import scrapy

class MyspiderSpider(scrapy.Spider):
    name = "myspider"

    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.css(".quote"):
            yield {
                "text": quote.css(".text::text").get(),
                "author": quote.css(".author::text").get(),
            }