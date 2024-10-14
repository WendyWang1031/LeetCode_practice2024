"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
# 自己解
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict = {}
        for num in nums :
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
            
            if count_dict[num] > len(nums) // 2:
                return num
            
solution = Solution()
arr = [2,2,1,1,1,2,2]
result = solution.majorityElement(arr)
print(result)
