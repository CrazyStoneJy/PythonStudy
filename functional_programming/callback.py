#!/usr/bin/python3
# -*- coding: utf-8 -*-

class A(object):
    a = ''
    def __init__(self,a):
        self.a = a

def callback(a,b):
    print(a,b)

def foo(name,callback):
    callback(1,23)
    print(name)

foo('jiayan',callback)