#!/usr/bin/python3
# -*- coding: utf-8 -*-

isDebug = True

def log(message):
    if isDebug:
        if isinstance(message,str):
            print(message)
        elif isinstance(message,int):
            print(str(message))
        elif isinstance(message,float):
            print(str(message))
        else:
            print(message)

def disable():
    global isDebug
    isDebug = False
# log()
