#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello World')
    elif len(args)==2:
        print('Hello,%s'%(args[1]))
    else:
        print('to much argments')

if __name__ == '__main__':
    test()
