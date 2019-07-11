import scrapy
from scrapy_splash import SplashRequest

class CurrentOutages(scrapy.Spider):
    name = "current"

    def start_requests(self):
        page = "https://www.duquesnelight.com/outages-safety/current-outages"
        yield SplashRequest(url=page, callback=self.parse, endpoint='render.html', args={'wait': 2})

    def parse(self, response):
        for entry in response.selector.xpath('//table[@class="k-selectable"]/tbody/tr'):
            yield {
                'Municipality': entry.xpath('.//td[1]/text()').get(),
                'Zip Code': entry.xpath('.//td[2]/text()').get(),
                'Customers Out': entry.xpath('.//td[3]/text()').get()
            }

