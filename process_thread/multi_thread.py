#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#Created by crazystone

import threading
import os
import time
import random

class MyThread(threading.Thread):

    def __init__(self,threadName,fileName):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.fileName = fileName

    def run(self):
        filePath = os.path.join('/home/crazystone/test/',self.fileName)
        for i in range(100):
            time.sleep(random.random())
            with open(filePath,'a+') as f:
                message = 'message' + str(i)
                f.write(message)
                f.write('\n')
                print(self.threadName,message)

def execute():
    threads = []
    for i in range(20):
        t = MyThread('thread'+str(i),'test'+str(i)+'.txt')
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

if __name__ == '__main__':
    execute()
