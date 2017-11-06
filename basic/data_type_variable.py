#!/usr/bin/python3

## 字符串
print('hello world')
# 转义字符
print('\\hello world\n woca')
# r表示内部字符不考虑转义
print(r'\\hello world\n woca')
# 多行
print('''hello 
jiayan
hello
china''')

## 布尔变量 and not or
print(1 > 0)
print(1 > 0 and 2 < 4)
print(1 > 0 or 2 < 4)
print(not 1 > 0)

## 运算
# python的除法是精确除/,所以结果是个浮点型
print(10/3)
# python除法，结果为整数//
print(10//3)