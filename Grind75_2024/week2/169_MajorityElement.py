"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

class Solution(object):
    def majorityElement_map(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dict_map = {}
        for num in nums:
            if num in dict_map:
                dict_map[num] += 1
            else:
                dict_map[num] = 1

            if dict_map[num] > (len(nums) // 2):
                return num
    
    def majorityElement_BoyerMoore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
        for num in nums :
            if count == 0 :
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
   
    
"""
使用字典來計數，時間複雜度是 O(n)，但是空間複雜度為 O(n)


Boyer–Moore majority vote algorithm 多數投票演算法
是一種用於找出具有多數元素的算法，它在陣列中的應用情境以及使用限制如下

使用情境

主要元素檢測： 多數投票演算法主要用於找出陣列中出現次數超過一半的主要元素。這在選舉或投票系統中非常有用，
用於確定最多選票的候選人。
數據流中的眾數：當你需要在數據流中即時找到最多出現的元素，摩爾投票算法可以動態處理數據並找出眾數。


這樣的更新方式基於「多數元素」的特性：它出現的次數多於其他所有元素的總和。

時間和空間複雜度
時間複雜度：O(n)，因為只需遍歷數組一次。
空間複雜度：O(1)，因為只使用了常數空間。
"""