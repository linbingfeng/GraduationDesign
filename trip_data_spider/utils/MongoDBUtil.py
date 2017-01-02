# -*- coding: utf-8 -*-
from pymongo import MongoClient

class MongodbUtil(object):

    def __init__(self):
        self.client = MongoClient('127.0.0.1',27217)#连接服务器
        self.db = self.client['spider']#连接数据库
        self.collection = self.db['ly_pc_hotel']#连接collection

    def write(self,item):
        '''向mongoDB写入一条数据'''
        self.collection.insert(item)

    def delete(self):
        '''删除mongoDB中的collection'''
        self.collection.drop()