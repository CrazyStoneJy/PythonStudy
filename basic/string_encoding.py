#!/usr/bin/python3
# -*- encode:utf-8 -*-

# ord()函数，获取字符串的utf-8编码
print(ord('s'))
print(ord('中'))
# chr()函数，表示叫字符编码转为字符
print(chr(65))
print(chr(20013))
# 十六进制显示字符
print('\u4e2d\u6587')
# 将bytes转为str
print(b'ABDSD'.decode('utf-8'))
# 将str转为bytes
print('我擦'.encode('utf-8'))

# 计算字符串的长度 len()
print(len('adasdas'.encode('utf-8')))
print(len('adasdas'.encode('ascii')))
# 一个中文3占个字节
print(len('中'.encode('utf-8')))

# 字符串格式化
# %d整数 %f浮点数 %s字符串 %x十六进制整数
print('hello,%s'%'jiayan')
print('hello,%s,%d'%('jiayan',3))
print('%3d-%03d'%(12,3))
print('%.2f'%(3.1425234))
# print(str(PI))