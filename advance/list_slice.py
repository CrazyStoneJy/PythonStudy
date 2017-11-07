#!/usr/bin/python3
# -*- encode:utf-8 -*-
from collections import Iterable
from bs4 import BeautifulSoup


array = ['Alice','Bob','Curry','Dnoraze','Davice']
print(array[0:3])
print(array[:3])
print(array[-3:-1])
print(array[-2:])

numbers = []
for i in range(100):
    numbers.append(i)
# 前10个数，每两个取一个
print(numbers[:10:2])
# 所有数，每5个取一个
print(numbers[::5])


print(isinstance('abc',Iterable))

print(isinstance(numbers,Iterable))

print(isinstance((23,'343',23),Iterable))

for s in 'abc':
    print(s)

# Python内置的enumerate函数可以把一个list变成索引-元素对
for i,n in enumerate(numbers):
    print(i,n)

print('')