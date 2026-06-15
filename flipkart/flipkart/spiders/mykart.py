import scrapy


class MykartSpider(scrapy.Spider):
    name = "mykart"
    allowed_domains = ["flipkart.com"]
    start_urls = ["https://www.flipkart.com/search?q=iphone"]

    def parse(self, response):
        products = response.css("div._1AtVbE")

        for product in products:
            yield {
                "title": product.css("div._4rR01T::text").get(),
                "price": product.css("div._30jeq3::text").get(),
                "rating": product.css("div._3LWZlK::text").get(),
            }
