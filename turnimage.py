# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 14:48:00 2021

@author: Toshiba
"""
"""Turn image 90' degree  
[[1 2 3]
 [4 5 6]
 [7 8 9]]


[[7 4 1]
 [8 5 2]
 [9 6 3]]"""


import numpy as np
n = np.array([[1,2,3],[4,5,6],[7,8,9]])
s = len(n)
print(n)

"""print()
print(len(n))

print(np.shape(n))"""
print()

for i in range(len(n)):
    for j in range(i,len(n)):
        n[i][j] , n[j][i]  = n[j][i] , n[i][j]
print(n,"\n")
        
        
for i in range(len(n)):
    for j in range(len(n)//2):
        n[i][j] , n[i][s-1-j] = n[i][s-1-j] , n[i][j]


print(n)