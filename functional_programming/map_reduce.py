#!/usr/bin/python3
# -*- encode: utf-8 -*-
from functools import reduce

array = [1,2,3,4,5,6,7,8,9]
def power(x):
    return x*x
print(list(map(power,array)))

count = 0
def p(string):
    global count
    print(string)
    count = count + 1
    return count

print(list(map(p,'abc')))

array1 = []
print(sum(array1,3))

def add(a,b):
    return a + b

def iter(x,y):
    return 10*x + y

print(reduce(add,array))

print(reduce(iter,array))



### 将字符串转为int

def genCharDict():
    dicts = {}
    for i in range(10):
        dicts[str(i)] = i
    return dicts

charDict = genCharDict()

def char2int(everyChar):
    global charDict
    return charDict[everyChar]

def fn(x,y):
    return 10*x + y

def str2int(string):
    return reduce(fn,map(char2int,string))

print(str2int('123242'))



## work

arr = ['adam', 'LISA', 'barT']
def maching(string):
    fir = string[0]
    l = len(string)
    rest = string[1:l]
    return fir.upper() + rest.lower()

print(list(map(maching,arr)))

floatNum = float('234.45')
floatNum = floatNum + 1
print(floatNum)