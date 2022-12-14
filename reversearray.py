def reverseArray(a):
    # Write your code here
    for i in range(len(a)//2):
        temp = a[i]
        a[i] = a[len(a)-i-1]
        a[len(a)-i-1] = temp
        
    # a.reverse()
    return a



arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
res = reverseArray(arr)
print(res)
