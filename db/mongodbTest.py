#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#Created by crazystone
from pymongo import MongoClient
import json

def query(spider):
    results = spider.find({})
    for result in results:
        print(result)

def connect():
    client = MongoClient('localhost',27017)
    db = client['bluecoor']
    spider = db.spider
    return spider

def insert(spider):
    jsonArray = []
    for i in range(10):
        aDict = {}
        aDict['name'] = 'name' + str(i)
        aDict['address'] = 'beijing'
        spider.insert(aDict)
        # jsonArray.append(aDict)
    # spider.insert_many(jsonArray)
def update(spider):
    spider.update({'name':'name9'},{'$set':{'address':0}},upsert = False,multi = True)


def main():
    spider = connect()
    insert(spider)
    query(spider)
    update(spider)
    query(spider)

if __name__ == '__main__':
    main()