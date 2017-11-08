#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import threading
import os,random,time

# print(threading.current_thread().name)

def loop():
    printCurrentThreadName('start')
    for i in range(10):
        printCurrentThreadName(str(i))
        time.sleep(random.random()*2)
    printCurrentThreadName('end')

def newThread():
    printCurrentThreadName('start')
    t = threading.Thread(target=loop,name='test')
    t.start()
    ''' join表示等线程t执行完后,主线程再执行 '''
    t.join()
    printCurrentThreadName('end')

def printCurrentThreadName(state = ''):
    print('current thread name:' + threading.current_thread().name + ' ' + state)

newThread()