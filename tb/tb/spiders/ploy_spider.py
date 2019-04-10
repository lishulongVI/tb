import scrapy
from urllib import parse


class PloySpider(scrapy.Spider):
    name = "ploy"

    def start_requests(self):
        urls = [
            "https://www.taobao.com/markets/nvzhuang/taobaonvzhuang",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        file_name = parse.urlsplit(response.url).path.replace('/', '_')
        with open('{}.html'.format(file_name), 'wb') as file:
            file.write(response.body)
            self.log(' save info file name:{}'.format(file_name))
        # print(response.body)


if __name__ == '__main__':
    a = parse.urlsplit('https://www.taobao.com/markets/nvzhuang/taobaonvzhuang')
    print(a.path)
    a = parse.urlparse('https://www.taobao.com/markets/nvzhuang/taobaonvzhuang')
    print(a)
