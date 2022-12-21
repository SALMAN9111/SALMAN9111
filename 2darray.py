# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 19:49:55 2021

@author: Toshiba
"""
"""
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0"""

n = 6
m = []
for i in range(n):
    m.append(list(map(int, input().split()[:n])))
    
def sum_glass(m, i, j):
    """Assumes hour-glass is in bounds of m!"""
    return sum(m[i][j:j+3]) + m[i+1][j+1] + sum(m[i+2][j:j+3])

best = float("-inf")
for i in range(4):
    for j in range(4):
        s = sum_glass(m, i, j)
        if s > best:
            best = s
            
print (best)