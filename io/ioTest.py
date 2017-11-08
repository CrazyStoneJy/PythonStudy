#!/usr/bin/python3
# -*- coding: utf-8 -*-
from io import StringIO,BytesIO

f = StringIO()
f.write('hello\n')
f.write('world')

print(f.getvalue())

