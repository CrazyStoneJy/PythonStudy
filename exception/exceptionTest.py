#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging


## 捕获异常
def divide(num):
    try: 
        return num/0
    except Exception as e:
        # logging.exception(e)
        return 0
    finally:
        print('it is done')

print(divide(10))


### 抛异常

def test(num):
    if num == 0:
        raise ValueError('can not be zero')
    else:
        print('success')

test(0)
