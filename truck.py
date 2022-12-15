class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        maxUnit : int = 0
        for i in range(len(boxTypes)):
            if(i != ((len(boxTypes)))):
                maxUnit = (boxTypes[i][0] * boxTypes[i][1]) + maxUint
            maxUnit = (boxTypes[i][0] * 1)
               
        return maxUnit	

eBr@J8,V_mLf,Ty


Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8	
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
Example 2:
