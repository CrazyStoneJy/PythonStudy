#!/usr/bin/python3
# -*- encode: utf-8 -*-
import os
from multiprocessing import Process

# fork 方法会返回两次
print('pid',os.getpid())
print('ppid',os.getppid())
def forkTest():
    pid = os.fork()
    testPId = os.fork()
    if pid == 0:
        print('i am child process pid:%s,parent process id is %s'%(os.getpid(),os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
    print('>>>')

forkTest()
print('heheh')




