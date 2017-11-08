#!/usr/bin/python3
# -*- encoding: utf-8 -*-

def foo():
    print('foo')

# 函数名也是变量  foo先是指向一个方法，然后又被指向了一个int类型，所以foo变量已经指向一个值了,再调用foo()便会报异常
# foo()
# foo = 12
# foo()

def add(a,b,c):
    # return c(a,b) + c(b,a)
    c(a,b)
    c(b,a)

def aa(a,b):
    print(str(a),str(b))

def abs2(num):
    return abs(num)
# f = aa()
print(add(-1,-4,aa))