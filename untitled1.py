# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 20:06:22 2021

@author: Toshiba
"""

# function to find the once
# appearing element in array
def findSingle( ar, n):
    lis = []
    for i in range(n):
        m = set(ar)
        f = list(m)
        for j in ar:
            if(f[i]!=j):
                lis.append(f[i])
            
        
        
        #m = 2 * sum(set(ar[i])) - sum(ar[i])
        #lis.append(m)
    #return sum(lis)
    return lis

# Driver code
ar = [2, 3, 5, 9, 4, 5, 3, 4]
print("sum of element occuruing once in given matrix", findSingle(ar, len(ar)))

# This code is contributed by __Devesh Agrawal__
