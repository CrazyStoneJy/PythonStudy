#!/usr/bin/python3
# -*- encoding: utf-8 -*-

g = (x*x for x in range(10))

print(next(g))
print(next(g))
print(next(g))
print(next(g))

for every in g:
    print(every)


def fib(maxNum):
    n,a,b = 0,0,1
    while n < maxNum:
        a,b = b, a+b
        n = n + 1
        print(b)
    return 'done'

fib(5)

#将fib函数变为生成器
def fib2(maxNum):
    n,a,b = 0,0,1
    while n < maxNum:
        yield b
        a,b = b, a+b
        n = n + 1
        # print(b)
    # return 'done'

# print(fib2(4))
for f in fib2(4):
    print('--' + str(f))



# 含有yield关键字的函数,即为生成器
def step():
    print('step 1')
    yield 1
    print('step 3')
    yield 3
    print('step 5')
    yield 5

s = step()
next(s)
next(s)
next(s)
# next(s)


## 杨辉三角 todo

def triangels(level):
    for i in range(0,level):
        arr = []
        if i == 0:
            arr.append(1)
            yield arr
        elif i == 1:
            arr.append(1)
            arr.append(1)
            yield arr
        else:
            for j in range(i):
                yield arr
                if j==0 or j == i:
                    arr.append(1)
                else:
                    arr.append(arr[j]+arr[j+1])
    
        # if i == 0 or i == level:
        #     print(str('1',end=''))
        # else:
        #     print()

for ll in triangels(5):
    print(ll)