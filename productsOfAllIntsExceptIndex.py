from datetime import datetime

ls = [1,20,4,6]


def getproduct(x):
    prod = 1
    for i in x:
        prod = prod * i
    return prod

st = datetime.now()
print([getproduct([ls[i] for i in range(len(ls)) if i!= k])for k,el in enumerate(ls)])
print((datetime.now()-st))

print("lll")

st = datetime.now()
l=[]
prod = 1
for i in range(len(ls)):
    for j in range(0,len(ls)):
        if i !=j :
            prod = prod * ls[j]
    l.append(prod)
    prod = 1
print(l)
print((datetime.now()-st))

