# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 07:07:49 2021

@author: Toshiba
"""


# Complete the solve function below.
def solve(s):
    for m in s[:].split():
        s = (s.replace(m,m.capitalize()))
    return s
s = input()
print(solve(s))





"""
name1 = input()
name2 = input()
name3 = input()
print(list(name1))

print(name1.capitalize() + name2.capitalize()
                         + name3.capitalize())
"""