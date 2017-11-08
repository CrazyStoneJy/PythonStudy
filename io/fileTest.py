#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import json

print(os.name)

# print(os.environ)

# print(os.environ.get('PATH'))

print(os.path.split('/home/crazystone/study_code/pythonStudy/README.md'))

print(os.path.splitext('/home/crazystone/study_code/pythonStudy/README.md'))

dictNum = {23:'asda','das':'da'}
ss = json.dumps(dictNum)
print(ss)

class Student(object):
    name = ''
    id = 0
    address = ''
    
    def __init__(self,id,name,address):
        self.id = id
        self.name = name
        self.address = address
    
s = Student(1,'jiayan','beijing')
def stu2dict(stu):
    return {'id':stu.id,'name':stu.name,'address':stu.address}
jsonString = json.dumps(s,default=stu2dict)
print('jsonString:'+jsonString)