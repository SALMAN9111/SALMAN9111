from tkinter import X


def prints():
    print("Running")

prints()
for x in range(5):
    print(x,end=" ")

lis = ["zlshfk","sldjkl"]
lis = [2,3,6,5,8]
lis = ["zlshfk","sldjkl","qwdiydfj","liuejhks","opqwod"]
# print(sorted(lis))
print(len(lis))
c = 5
print(c)


for x in range(len(lis)):
    for j in range(x,len(lis)):
        if(lis[x] > lis[j]):
            lis[x],lis[j] = lis[j],lis[x]

# print(lis)
l = lambda x :x in lis

print(l(lis))

import string
alpha = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print(L)
print('\n'.join(L[::-1]))


"""
def print_rangoli(n):
    from string import ascii_lowercase as chars
    heap = [(('-'.join(chars[i:n])[::-1]+'-'.join(chars[i:n])[1:])).center(4*n-3, '-')for i in range(n)]
    print(*(heap[::-1]+heap[1:]), sep="\n")
"""