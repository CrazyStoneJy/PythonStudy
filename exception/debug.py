#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)

def foo(number):
    # assert number != 0 , 'n is zero'
    logging.info('woca')
    return 10 / number

foo(0)

# python3 -O debug.py   参数-O表示禁止断言