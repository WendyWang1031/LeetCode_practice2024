"""
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, 
and 
nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # 1. 首先將數組進行排序
        res = []     # 存儲結果
        n = len(nums)

        # 2. 遍歷每個元素作為固定的數字
        for i in range(n - 2):  # 因為需要三個數字，所以只遍歷到 n-2
            # 跳過重複的數字
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 如果當前數字與前一個數字相同，跳過，避免重複
            
            # 3. 使用雙指針來查找剩下兩個數字
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    # 找到一組三元組
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # 跳過重複的左指針數字
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 跳過重複的右指針數字
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 移動雙指針
                    left += 1
                    right -= 1
                elif total < 0:
                    # 如果總和小於0，移動左指針，增加總和
                    left += 1
                else:
                    # 如果總和大於0，移動右指針，減少總和
                    right -= 1
        
        return res