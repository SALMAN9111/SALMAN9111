#  const totalNumbers = arr.length
#   const totalPositives = arr.filter(number => number > 0).length
#   const totalNegatives = arr.filter(number => number < 0).length
#   const totalZeros = arr.filter(number => number === 0).length
  
#   const positives = totalPositives / totalNumbers
#   const negatives = totalNegatives / totalNumbers
#   const zeros = totalZeros / totalNumbers
  
#   console.log(positives.toFixed(6))
#   console.log(negatives.toFixed(6))
#   console.log(zeros.toFixed(6))

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    pos,neg,zero = 0,0,0
    
    for i in arr:
        if(i > 0):
            pos = pos + 1
        elif (i<0):
            neg = neg + 1
        else:
            zero = zero + 1
    print(pos/n,"\n",neg/n,"\n",zero/n)

n = [-4 ,3 ,-9 ,0 ,4 ,1]