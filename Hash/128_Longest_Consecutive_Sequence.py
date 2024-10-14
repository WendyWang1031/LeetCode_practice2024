"""
Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

"""

# 自己解
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0

        sort_arr = sorted(set(nums))
        print(sort_arr)
        
        result = []
        count = 1

        for i in range(1,len(sort_arr)):
            if sort_arr[i] == sort_arr[i-1] +1:
                count += 1
            else:
                result.append(count)
                count = 1 
        result.append(count)
        return max(result)
    
solution1 = Solution()
nums1 = [100,4,200,1,3,2]
result1 = solution1.longestConsecutive(nums1)
print(result1)

solution2 = Solution()
nums2 = [0,3,7,2,5,8,4,6,0,1]
result2 = solution2.longestConsecutive(nums2)
print(result2)

# Arthur 解法
# 第一個效能較好
def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length = 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue
            next_num = num + 1
            count = 1
            while next_num in nums_set:
                count += 1
                next_num += 1
            if count > length:
                length = count

        return length

def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length = 0

        for num in nums:
            count = 0
            if num - 1 in nums_set:
                continue
            next_num = num
            while next_num in nums_set:
                count += 1
                next_num += 1
            if count > length:
                length = count

        return length

# chatGPT 寫法
def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
        return 0
    
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_num_srteak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_num_srteak +=1
            
            longest_streak = max(longest_streak, current_num_srteak)
    return longest_streak