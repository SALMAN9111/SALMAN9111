# 1. Two Sum
# Easy

# 34797

# 1097

# Add to List

# Share
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Edge Case :
# 1) Given list=[3,2,3], Target = 6, list = [-1,-2,-3,-4,-5], Target = -8
# For this edge case extra for loop came
# outerCount and the innerCount variable got to be defined to track indexs

#Solution from leetCode class Solution:
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
     #   for i in range(len(nums)):
     #       for j in range(i + 1, len(nums)):
     #           if nums[j] == target - nums[i]:
    #                return [i, j]

# Solution:

class Solution:
    def twoSum(nums, target):
        outerCount: int = 0
        innerCount: int = 0
        lis = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if((nums[i]+nums[j]) == target):
                    lis.append(outerCount), lis.append(innerCount+1)
                    return lis
                innerCount += 1
            outerCount += 1
            innerCount = outerCount
        else:
            return ("The Given Target value is Incorrect. Pls Check.")


print(Solution.twoSum([1,2,3,4,5], 8))
