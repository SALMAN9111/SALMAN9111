# Python3 program to count frequencies
# of array items
def countFreq(arr, n):

	mp = {}

    # Traverse through array elements
	# and count frequencies
	for i in range(n):
		if arr[i] in mp.keys():
			mp[arr[i]] += 1
            
		else:
			mp[arr[i]] = 1
			
	# Traverse through map and print
	# frequencies
	for x in mp:
		print(x, " ",mp[x])

# Driver code
arr = [10, 20, 20, 10, 10, 20, 5, 2]
n = len(arr)
countFreq(arr, n)

