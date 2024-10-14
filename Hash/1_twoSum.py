from typing import List

"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""
# 自解 時間複雜度是 O(n平方)
class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        final = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    final = [i,j]

        return final
    
solution1 = Solution1()
nums = [3,3]
target = 6
result1 = solution1.twoSum(nums, target)
print(result1) 


# 最佳解
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
            
        return []
    
solution2 = Solution2()
nums = [4,8,3,1,7]
target = 8
result2 = solution2.twoSum(nums, target)
print(result2) 

class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i in range (len(nums)):
            if target - nums[i] in numToIndex :
                return numToIndex[target - nums[i]]
            numToIndex[nums[i]] = i
    
solution2 = Solution3()
nums = [4,8,3,1,7]
target = 8
result2 = solution2.twoSum(nums, target)
print(result2) 