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
                    catalog_list = category.css('div.catalog-navigation-list__aside-item')
                    for item in catalog_list:
                        title = item.css('div.catalog-navigation-list__aside-title::text').get()
                        links = item.css('a.catalog-navigation-list__dropdown-item::attr(href)').getall()
                        yield from response.follow_all(links, callback=self.parse_link)
                        break
                    break
            except ValueError:
                pass

    def parse_link(self, response):
        div = response.css('div.schema-product')
        print(div, '\n')
