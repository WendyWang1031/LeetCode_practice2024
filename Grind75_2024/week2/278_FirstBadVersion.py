"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:

Input: n = 1, bad = 1
Output: 1
 
"""
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left , right = 1 , n
        while left < right :
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid  # 壞版本可能是 mid，或在左邊
            else:
                left = mid + 1 # 壞版本在 mid 右邊
        return left
    
"""
時間與空間複雜度
時間複雜度：O(log n)，因為我們採用了二分查找。
空間複雜度：O(1)，因為僅使用了有限的變數。
"""