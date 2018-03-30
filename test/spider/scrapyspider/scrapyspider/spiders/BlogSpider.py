from scrapy.spider import Spider


class BlogSpider(Spider):
    name = "first_blog"
    start_urls = ["http://woodenrobot.me"]

    def parse(self, response):
        titles = response.xpath(
            '//a[@class="post-title-link"]/text()').extract()
        for title in titles:
            print(title.strip())
