def diagonalDifference(arr):
    # Write your code here
    lD, rD =0,0
    count =len(arr) -1
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                lD = lD + arr[i][j]
                rD = rD + arr[i][count]
                count = count -1
            # if i+j == len(arr)-1:
            #     rD = rD = arr[j][i]
    # print(lD,rD)
    return abs(lD-rD)

mat = [[1,2,3],[4,5,6],[9,8,9]]

print(diagonalDifference(mat))



# for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))

