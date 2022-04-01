import scrapy

class PriceSpider(scrapy.Spider):
    name = "prices"
    
    def start_requests(self):
        urls = [
            "https://voxatcumulus.com/floorplans",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response, **kwargs):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
