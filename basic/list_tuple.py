#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# list列表是有序的，list的索引是可以为负数的，但是不能超过list的len的大小，范围为[-len,len-1)
# 因为python是弱类型的，所以list中为元素可以为任意类型，例如： arraty = [1, 'asd',False] 

array = ['1','2','3']
def traverse():
    for string in array:
        print(string,end=' ')
    print()
# print(array[-3])
# list 向后增加一个元素
array.append('4')
traverse()
# list向制定位置增加元素
array.insert(1,'5')
traverse()
# list删除末尾的元素
array.pop()
traverse()
# list删除指定位置上的元素
array.pop(1)
traverse()

# 字符串为不可变对象
a = 'abc'
b = a.replace('a','A')
# a被replace之后赋值给b，发现a原先指向的还是‘abc’，并没有变化
print(a)
print(b)


# L = [['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']]
# print(L[0][0])
# print(L[-2][-3])
# print(L[2][-1])












