# -*- coding: utf-8 -*-
import sys
import os
import time

from scrapy.cmdline import execute

class Start():

    def __init__(self):
        self.log_path = conf.log_path

    def run(self):
        log_path = self.log_path + '/LyPcHotelInfoSpider/spider_log_' + str(int(time.time()))
        dir_path = self.log_path + r'/LyPcHotelInfoSpider'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        sys.argv = ["scrapy", "crawl", "LyPcHotelInfoSpider","--logfile="+log_path]
        execute()



if __name__ == '__main__':
    start = Start()
    start.run()