import scrapy


class OnlinerSpider(scrapy.Spider):
    name = 'onliner'
    start_urls = ['https://catalog.onliner.by']

    def parse(self, response, **kwargs):
        categories = response.css('div.catalog-navigation-list__category')
        categories_number = range(1, 10)
        for category in categories:
            try:
                if int(category.attrib['data-id']) in categories_number:
                    links = category.css('a.catalog-navigation-list__dropdown-item::attr(href)').getall()
                    print(links, '\n')
            except ValueError:
                pass
