# -*- coding: utf-8 -*-
from scrapy import spider

class LyPcHotelInfoSpider(spider):

    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)