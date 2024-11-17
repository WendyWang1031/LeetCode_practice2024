"""
Given an integer array nums, 
return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


"""
from collections import defaultdict
class Solution(object):
    def containsDuplicate_dict(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 初始化一個字典來記錄每個數字的出現次數
        dict_map = defaultdict(int)
        
        for num in nums:
            dict_map[num] += 1
            if dict_map[num] > 1:
                return True
        return False
    def containsDuplicate_set(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)

solution = Solution()
nums_arr = [1,1,1,3,3,4,3,2,4,2]
result = solution.containsDuplicate_dict(nums_arr)
print(result)

"""
使用字典：
時間複雜度：O(n)，需要遍歷整個 nums 列表。
空間複雜度：O(n)，需要儲存每個數字的計數。
使用集合：
時間複雜度：O(n)，需要遍歷整個 nums 列表來建立集合。
空間複雜度：O(n)，需要儲存每個唯一的數字。
"""