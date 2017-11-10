#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import threading
import os,random,time
from multiprocessing import Process
from multiprocessing import Pool
import multiprocessing

# print(threading.current_thread().name)

def loop():
    printCurrentThreadName('start')
    for i in range(10):
        printCurrentThreadName(str(i))
        # time.sleep(random.random()*2)
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

# newThread()

# count = 0

class MyThread(threading.Thread):
    threadName = ''
    num = 0
    def __init__(self,threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName
    
    def run(self):
        
        self.count(0)

    def count(self,num):
        # limit = random.randint(1,20)
        # global count
        limit = 5
        for i in range(limit):
            time.sleep(random.random())
            print(self.threadName + '->' + str(num))
            num = num + 1
            # count = count + 1

def execute(name):
    # print('process->' + str(name))
    processName = 'process->' + str(name)
    threads = []
    for i in range(5):
        t = MyThread(processName + ',thread->' + str(i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


cpuCount = multiprocessing.cpu_count()

p = Pool(cpuCount)
for i in range(cpuCount):
    p.apply_async(execute,args=(i,))
p.close()
p.join()

print('main thread is end.')


# execute('1')