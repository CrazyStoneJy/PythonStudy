#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import functools

s = '12324'
print(int(s))
print(int(s,5))

int2 = functools.partial(int,base=8)
print(int2('234'))