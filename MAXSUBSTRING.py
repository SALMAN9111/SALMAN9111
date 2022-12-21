# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 11:29:14 2021

@author: Toshiba

"""

def maxsubString(s):
    m = " "
    for i in range(len(s)):
        m = max(m,s[i:])
    return m
s = input()
print(maxsubString(s))
"""
n = [{"name":"sai","age":20},{"names":"so","age":18}]
n.append({"name":"p","age":27})
print(n)
for i in range(len(n)):
    if n[i]["age"]>18:
        print(n[i]["age"])
"""
"""
n = int(input())
lis = []
for i in range(n):
    ele = int(input())
    lis.append(ele)

li = []
s = 0
for i in lis:
    j = i
    while j > 0:
        r = j%10
        j = j//10
        s = s + r
    li.append(s)
    s = 0
print(li)
"""

"""n = int(input())
lis = []
for i in range(n):
    ele = int(input())
    lis.append(ele)

lis = sorted(lis)

m = lis[0]
for i in range(len(lis)):
    if m < lis[i+1]:
        print(lis[i+1])
    break
"""

        








