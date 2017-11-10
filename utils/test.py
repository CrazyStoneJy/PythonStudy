#!/usr/bin/python3
# -*- coding: utf-8 -*-
from Log import log
import Log


log('woca')
log(12)
Log.disable()
log(12.3)

class Student(object):
    name = ''
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return self.name

s = Student('jiayan')
log(s)
print(Log.isDebug)