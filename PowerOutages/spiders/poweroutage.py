import scrapy
from scrapy_splash import SplashRequest
from urllib.parse import urljoin
import json

class PowerOutage(scrapy.Spider):
    name = "power"

    def start_requests(self):
        webpage = "https://poweroutage.us/area/state/"

        # States saved in json file
        with open('../docs/states.json') as f:
            states = json.load(f)
            for state in states:
                page = urljoin(webpage, state["name"])
                yield SplashRequest(url=page, callback=self.parse, endpoint='render.html', args={'wait': 2})

    def parse(self, response):
        yield {
            'State': self.states(response),
            "Electric Providers": self.electric_providers(response)
        }
    
    def states(self, response):
        return response.selector.xpath('//div[@class="row"]/div/h1/text()').get()

    def electric_providers(self, response):
        entries = []
        # Skips first table row (title)
        for entry in response.selector.xpath('/html/body/div[2]/table[1]/tbody/tr[position() > 1]'):
            entries.append({
                "Provider": entry.xpath('.//td[1]/a/text()').get(),
                "Customers Tracked": entry.xpath('.//td[2]/text()').get(),
                "Customers Out": entry.xpath('.//td[4]/text()').get()
            })
        return entries



