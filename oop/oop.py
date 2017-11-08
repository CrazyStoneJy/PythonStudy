#!/usr/bin/python3
# -*- encoding: utf-8 -*-

class MyObj:
    name = ''
    def __init__(self,name):
        self.name = name

obj = MyObj('jiayan')
print(type(obj))
print(hasattr(obj,'x'))
setattr(obj,'x',200)
print(hasattr(obj,'name'))
print(obj.x)

obj.address = 'beijing'
print(obj.address)