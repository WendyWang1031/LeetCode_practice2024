# 自己解 使用sort
class Solution1(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sort_arr = sorted(nums,reverse=True)
        return sort_arr[k-1]
    
solution = Solution1()
nums1 = [3,2,1,5,6,4]
k1 = 2
result1 = solution.findKthLargest(nums1,k1)
print(result1)

nums2 = [3,2,3,1,2,4,5,5,6]
k2 = 4
result2 = solution.findKthLargest(nums2,k2)
print(result2)