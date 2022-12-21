# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 14:55:01 2021

@author: Toshiba
"""

lis = [5,5,6,6,7,5,8,7,9,6,3,2,1,4,5]
lists = []
for i in range(len(lis)):
    if(lis[i] in lists):
        continue
    print(lis.count(lis[i]),lis[i])
    lists.append(lis[i])