import scrapy

class TestSpider(scrapy.spiders.Spider):
    name = "test"
    allowed_domains= ["duobao.alibaba9.com/"]
    start_urls = [
        "http://duobao.alibaba9.com/"
    ]

    def parse(self, response):
        filename = "testFile"
        with open(filename, "wb") as f:
            f.write(response.body)
