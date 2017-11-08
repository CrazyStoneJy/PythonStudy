#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from operator import itemgetter

ll = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(ll)

ll2 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse = True)
print(ll2)

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0].lower()
def by_sorce(t):
    return t[1]

print(sorted(students,key=by_name))
print(sorted(students,key=by_sorce))
print(sorted(students,key=by_sorce,reverse = True))
# print(sorted(students, key=itemgetter(0)))
# print(sorted(students, key=lambda t: t[1]))
# print(sorted(students, key=itemgetter(1), reverse=True))