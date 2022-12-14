def staircase(n):
    # Write your code here
        #  *
        # ** 
    for i in range(n):
        for j in range(i,n-1):
            print(" ",end="")
            
        for k in range(0,i+1):
            print("#",end="")
            
        print()

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

    #     1
    #   1 1
    # 1 1 1s
    #  for i in range(n):
    #     for j in range(i,n-1):
    #         print(" ",end=" ")
            
    #     for k in range(0,i+1):
    #         print("# ",end="")
            
    #     print()

    # *
    # * *
    #  for k in range(0,i+1):
    #         print("# ",end=" ")
        
    #     for j in range(i,n-1):
    #         print(" ",end="")
 