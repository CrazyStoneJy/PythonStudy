#!/usr/bin/python3
# -*- encode: utf-8 -*-

array1 = list(range(1,10))
print(array1)

array2 = [x*x for x in range(1,10)]
print(array2)

# 筛选出偶数的平方
array3 = [x*x for x in range(1,10) if x%2==0]
print(array3)

arr = ['12','34','546']

# 两层循环
array4 = [str(m) + str(n) for m in arr for n in 'abcdf']
print(array4)

d = {'a':'1','b':'2','c':'3'}
array5 = [k + '=' + v for k,v in d.items()]
print(array5)


L1 = ['Hello', 'World', 18, 'Apple', None]
array6 = [s.lower() for s in L1 if isinstance(s,str)]
print(array6)