import math
import os
import random
import re
import sys

def simpleArraySum(ar):
    # Write your code here
    return iSum(ar)



def iSum(ar):
    s = 0
    for i in range(len(ar)):
        s = ar[i] + s
    return s

ar = list(map(int, input().rstrip().split()))

print(simpleArraySum(ar))


    