#!/usr/bin/python3
# -*- encoding: utf-8 -*-

def filterFunc(num):
    return num % 2 == 0

array = [2,3,6,7,9]

print(list(filter(filterFunc,array)))    
