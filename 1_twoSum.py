from typing import List
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