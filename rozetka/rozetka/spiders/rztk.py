import scrapy


class RztkSpider(scrapy.Spider):
    name = "rztk"
    allowed_domains = ["rozetka.com.ua"]
    start_urls = ["https://rozetka.com.ua/umnoe-osveshchenie/c4638351/"]

    def parse(self, response):
        smart_light = response.css('div.goods-tile__content')
        for light in smart_light:
            yield {'name': light.css('span.goods-tile__title::text').get(),
                   'price': f'{light.css('span.goods-tile__price-value::text').get()}'
                            f' {light.css('span.currency::text').get()}',
                   'url': light.css('a.product-link').attrib['href']}
