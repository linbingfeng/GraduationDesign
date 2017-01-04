# -*- coding: utf-8 -*-
import time
from pymongo import MongoClient
from trip_data_spider.utils.MongoDBUtil import MongodbUtil

class HotelCityDistribution():
    client = MongoClient('127.0.0.1', 27017)  # 连接服务器
    db = client['spider']  # 连接数据库
    collection = db["ly_pc_hotel"]  # 连接collection
    mongo = MongodbUtil()

    def run(self):
        hotel_num = self.collection.count()
        one_city = [u'北京',u'上海',u'广州',u'深圳']
        two_city = [u'天津',u'南京',u'武汉',u'沈阳',u'西安',u'重庆',u'杭州',u'青岛',u'大连',u'宁波',u'济南',u'哈尔滨',u'长春',u'厦门',u'郑州',u'长沙',u'福州',u'乌鲁木齐',u'昆明',u'兰州',u'苏州',u'无锡',u'南昌',u'贵阳',u'南宁',u'合肥',u'太原',u'石家庄',u'呼和浩特',u'佛山',u'东莞',u'唐山',u'烟台',u'泉州',u'包头']
        city_item = {
            "hotel_num":hotel_num,
            "one_city_num" :0,
            "two_city_num": 0,
            "other_city_num": 0,
            "time":time.strftime("%Y-%m-%d",time.localtime())
        }
        one_price_item = {
            "type":1,
            "hotel_num":0,
            "height_num": 0,
            "middle_num": 0,
            "low_num": 0,
            "time": time.strftime("%Y-%m-%d", time.localtime())
        }
        two_price_item = {
            "type": 2,
            "hotel_num": 0,
            "height_num": 0,
            "middle_num": 0,
            "low_num": 0,
            "time": time.strftime("%Y-%m-%d", time.localtime())
        }
        other_price_item = {
            "type": 3,
            "hotel_num": 0,
            "height_num": 0,
            "middle_num": 0,
            "low_num": 0,
            "time": time.strftime("%Y-%m-%d", time.localtime())
        }
        for hotel in self.collection.find():
            if hotel["city_name"] in one_city:
                city_item["one_city_num"] = city_item["one_city_num"] + 1
                if hotel["price"] != 0:
                    one_price_item["hotel_num"] = one_price_item["hotel_num"] + 1
                    if hotel["price"] < 100:
                        one_price_item["low_num"] = one_price_item["low_num"] + 1
                    elif hotel["price"] >= 100 and hotel["price"] < 300:
                        one_price_item["middle_num"] = one_price_item["middle_num"] + 1
                    else:
                        one_price_item["height_num"] = one_price_item["height_num"] + 1
            elif hotel["city_name"] in two_city:
                city_item["two_city_num"] = city_item["two_city_num"] + 1
                if hotel["price"] != 0:
                    two_price_item["hotel_num"] = two_price_item["hotel_num"] + 1
                    if hotel["price"] < 100:
                        two_price_item["low_num"] = two_price_item["low_num"] + 1
                    elif hotel["price"] >= 100 and hotel["price"] < 300:
                        two_price_item["middle_num"] = two_price_item["middle_num"] + 1
                    else:
                        two_price_item["height_num"] = two_price_item["height_num"] + 1
            else:
                city_item["other_city_num"] = city_item["other_city_num"] + 1
                if hotel["price"] != 0:
                    other_price_item["hotel_num"] = other_price_item["hotel_num"] + 1
                    if hotel["price"] < 100:
                        other_price_item["low_num"] = other_price_item["low_num"] + 1
                    elif hotel["price"] >= 100 and hotel["price"] < 300:
                        other_price_item["middle_num"] = other_price_item["middle_num"] + 1
                    else:
                        other_price_item["height_num"] = other_price_item["height_num"] + 1
        self.mongo.write(city_item,'ly_hotel_city_distribution')
        self.mongo.write(one_price_item, 'ly_hotel_price_distribution')
        self.mongo.write(two_price_item, 'ly_hotel_price_distribution')
        self.mongo.write(other_price_item, 'ly_hotel_price_distribution')

if __name__ == '__main__':
    HotelCityDistribution().run()