#!/usr/bin/python3
# -*- encode:utf-8 -*-

# max可以传多个参数
print(max(2,5,9,-3,-4))

print(hex(31))

def hex2(number):
    #定义一个不可改的元组
    array = ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')
    aux = 16
    results = []
    resultString = '0x'
    try:
        num = int(number)
        # for a in array:
        #     print(a)
        while num > 0:
            res = num % aux
            num = num // aux
            results.insert(0,res)
        for r in results:
            resultString = resultString + array[r]
        return resultString
    except Error as err:
        print('error:',err)

print(hex2(256))

# 返回值多个，是代表一个元组
def move():
    return 9,8
print(move()[1])

# 函数默认参数
def power(number,n = 2):
    temp = number
    for i in range(1,n):
        temp = number * temp
    return temp
print(power(3,3))

# 函数可变参数
def printStr(*strings):
    for string in strings:
        print(string,end = ' ')
    print()

stringArray = ['a','b','c','f']
printStr('hello','world','jiayan','nihao')
# 将元组或者列表当为可变参数
printStr(*stringArray)
print('hello','world','jiayan','nihao')

# 关键字参数  关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def test(id,name,**kw):
    print(str(id),name)
    print(kw)
test(12,'name')
test(13,'array',city = 'Beijing')

## 命名关键字参数(如果没有默认参数，则为必传项)命名关键字参数形式为: *,参数
def test2(name,*,city,address):
    print(name,city,address)
test2('jiayan',city = 'BeiJing',address = 'ChangPing')


## 参数组合 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def foo(a,b='b',*c,d,**kw):
    print(a,b,c,d,kw)
foo('1',*['334','234','asd'],d='woca')
foo('1','2',*['334','234','asd'],d='woca',e = 'hello')

## 递归
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
def f(n):
    if n == 0:
        return 1
    else:
        return f(n-1)*n
# print(f(3))
# print(f(5))
print(f(100))

## 尾递归 递归的优化
def f2(n,res):
    if n == 1:
        return res
    else:
        return f2(n-1,n*res)

def f3(n):
    return f2(n,1)

print(f3(100))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")

# todo 优化9x9的显示效果，空格处对齐
def multi():
    for i in range(1,10):
        for j in range(1,i+1):
            res = i*j
            if (i+1) >= 10:
                futureRes = res
            else:
                futureRes = (i+1)*j
            if isDigit(res,futureRes):
                print(str(j) + '*' + str(i) + '=' + str(res),end = ' ')
            else:
                print(str(j) + '*' + str(i) + '=' + str(res),end = '  ')
        print()

def isDigit(n1,n2):
    return digit(n1) == digit(n2)
def digit(n):
    # temp = n
    index = 0
    while(n > 0):
        index = index + 1
        n = n//10
    return index

multi()


## 汉诺塔
count = 0
# 参数代表的意思 n为盘子的个数，a为原桩,c为目标桩，b为辅助桩
def move(n,a,b,c):
    global count
    if n == 1:
        print(a + ' --> '+ c)
        count = count + 1 
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(3,'A','B','C')
print(count)