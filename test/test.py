#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#Created by crazystone 

import os
import sys
import time
from datetime import datetime
from pymongo import MongoClient

# print(sys.argv) 
# os.system('notify-send \'woca\'')
startDay = datetime(2017,11,16)
month = startDay.month
day = startDay.day
hour = startDay.hour
print(month,day)
print(datetime.now())

def connectDB():
    client = MongoClient('localhost',27017)
    db = client['bluecoor']
    tableRecord = db['record']
    return tableRecord
    # pass

def test():
    tableRecord = connectDB()
    result = tableRecord.find_one()
    storeIndex = result['index']
    if storeIndex <= 9:
        os.system('notify-send \'woca\'' + str(storeIndex))
        storeIndex = storeIndex + 1
        tableRecord.update({},{'$set':{'index':storeIndex}},upsert = False,multi = False)
        pass
    else:

        pass
    # print(result['index'])

if __name__ == '__main__':
    test()
