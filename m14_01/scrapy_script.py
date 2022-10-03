import re
from datetime import datetime

import scrapy
from scrapy.crawler import CrawlerProcess

next_links = ['/month.php?month=2022-08', '/month.php?month=2022-07', '/month.php?month=2022-06',
              '/month.php?month=2022-05', '/month.php?month=2022-04', '/month.php?month=2022-03',
              '/month.php?month=2022-02']


class GetDataSpider(scrapy.Spider):
    name = 'get_data'
    allowed_domains = ['index.minfin.com.ua']
    start_urls = ['https://index.minfin.com.ua/ua/russian-invading/casualties']
    custom_settings = {"FEED_FORMAT": "csv", "FEED_URI": "result.csv", "FEED_EXPORT_ENCODING": 'utf-8'}

    def parse(self, response):
        result = {}
        for element in response.css('ul[class=see-also] li[class=gold]'):
            date = element.xpath('span/text()').get()
            try:
                date = datetime.strptime(date, "%d.%m.%Y").isoformat()
                print(date)
            except ValueError:
                print(f'Error for {date}')
                continue

            result.update({"date": date})
            losses = element.xpath('div[@class="casualties"]/div/ul/li')
            for l in losses:
                # print(' '.join(l.css('*::text').extract()).split("—"))
                title, quantity = ' '.join(l.css('*::text').extract()).split("—")
                title = title.strip()
                quantity = re.search(r"\d+", quantity).group()
                result.update({title: int(quantity)})
            yield result

        for next_link in next_links:
            yield scrapy.Request(url=self.start_urls[0] + next_link)


# run spider
process = CrawlerProcess()
process.crawl(GetDataSpider)
process.start()
