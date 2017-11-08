#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from multiprocessing import *
import os,random,time

def proce(name):
    print('Run Task %s,processId:%s'%(name,os.getpid()))
    start = time.time()
    randomTime = random.random()*3
    time.sleep(randomTime)
    end = time.time()
    print('Task %s,run %fs'%(name,(end-start)))


if __name__ == '__main__':
    print('parent processor id:',os.getpid())
    p = Pool(4)
    for i in range(10):
        p.apply_async(proce,args = (i,))
    print('wating all child process')
    p.close()
    p.join()
    print('all child process done')
