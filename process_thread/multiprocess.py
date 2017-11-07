#!/usr/bin/python3
# -*- encode: utf-8 -*-
from multiprocessing import *
import multiprocessing
import os

def run_proc(name):
    print('Run child process %s. (%s)...'%(name,os.getpid()))

if __name__ == '__main__':
    print('Parent Processor id %s' % os.getpid())
    print('computer cpu core number:' + str(multiprocessing.cpu_count()))
    p = Process(target = run_proc,args = ('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end.')