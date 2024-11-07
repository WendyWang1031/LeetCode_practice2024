class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        left , right = 0 , n-1

        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                right = mid - 1

            else:
                left = mid + 1
        return n - left

solution = Solution()

# 測試例子 1
citations1 = [0, 1, 3, 5, 6]
print(solution.hIndex(citations1))  

# 測試例子 2
citations2 = [1, 2, 100]
print(solution.hIndex(citations2)) 